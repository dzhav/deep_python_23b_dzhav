import unittest
from unittest.mock import MagicMock

from mmf import predict_message_mood


class Test(unittest.TestCase):
    def setUp(self):
        print("SETUP")

    def tearDown(self):
        print("TEAR_DOWN")

    def test_ans_predict_good_norm(self):
        model_mock = MagicMock()
        model_mock.predict.return_value = 0.8
        result = predict_message_mood("Hello world!", model_mock)
        self.assertEqual(result, "норм")
        model_mock.predict.assert_called_once_with("Hello world!")

    def test_ans_predict_bad_norm(self):
        model_mock = MagicMock()
        model_mock.predict.return_value = 0.3
        result = predict_message_mood("12", model_mock)
        self.assertEqual("норм", result)
        model_mock.predict.assert_called_once_with("12")

    def test_ans_predict_neud(self):
        model_mock = MagicMock()
        model_mock.predict.return_value = 0.25
        result = predict_message_mood("1", model_mock)
        self.assertEqual("неуд", result)
        model_mock.predict.assert_called_once_with("1")

    def test_ans_predict_otl(self):
        model_mock = MagicMock()
        model_mock.predict.return_value = 1
        result = predict_message_mood("abrakadabra12345", model_mock)
        self.assertEqual("отл", result)
        model_mock.predict.assert_called_once_with("abrakadabra12345")

    def test_ans_predict_empty(self):
        model_mock = MagicMock()
        model_mock.predict.return_value = 0.20
        result = predict_message_mood("", model_mock)
        self.assertEqual("неуд", result)
        model_mock.predict.assert_called_once_with("")

    def test_ans_predict_bad_norm_good(self):
        model_mock = MagicMock()
        model_mock.predict.return_value = 0.35
        result = predict_message_mood("dog", model_mock)
        self.assertEqual("норм", result)
        model_mock.predict.assert_called_once_with("dog")

    def test_ans_predict_change_thresholds_neud(self):
        model_mock = MagicMock()
        model_mock.predict.return_value = 0.4
        result = predict_message_mood("tort", model_mock, 0.5, 0.9)
        self.assertEqual("неуд", result)
        model_mock.predict.assert_called_once_with("tort")

    def test_ans_predict_change_thresholds_norm(self):
        model_mock = MagicMock()
        model_mock.predict.return_value = 0.6
        result = predict_message_mood("bant1234", model_mock, 0.5, 0.9)
        self.assertEqual("норм", result)
        model_mock.predict.assert_called_once_with("bant1234")

    def test_ans_predict_change_thresholds_otl(self):
        model_mock = MagicMock()
        model_mock.predict.return_value = 1
        result = predict_message_mood("message123456789", model_mock, 0.5, 0.9)
        self.assertEqual("отл", result)
        model_mock.predict.assert_called_once_with("message123456789")


if __name__ == '__main__':
    unittest.main()
