import unittest


# 测试顺序,数字与字母的顺序为:0-9,A-Z,a-z

class TestBdd(unittest.TestCase):

    def setUp(self):
        print('test TestBdd ')

    def tearDown(self):
        print('test TestBdd end')

    def test_ccc(self):
        print('test ccc')

    def test_aaa(self):
        print('test aaa')


class TestAdd(unittest.TestCase):
    def setUp(self):
        print('test TestAdd ')

    def tearDown(self):
        print('test TestAdd end')

    def test_bbb(self):
        print('test bbb')


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestBdd('test_ccc'))
    suite.addTest(TestBdd('test_aaa'))
    suite.addTest(TestAdd('test_bbb'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
