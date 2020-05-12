# -*- coding: utf-8 -*-
# @Author  : Bruce.Chen
# @Time    : 2020/5/10 21:24
# @File    : testAPI.py
# @Software: PyCharm


from appium import webdriver
from appium.webdriver.extensions.android.gsm import GsmCallActions

from config.ConnectConfig import *


class TestAPI:

    def setup(self):
        self.driver = webdriver.Remote(AppiumServerUrl, VirtualConnection)

    def testCall(self):
        # self.driver.send_sms("10000", GsmCallActions.CALL)
        print(self.driver.get_performance_data_types())
        for p in self.driver.get_performance_data_types():
            try:
                print(self.driver.get_performance_data('com.xueqiu.android', p, 120))
            except:
                pass
