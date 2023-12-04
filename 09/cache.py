import argparse
import logging


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prevnode = None
        self.nextnode = None


class LRUCache:
    def __init__(self, limit=42):
        self.limit = limit
        self.cache = {}
        self.head = None
        self.tail = None

    def set(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.move_to_front(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self.add_to_front(node)
            if self.limit < len(self.cache):
                del self.cache[self.remove_last().key]

    def remove_last(self):
        removed_node = self.tail
        if self.tail != self.head:
            self.tail = removed_node.prevnode
            self.tail.nextnode = None
        else:
            self.head = None
            self.tail = None
        return removed_node

    def get(self, key):
        if key not in self.cache:
            return None
        self.move_to_front(self.cache[key])
        return self.cache[key].value

    def add_to_front(self, node):
        if self.head is not None:
            node.nextnode = self.head
            self.head.prevnode = node
        else:
            self.tail = node
        self.head = node

    def move_to_front(self, node):
        if node == self.head:
            return
        if node == self.tail:
            self.tail = node.prevnode
        if node.prevnode is not None:
            node.prevnode.nextnode = node.nextnode
        if node.nextnode is not None:
            node.nextnode.prevnode = node.prevnode
        self.add_to_front(node)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', action='store_true')
    parser.add_argument('-f', action='store_true')
    args = parser.parse_args()

    log_format = '%(asctime)s | %(levelname)s | %(message)s'

    if args.s:
        logging.basicConfig(level=logging.DEBUG, format=log_format)
    else:
        logging.basicConfig(level=logging.DEBUG, format=log_format, filename='cache.log')

    if args.f:
        class CustomFilter(logging.Filter):
            def filter(self, record):
                return len(record.msg.split()) == 4
        logger = logging.getLogger()
        logger.addFilter(CustomFilter())
    else:
        logger = logging.getLogger()

    cache = LRUCache(5)
    cache.set(1, 'dog')
    cache.set(2, 'cat')
    logging.info(f'Get key 1: {cache.get(1)}')
    logging.info(f'Get key 3: {cache.get(3)}')
    logging.warning('This is warning')
    logging.error('This is error')


if __name__ == "__main__":
    main()
