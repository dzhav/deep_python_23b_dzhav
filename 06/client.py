import argparse
import socket
from concurrent.futures import ThreadPoolExecutor


class Client:
    def __init__(self, host, port, urls_file, num_threads):
        self.host = host
        self.port = port
        self.urls_file = urls_file
        self.num_threads = num_threads

    def process_url(self, url):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((self.host, self.port))
        client_socket.send(url.encode())
        print(f"{url.strip()}: {client_socket.recv(1024).decode()}")
        client_socket.close()

    def run(self):
        with open(self.urls_file, 'r') as file:
            urls = file.readlines()

        step = len(urls) // self.num_threads
        url_steps = []
        for i in range(0, len(urls), step):
            chunk = urls[i:i + step]
            url_steps.append(chunk)

        with ThreadPoolExecutor(max_workers=self.num_threads) as executor:
            for url_step in url_steps:
                executor.map(self.process_url, url_step)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("threads", type=int)
    parser.add_argument("urls_file", type=str)
    args = parser.parse_args()

    client = Client("127.0.0.1", 7777, args.urls_file, args.threads)
    client.run()
