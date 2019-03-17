import unittest


def sum(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


# 断言了解一下，测试的时候会使用到
# 编写测试类，父类是unittest.TestCase
class MyTest(unittest.TestCase):
    # 测试之前的准备工作
    def setUp(self):
        print("测试之前的数据初始化......")

    # 测试之后的收尾工作
    def tearDown(self):
        print("测试之后的收尾工作......")

    def testSum_1(self):
        self.assertAlmostEqual(sum(2, 3), 5, "Test sun fail")

    def testSum_2(self):
        self.assertAlmostEqual(sum(2, 3), 5, "Test sun fail")

    def testSum_3(self):
        self.assertAlmostEqual(sum(2, 3), 7, "Test sun fail")


if __name__ == "__main__":
    unittest.main()
