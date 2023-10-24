import unittest
from LRUCache import LRUCache


class Test(unittest.TestCase):
    def setUp(self):
        print("SETUP")

    def tearDown(self):
        print("TEAR_DOWN")

    def test_set_and_get(self):
        cache = LRUCache(2)
        cache.set("k1", "val1")
        cache.set("k2", "val2")

        self.assertIsNone(cache.get("k3"))
        self.assertEqual(cache.get("k2"), "val2")
        self.assertEqual(cache.get("k1"), "val1")
        self.assertNotEqual(cache.get("k1"), "val2")

        cache.set("k2", "val3")
        self.assertEqual(cache.get("k2"), "val3")

    def test_set_and_get_with_replacement(self):
        cache = LRUCache(2)
        cache.set("k1", "val1")
        cache.set("k2", "val2")
        cache.set("k1", "val3")

        self.assertEqual(cache.get("k1"), "val3")
        self.assertNotEqual(cache.get("k1"), "val1")
        self.assertEqual(cache.get("k2"), "val2")

    def test_set_and_get_with_limit(self):
        cache = LRUCache(2)
        cache.set("k1", "val1")
        cache.set("k2", "val2")
        cache.set("k3", "val3")
        self.assertIsNone(cache.get("k1"))
        self.assertEqual(cache.get("k2"), "val2")
        self.assertEqual(cache.get("k3"), "val3")

        cache = LRUCache(2)
        cache.set("k1", "val1")
        cache.set("k2", "val2")
        flag = cache.get("k1")
        cache.set("k3", "val3")
        self.assertIsNone(cache.get("k2"))
        self.assertEqual(cache.get("k1"), "val1")
        self.assertEqual(cache.get("k3"), "val3")

if __name__ == '__main__':
    unittest.main()
