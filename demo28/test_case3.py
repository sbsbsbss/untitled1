# 1.导包
import unittest
from controller import login

# 2.导入模块
from parameterized import parameterized
# 3.导入类
class TastLogin(unittest.TestCase):

    @parameterized.expand([("登录成功","admin","123456"),("用户名不能为空"," ","123456"),("密码不能为空","admin"," ")])
    def test_login(self,expect,username,password):
        self.assertEqual(expect,login(username,password))




# # 4.测试用例并使用TestCase断言操作
#     def test_login1(self):
#         print("执行测试用例1")
#         self.assertEqual("登录成功",login("admin","123456"))
#     def test_login2(self):
#         print("执行测试用例2")
#         self.assertEqual("用户名不能为空",login(' ',"123456"))
#     def test_login3(self):
#         print("执行测试用例3")
#         self.assertEqual("密码不能为空",login("admin",''))
#
#















