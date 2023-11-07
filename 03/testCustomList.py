import unittest
from CustomList import CustomList


class TestCustomList(unittest.TestCase):
    def setUp(self):
        print("SETUP")

    def tearDown(self):
        print("TEAR_DOWN")

    def test_add_custom_regular(self):
        lst1 = CustomList([1, 2, 3])
        lst2 = [1, 2]
        lst3 = [5, 6, 7, 8]
        lst4 = []
        lst5 = [-1, -2, -3]
        self.assertTrue((lst1 + lst2).element_wise_comparison(CustomList([2, 4, 3])))
        self.assertTrue(lst1.element_wise_comparison(CustomList([1, 2, 3])))
        self.assertEqual(lst2, [1, 2])
        self.assertTrue((lst1 + lst3).element_wise_comparison(CustomList([6, 8, 10, 8])))
        self.assertTrue(lst1.element_wise_comparison(CustomList([1, 2, 3])))
        self.assertEqual(lst3, [5, 6, 7, 8])
        self.assertTrue((lst1 + lst4).element_wise_comparison(lst1))
        self.assertTrue(lst1.element_wise_comparison(CustomList([1, 2, 3])))
        self.assertEqual(lst4, [])
        self.assertTrue((lst1 + lst5).element_wise_comparison(CustomList([0, 0, 0])))
        self.assertTrue(lst1.element_wise_comparison(CustomList([1, 2, 3])))
        self.assertEqual(lst5, [-1, -2, -3])

    def test_add_regular_custom(self):
        lst1 = [1, 2, 3]
        lst2 = CustomList([1, 2])
        lst3 = CustomList([5, 6, 7, 8])
        lst4 = CustomList([])
        lst6 = CustomList([1, 2, 3])
        lst5 = CustomList([-1, -2, -3])
        self.assertTrue((lst1 + lst2).element_wise_comparison(CustomList([2, 4, 3])))
        self.assertEqual(lst1, [1, 2, 3])
        self.assertTrue(lst2.element_wise_comparison(CustomList([1, 2])))
        self.assertTrue((lst1 + lst3).element_wise_comparison(CustomList([6, 8, 10, 8])))
        self.assertEqual(lst1, [1, 2, 3])
        self.assertTrue(lst3.element_wise_comparison(CustomList([5, 6, 7, 8])))
        self.assertTrue((lst1 + lst4).element_wise_comparison(lst6))
        self.assertTrue(lst6.element_wise_comparison(CustomList([1, 2, 3])))
        self.assertTrue(lst4.element_wise_comparison(CustomList([])))
        self.assertTrue((lst1 + lst5).element_wise_comparison(CustomList([0, 0, 0])))
        self.assertEqual(lst1, [1, 2, 3])
        self.assertTrue(lst5.element_wise_comparison(CustomList([-1, -2, -3])))

    def test_add_custom_custom(self):
        lst1 = CustomList([1, 2, 3])
        lst2 = CustomList([1, 2])
        lst3 = CustomList([5, 6, 7, 8])
        lst4 = CustomList([])
        lst5 = CustomList([-1, -2, -3])
        self.assertTrue((lst1 + lst2).element_wise_comparison(CustomList([2, 4, 3])))
        self.assertTrue(lst1.element_wise_comparison(CustomList([1, 2, 3])))
        self.assertTrue(lst2.element_wise_comparison(CustomList([1, 2])))
        self.assertTrue((lst1 + lst3).element_wise_comparison(CustomList([6, 8, 10, 8])))
        self.assertTrue(lst1.element_wise_comparison(CustomList([1, 2, 3])))
        self.assertTrue(lst3.element_wise_comparison(CustomList([5, 6, 7, 8])))
        self.assertTrue((lst1 + lst4).element_wise_comparison(lst1))
        self.assertTrue(lst1.element_wise_comparison(CustomList([1, 2, 3])))
        self.assertTrue(lst4.element_wise_comparison(CustomList([])))
        self.assertTrue((lst1 + lst5).element_wise_comparison(CustomList([0, 0, 0])))
        self.assertTrue(lst1.element_wise_comparison(CustomList([1, 2, 3])))
        self.assertTrue(lst5.element_wise_comparison(CustomList([-1, -2, -3])))

    def test_subtract_custom_regular(self):
        lst1 = CustomList([1, 2, 3])
        lst2 = [1, 2]
        lst3 = [5, 6, 7, 8]
        lst4 = []
        lst5 = [-1, -2, -3]
        self.assertTrue((lst1 - lst2).element_wise_comparison(CustomList([0, 0, 3])))
        self.assertTrue(lst1.element_wise_comparison(CustomList([1, 2, 3])))
        self.assertEqual(lst2, [1, 2])
        self.assertTrue((lst1 - lst3).element_wise_comparison(CustomList([-4, -4, -4, -8])))
        self.assertTrue(lst1.element_wise_comparison(CustomList([1, 2, 3])))
        self.assertEqual(lst3, [5, 6, 7, 8])
        self.assertTrue((lst1 - lst4).element_wise_comparison(lst1))
        self.assertTrue(lst1.element_wise_comparison(CustomList([1, 2, 3])))
        self.assertEqual(lst4, [])
        self.assertTrue((lst1 - lst5).element_wise_comparison(CustomList([2, 4, 6])))
        self.assertTrue(lst1.element_wise_comparison(CustomList([1, 2, 3])))
        self.assertEqual(lst5, [-1, -2, -3])

    def test_subtract_regular_custom(self):
        lst1 = [1, 2, 3]
        lst2 = CustomList([1, 2])
        lst3 = CustomList([5, 6, 7, 8])
        lst4 = CustomList([])
        lst5 = CustomList([-1, -2, -3])
        lst6 = CustomList(lst1)
        self.assertTrue((lst1 - lst2).element_wise_comparison(CustomList([0, 0, 3])))
        self.assertEqual(lst1, [1, 2, 3])
        self.assertTrue(lst2.element_wise_comparison(CustomList([1, 2])))
        self.assertTrue((lst1-lst3).element_wise_comparison(CustomList([-4, -4, -4, -8])))
        self.assertEqual(lst1, [1, 2, 3])
        self.assertTrue(lst3.element_wise_comparison(CustomList([5, 6, 7, 8])))
        self.assertTrue((lst1 - lst4).element_wise_comparison(lst6))
        self.assertTrue(lst6.element_wise_comparison(CustomList([1, 2, 3])))
        self.assertTrue(lst4.element_wise_comparison(CustomList([])))
        self.assertTrue((lst1 - lst5).element_wise_comparison(CustomList([2, 4, 6])))
        self.assertEqual(lst1, [1, 2, 3])
        self.assertTrue(lst5.element_wise_comparison(CustomList([-1, -2, -3])))

    def test_subtract_regular_regular(self):
        lst1 = CustomList([1, 2, 3])
        lst2 = CustomList([1, 2])
        lst3 = CustomList([5, 6, 7, 8])
        lst4 = CustomList([])
        lst5 = CustomList([-1, -2, -3])
        self.assertTrue((lst1 - lst2).element_wise_comparison(CustomList([0, 0, 3])))
        self.assertTrue(lst1.element_wise_comparison(CustomList([1, 2, 3])))
        self.assertTrue(lst2.element_wise_comparison(CustomList([1, 2])))
        self.assertTrue((lst1-lst3).element_wise_comparison(CustomList([-4, -4, -4, -8])))
        self.assertTrue(lst1.element_wise_comparison(CustomList([1, 2, 3])))
        self.assertTrue(lst3.element_wise_comparison(CustomList([5, 6, 7, 8])))
        self.assertTrue((lst1 - lst4).element_wise_comparison(lst1))
        self.assertTrue(lst1.element_wise_comparison(CustomList([1, 2, 3])))
        self.assertTrue(lst4.element_wise_comparison(CustomList([])))
        self.assertTrue((lst1 - lst5).element_wise_comparison(CustomList([2, 4, 6])))
        self.assertTrue(lst1.element_wise_comparison(CustomList([1, 2, 3])))
        self.assertTrue(lst5.element_wise_comparison(CustomList([-1, -2, -3])))

    def test_comparison(self):
        lst1 = CustomList([1, 2, 3])
        lst2 = CustomList([14, 15, 10])
        lst3 = CustomList([1, 2, 3])
        lst4 = CustomList([1, 5])
        self.assertTrue(lst2 > lst1)
        self.assertTrue(lst2.element_wise_comparison(CustomList([14, 15, 10])))
        self.assertTrue(lst1.element_wise_comparison(CustomList([1, 2, 3])))
        self.assertTrue(lst2 >= lst1)
        self.assertTrue(lst2.element_wise_comparison(CustomList([14, 15, 10])))
        self.assertTrue(lst1.element_wise_comparison(CustomList([1, 2, 3])))
        self.assertTrue(lst1 < lst2)
        self.assertTrue(lst2.element_wise_comparison(CustomList([14, 15, 10])))
        self.assertTrue(lst1.element_wise_comparison(CustomList([1, 2, 3])))
        self.assertTrue(lst1 <= lst2)
        self.assertTrue(lst2.element_wise_comparison(CustomList([14, 15, 10])))
        self.assertTrue(lst1.element_wise_comparison(CustomList([1, 2, 3])))
        self.assertTrue(lst1 == lst3)
        self.assertTrue(lst3.element_wise_comparison(CustomList([1, 2, 3])))
        self.assertTrue(lst1.element_wise_comparison(CustomList([1, 2, 3])))
        self.assertTrue(lst1 == lst4)
        self.assertTrue(lst4.element_wise_comparison(CustomList([1, 5])))
        self.assertTrue(lst1.element_wise_comparison(CustomList([1, 2, 3])))
        self.assertTrue(lst1 != lst2)
        self.assertTrue(lst2.element_wise_comparison(CustomList([14, 15, 10])))
        self.assertTrue(lst1.element_wise_comparison(CustomList([1, 2, 3])))

    def test_str(self):
        lst = CustomList([1, 2, 3])
        lst2 = CustomList([1, 2, 4])
        lst3 = CustomList([])
        self.assertEqual(str(lst3), "[] (0)")
        self.assertTrue(lst3.element_wise_comparison(CustomList([])))
        self.assertEqual(str(lst2), "[1, 2, 4] (7)")
        self.assertTrue(lst2.element_wise_comparison(CustomList([1, 2, 4])))
        self.assertEqual(str(lst), "[1, 2, 3] (6)")
        self.assertTrue(lst.element_wise_comparison(CustomList([1, 2, 3])))


if __name__ == "__main__":
    unittest.main()
