import unittest


class Test(unittest.TestCase):
    def setUp(self):
        number = input("Enter a number:")
        self.number = int(number)

    def tearDown(self):
        print('pass')

    def test_case(self):
        self.assertEqual(self.number, 10, msg="your input is not 10!")


if __name__ == '__main__':
    unittest.main()
