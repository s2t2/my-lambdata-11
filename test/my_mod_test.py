import unittest

from my_lambdata.my_mod import enlarge

class MyModTest(unittest.TestCase):

    def test_enlarge(self):
        self.assertEqual(enlarge(4), 400)

if __name__ == '__main__':
    unittest.main()
