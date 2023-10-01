import unittest

from gen_f_read import gen


class Test(unittest.TestCase):
    def setUp(self):
        print("SETUP")

    def tearDown(self):
        print("TEAR_DOWN")

    def test_gen(self):
        a = ["52", "сортировка", "ро"]
        test_file = "test.txt"
        with open(test_file, "w") as f:
            f.write("Сортировка чисел\n")
            f.write("Роботы и люди\n")
            f.write("52-выход на связь\n")
            f.write("Как управлять роботами\n")
            f.close()
            g = gen(test_file, a)

            result = [i for i in g]
            expected = ["Сортировка чисел\n"]
            self.assertEqual(result, expected)

    def test_gen_empty_file(self):
        a = ["52", "сортировка", "ро"]
        test_file = "test.txt"
        with open(test_file, "w") as f:
            f.close()
            g = gen(test_file, a)

            result = [i for i in g]
            expected = []
            self.assertEqual(result, expected)

    def test_gen_empty_a(self):
        a = []
        test_file = "test.txt"
        with open(test_file, "w") as f:
            f.write("Сортировка чисел\n")
            f.write("Роботы и люди\n")
            f.write("52-выход на связь\n")
            f.write("Как управлять роботами\n")
            f.close()
            g = gen(test_file, a)

            result = [i for i in g]
            expected = []
            self.assertEqual(result, expected)
