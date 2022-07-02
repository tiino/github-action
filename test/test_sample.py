import unittest
import requests
import os
import sys
import pathlib

filepath = pathlib.Path(os.path.abspath(__file__))
filedir = filepath.parent.parent
sys.path.append(str(filedir))


class TestSample(unittest.TestCase):

    def test_function_a(self):
        from src.sample import function_a
        a = 2
        b = 3

        exp = 5
        res = function_a(a, b)

        self.assertEqual(res, exp)

    def test_function_b(self):
        from src.sample import function_b
        a = 3
        b = 1

        exp = 2
        res = function_b(a, b)

        self.assertEqual(res, exp)

    def test_function_c(self):
        from src.sample import function_c
        a = 3
        b = 2

        exp = 6
        res = function_c(a, b)

        self.assertEqual(res, exp)

    def test_post(self):
        url = 'http://localhost:8787/sse'
        exp = {'val_1': 1, 'val_2': 2}

        response = requests.post(url, data='{"val_1": 1, "val_2": 2}')

        self.assertDictEqual(response.json(), exp)


if __name__ == '__main__':
    unittest.main()
