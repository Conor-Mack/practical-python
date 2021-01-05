import unittest
import stock

class TestStock(unittest.TestCase):
    s = stock.Stock('GOOG', 100, 490.1)

    def test_create(self):
        self.assertEqual(self.s.name, 'GOOG')
        self.assertEqual(self.s.shares, 100)
        self.assertEqual(self.s.price, 490.1)

    def test_cost(self):
        self.assertEqual(self.s.cost, 49010.0)

    def test_shares(self):
        with self.assertRaises(TypeError):
            self.s.shares = "yeo"


if __name__ == "__main__":
    unittest.main()