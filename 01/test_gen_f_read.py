import unittest
from gen_f_read import gen


class Test(unittest.TestCase):
    def setUp(self):
        print("SETUP")

    def tearDown(self):
        print("TEAR_DOWN")

    def test_gen(self):
        words = ["52", "сортировка", "ро"]
        test_file = "test.txt"
        with open(test_file, "w") as f:
            f.write("сортировка чисел\n")
            f.write("Роботы и люди\n")
            f.write("52-выход на связь\n")
            f.write("Как управлять роботами\n")
            f.close()
            g = gen(test_file, words)

            result = [i for i in g]
            expected = ["сортировка чисел\n"]
            self.assertEqual(result, expected)

    def test_gen_with_case_insensitive(self):
        words = ["52", "СоРтИрОвКа", "ро"]
        test_file = "test.txt"
        with open(test_file, "w") as f:
            f.write("сОрТиРоВкА чисел\n")
            f.write("Роботы и люди\n")
            f.write("52-выход на связь\n")
            f.write("Как управлять роботами\n")
            f.close()
            g = gen(test_file, words)

            result = [i for i in g]
            expected = ["сОрТиРоВкА чисел\n"]
            self.assertEqual(result, expected)

    def test_gen_with_multiple_filters_in_line(self):
        words = ["52", "СоРтИрОвКа", "ро"]
        test_file = "test.txt"
        with open(test_file, "w") as f:
            f.write("сОрТиРоВкА ро\n")
            f.write("Роботы и люди\n")
            f.write("52-выход на связь\n")
            f.write("Как управлять роботами\n")
            f.close()
            g = gen(test_file, words)

            result = [i for i in g]
            expected = ["сОрТиРоВкА ро\n"]
            self.assertEqual(result, expected)

    def test_gen_with_filter_matches_string(self):
        words = ["52", "СоРтИрОвКа", "ро"]
        test_file = "test.txt"
        with open(test_file, "w") as f:
            f.write("сОрТиРоВкА\n")
            f.write("Роботы и люди\n")
            f.write("52-выход на связь\n")
            f.write("Как управлять роботами\n")
            f.close()
            g = gen(test_file, words)

            result = [i for i in g]
            expected = ["сОрТиРоВкА\n"]
            self.assertEqual(result, expected)

    def test_gen_with_several_matches(self):
        words = ["52", "сортировка", "ро"]
        test_file = "test.txt"
        with open(test_file, "w") as f:
            f.write("Сортировка чисел\n")
            f.write("Роботы и люди\n")
            f.write("52-выход на связь\n")
            f.write("Как управлять роботами\n")
            f.write("52 кошки\n")
            f.close()
            g = gen(test_file, words)

            result = [i for i in g]
            expected = ["Сортировка чисел\n", "52 кошки\n"]
            self.assertEqual(result, expected)

    def test_gen_empty_file(self):
        words = ["52", "сортировка", "ро"]
        test_file = "test.txt"
        with open(test_file, "w") as f:
            f.close()
            g = gen(test_file, words)

            result = [i for i in g]
            expected = []
            self.assertEqual(result, expected)

    def test_gen_empty_words(self):
        words = []
        test_file = "test.txt"
        with open(test_file, "w") as f:
            f.write("Сортировка чисел\n")
            f.write("Роботы и люди\n")
            f.write("52-выход на связь\n")
            f.write("Как управлять роботами\n")
            f.close()
            g = gen(test_file, words)

            result = [i for i in g]
            expected = []
            self.assertEqual(result, expected)

    def test_gen_empty_file_and_words(self):
        words = []
        test_file = "test.txt"
        with open(test_file, "w") as f:
            f.close()
            g = gen(test_file, words)

            result = [i for i in g]
            expected = []
            self.assertEqual(result, expected)

    def test_gen_isinstance_file(self):
        words = ["Сортировка"]
        f = open("test.txt", "w")
        f.write("Сортировка чисел\n")
        f.write("Роботы и люди\n")
        f.write("52-выход на связь\n")
        f.write("Как управлять роботами\n")
        f.close()
        f = open("test.txt", "r")
        g = gen(f, words)

        result = [i for i in g]
        expected = ["Сортировка чисел\n"]
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
