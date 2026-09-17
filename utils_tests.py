import unittest
from utils import utils


class TestUtils(unittest.TestCase):

    def setUp(self):
        self.util = utils()

    def test_reversed_integer(self):
        self.assertEqual(self.util.reversed(1234), 4321)

    def test_reversed_string(self):
        with self.assertRaises(TypeError):
            self.util.reversed("1234")

    def test_reversed_float(self):
        with self.assertRaises(TypeError):
            self.util.reversed(12.34)

    def test_formatter_integer(self):
        self.assertEqual(
            self.util.formatter(10),
            ("0b1010", "0o12")
        )

    def test_formatter_string(self):
        with self.assertRaises(TypeError):
            self.util.formatter("10")

    def test_formatter_float(self):
        with self.assertRaises(TypeError):
            self.util.formatter(10.5)


if __name__ == "__main__":
    unittest.main()