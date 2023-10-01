import unittest

from mmf import SomeModel
from mmf import predict_message_mood


class Test(unittest.TestCase):
    def setUp(self):
        print("SETUP")

    def tearDown(self):
        print("TEAR_DOWN")

    def test_somemodel_predict(self):
        model = SomeModel()
        self.assertEqual(0.54, model.predict("111111"))

    def test_somemodel_predict_empty(self):
        model = SomeModel()
        self.assertEqual(0.24, model.predict(""))

    def test_ans_predict_neud(self):
        model = SomeModel()
        self.assertEqual("неуд", predict_message_mood("1", model))

    def test_ans_predict_norm(self):
        model = SomeModel()
        self.assertEqual("норм", predict_message_mood("12", model))

    def test_ans_predict_otl(self):
        model = SomeModel()
        self.assertEqual("отл",
                         predict_message_mood("abrakadabra12345", model))

    def test_ans_predict_empty(self):
        model = SomeModel()
        self.assertEqual("неуд", predict_message_mood("", model))
