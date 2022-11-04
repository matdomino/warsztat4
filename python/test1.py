import unittest

from python1 import silnia

class TestStringMethods(unittest.TestCase):
    def test_testowy(self):
        self.assertEqual(silnia(3),6)

if __name__=='__main__':
    unittest.main()
