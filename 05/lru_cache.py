from Node import Node


class lru_cache:
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
