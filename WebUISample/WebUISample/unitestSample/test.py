from WebUISample.WebUISample.unitestSample.testpro.calculator import count
import unittest
class MyTest(unittest.TestCase):
    def setUp(self):
        print('test case start')
    def tearDown(self):
        print('test case end')

class TestAdd(MyTest):

    def test_add1(self):
        j = count(1, 4)
        self.assertEqual(j.add(), 5)

    def test_add2(self):
        j = count(3, 8)
        self.assertEqual(j.add(), 11)


class TestSub(MyTest):

    def test_sub1(self):
        j = count(1, 4)
        self.assertEqual(j.sub(), -3)

    def test_sub2(self):
        j = count(8, 3)
        self.assertEqual(j.sub(), 5)




if __name__ == '__main__':
    # 构造测试集
    # suite = unittest.TestSuite()
    # suite.addTest(TestAdd('test_add1'))
    # suite.addTest(TestAdd('test_add2'))
    # suite.addTest(TestSub('test_sub1'))
    # suite.addTest(TestSub('test_sub2'))
    #
    # # 执行测试
    # runner = unittest.TextTestRunner()
    # runner.run(suite)

  unittest.main()
