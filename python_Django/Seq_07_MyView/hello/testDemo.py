import unittest


def division(x, y):
    return round(float(x) / y, 6)


class TestDivision(unittest.TestCase):
    def test1(self):
        self.assertEqual(division(9, 3), 3)

    def test1(self):
        self.assertEqual(division(9, 4), 2.25)

    def test1(self):
        self.assertEqual(division(4.2, 3), 1.4)


if __name__ == "__main__":
    unittest.main()
