import unittest
from CustomList import CustomList


class TestCustomList(unittest.TestCase):
    def setUp(self):
        print("SETUP")

    def tearDown(self):
        print("TEAR_DOWN")

    def test_add(self):
        lst1 = CustomList([1, 2, 3])
        lst2 = CustomList([4, 5, 6])
        lst3 = CustomList([7, 8, 9])
        self.assertEqual(lst1 + [], lst1)
        self.assertEqual(lst1 + [4, 5], CustomList([5, 7, 3]))
        self.assertEqual(lst1 + lst2, CustomList([5, 7, 9]))
        self.assertEqual(lst1 + [4, 5, 6], CustomList([5, 7, 9]))
        self.assertEqual([4, 5, 6] + lst1, CustomList([5, 7, 9]))
        self.assertEqual(lst1 + lst3, CustomList([8, 10, 12]))

    def test_subtract(self):
        lst1 = CustomList([1, 2, 3])
        lst2 = CustomList([4, 5, 6])
        self.assertEqual(lst1 - lst2, CustomList([-3, -3, -3]))
        self.assertEqual(lst1 - [4, 5, 6], CustomList([-3, -3, -3]))
        self.assertEqual([4, 5, 6] - lst1, CustomList([3, 3, 3]))
        self.assertEqual([4, 5, 6] - CustomList([1, 2]), CustomList([3, 3, 6]))

    def test_comparison(self):
        lst1 = CustomList([1, 2, 3])
        lst2 = CustomList([14, 15, 10])
        lst3 = CustomList([1, 2, 3])
        self.assertTrue(lst2 > lst1)
        self.assertTrue(lst2 >= lst1)
        self.assertTrue(lst1 < lst2)
        self.assertTrue(lst1 <= lst2)
        self.assertTrue(lst1 == lst3)
        self.assertTrue(lst1 == CustomList([1, 2, 3]))
        self.assertTrue(lst1 != lst2)

    def test_str(self):
        lst = CustomList([1, 2, 3])
        lst2 = CustomList([1, 2, 4])
        self.assertEqual(str(CustomList([])), "[] (0)")
        self.assertEqual(str(lst2), "[1, 2, 4] (7)")
        self.assertEqual(str(lst), "[1, 2, 3] (6)")


if __name__ == "__main__":
    unittest.main()
