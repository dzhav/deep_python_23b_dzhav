import unittest
from server import Master, Worker, crawl_url
import socket
import threading
import json
from queue import Queue


class TestServer(unittest.TestCase):
    def setUp(self):
        print("SETUP")

    def tearDown(self):
        print("TEAR_DOWN")

    def test_crawl_url(self):
        url = "https://example.com"
        k = 5
        result = crawl_url(url, k)
        self.assertIsInstance(result, str)

    def test_worker_init(self):
        stats_lock = threading.Lock()
        stats = {'amount_urls': 0}
        task_queue = Queue()
        worker = Worker(k=5, stats_lock=stats_lock, stats=stats, task_queue=task_queue)
        self.assertEqual(worker.k, 5)


if __name__ == '__main__':
    unittest.main()
