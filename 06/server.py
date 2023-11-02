import socket
import threading
import json
from queue import Queue
import requests
from bs4 import BeautifulSoup
from collections import Counter
import argparse


class Worker(threading.Thread):
    def __init__(self, k, stats_lock, stats, task_queue):
        super().__init__()
        self.k = k
        self.stats_lock = stats_lock
        self.stats = stats
        self.task_queue = task_queue

    def run(self):
        while True:
            client_socket = self.task_queue.get()
            url = client_socket.recv(1000).decode()
            if not url:
                break
            data = crawl_url(url, self.k)
            response = json.dumps(data)
            client_socket.send(response.encode())
            with self.stats_lock:
                self.stats['amount_urls'] += 1
            print(f"amount urls: {self.stats['amount_urls']}")
            client_socket.close()


def crawl_url(url, k):
    response = requests.get(url)
    page_text = response.text
    soup = BeautifulSoup(page_text, 'html.parser')
    text = soup.get_text()
    words = text.split()    
    word_count = Counter(words)
    top_words = word_count.most_common(k)
    result = dict((word, count) for word, count in top_words)
    return json.dumps(result)


class Master:
    def __init__(self, host, port, w, k):
        self.host = host
        self.port = port
        self.w = w
        self.k = k

    def run(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.host, self.port))
        server_socket.listen()

        stats_lock = threading.Lock()
        stats = {'amount_urls': 0}

        workers = []
        task_queue = Queue()

        for _ in range(self.w):
            worker = Worker(self.k, stats_lock, stats, task_queue)
            worker.start()
            workers.append(worker)

        while True:
            client_socket, client_address = server_socket.accept()
            task_queue.put(client_socket)
            print(f"Accepted connection from {client_address}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", type=int)
    parser.add_argument("-k", type=int)
    args = parser.parse_args()

    server = Master("127.0.0.1", 7777, args.w, args.k)
    server.run()
