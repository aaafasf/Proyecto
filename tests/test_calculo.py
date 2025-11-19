import unittest
from app.calculo import suma

class TestCalculo(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(5, 7), 12)
