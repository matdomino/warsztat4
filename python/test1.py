import unittest

class Testing(unittest.TestCase):
    def test_testowy(self):
        a = 10
        b = 10
        self.assertNotEqual(a, b)

if __name__=='__main__':
    unittest.main()
