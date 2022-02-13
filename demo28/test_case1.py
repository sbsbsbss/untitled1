# 1.导包
import unittest

# 2.导入模块
from controller import login

# 3.导入TestCase完成初始化和清空工作
class TestLongin(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("开始执行测试用例")
    @classmethod
    def tearDownClass(cls) -> None:
        print("结束执行测试用例")
    def setUp(self) -> None:
        print("执行初始化工作")
    def tearDown(self) -> None:
        print("执行清空工作")

# 4.测试用例并使用TestCase断言操作
    def test_login1(self):
        print("执行测试用例1")
        self.assertEqual("登录成功",login("admin","123456"))
    def test_login2(self):
        print("执行测试用例2")
        self.assertEqual("用户名不能为空",login(' ',"123456"))
    def test_login3(self):
        print("执行测试用例3")
        self.assertEqual("密码不能为空",login("admin",''))
# 5.导入TestSuite添加测试套件
# (创建一个名称suite，调用Testsuite。suite = nuittest.testsuite)
# suite = unittest.TestSuite()

# 添加单个测试套件
# suite.addTest(TestLongin('test_login2'))
# suite.addTest(TestLongin('test_login3'))

# 6.添加多个测试套件
# case_list = [TestLongin('test_login2'),TestLongin('test_login3')]
# suite.addTests(case_list)

# 7.导入TestTextRunner运行测试用例
# runner = unittest.TextTestRunner(verbosity=2)
# runner.run(suite)


















