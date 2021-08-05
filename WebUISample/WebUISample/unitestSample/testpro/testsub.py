import unittest
from calculator import count


class TestAdd(unittest.TestCase):

    def setUp(self):
        print('test case start')

    def tearDown(self):
        print('test case end')

    def test_sub1(self):
        j = count(1, 4)
        self.assertEqual(j.sub(), -3)

    def test_sub2(self):
        j = count(8, 3)
        self.assertEqual(j.sub(), 5)


if __name__ == '__main__':
    unittest.main()
