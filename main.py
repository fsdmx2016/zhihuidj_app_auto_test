import os
import unittest
import time
from unittestreport import TestRunner

# 获取到测试用例的路径
path = os.path.abspath(os.path.dirname(__file__)) + '/case'


def run_unittest_case():
    suite = unittest.defaultTestLoader.discover(path)
    now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    curPath = os.path.abspath(os.path.dirname(__file__))
    filename = curPath + "/reports/" + now + "_result.html"
    # 用例执行
    runner = TestRunner(suite,
                        filename=filename,
                        title="自动化测试报告",
                        report_dir=curPath + "/reports/",
                        templates=1,
                        desc="app自动化测试报告",
                        tester="系统定时触发"
                        )
    runner.run()



if __name__ == '__main__':
    run_unittest_case()
