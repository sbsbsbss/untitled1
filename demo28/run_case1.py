# 1.导包
import unittest
from HTMLTestRunner import HTMLTestRunner

# 2.创建套件
suite = unittest.TestLoader().discover('.',pattern='test*.py')
# 生成文件
report_path = 'test_report.html'
with open(report_path,'wb') as f:
    runner = HTMLTestRunner(f,title='测试报告',description='v1.0')
    runner.run(suite)














