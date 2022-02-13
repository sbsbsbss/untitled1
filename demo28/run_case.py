# 1.导包
import unittest
# 导入TestLoader
# 当前文件用'.'
# 2.创建套件
suite = unittest.TestLoader().discover('.',pattern='test*.py')
# 3.创建运行器
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)














