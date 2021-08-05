import  unittest
import testadd
import testsub
suit=unittest.TestSuite()
suit.addTest(testadd.TestAdd('test_add1'))
suit.addTest(testadd.TestAdd('test_add2'))
suit.addTest(testsub.TestAdd('test_sub1'))
suit.addTest(testsub.TestAdd('test_sub2'))
if __name__=='__main__':
    runner=unittest.TextTestRunner()
    runner.run(suit)