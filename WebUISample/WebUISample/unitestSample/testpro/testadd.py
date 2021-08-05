import unittest
from calculator import count


class TestAdd(unittest.TestCase):

    def setUp(self):
        print('test case start')

    def tearDown(self):
        print('test case end')

    def test_add1(self):
        j = count(1, 4)
        self.assertEqual(j.add(), 5)

    def test_add2(self):
        j = count(3, 8)
        self.assertEqual(j.add(), 11)


if __name__ == '__main__':
    unittest.main()
