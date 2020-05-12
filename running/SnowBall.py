# -*- coding: utf-8 -*-
# @Author  : Bruce.Chen
# @Time    : 2020/5/6 16:59
# @File    : SnowBall.py
# @Software: PyCharm
from time import sleep

import pytest
from appium import webdriver
from config.ConnectConfig import *
from utils.Screen import Screen


class TestSearch:

    def setup(self):
        self.driver = webdriver.Remote(AppiumServerUrl, VirtualConnection)
        self.width = Screen(self.driver).get_screen_width()
        self.height = Screen(self.driver).get_sreen_height()
        # print("\n屏幕尺寸" + str(self.width) + "*" + str(self.height))

    @pytest.mark.parametrize("keyword", [('阿里巴巴'), ('腾讯'), ('新浪')])
    def testsearch(self, keyword):
        self.driver.implicitly_wait(10)
        if len(self.driver.find_elements_by_id("com.xueqiu.android:id/tv_agree")) >= 1:
            self.driver.find_element_by_id("com.xueqiu.android:id/tv_agree").click()

        sleep(3)
        el1 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        el1.click()
        el2 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        el2.send_keys(keyword)

        sleep(3)
        resultlist = self.driver.find_elements_by_id("com.xueqiu.android:id/name")
        print()
        for resultel in resultlist:
            print(resultel.text)
            # assert keyword in resultel.text

        condition = "//*[contains(@text, '{0}') and contains(@resource-id, 'name')]".format(keyword)
        el3 = self.driver.find_element_by_xpath(condition)
        el3.click()

        for i in range(0, 10):
            try:
                self.driver.swipe(self.width / 2, self.height * 4 / 5, self.width / 2, self.height / 5)
            except:
                pass

    # def teardown(self):
    #     print()
    #     print(self.driver.get_performance_data_types())
    #     for p in self.driver.get_performance_data_types():
    #         try:
    #             print(self.driver.get_performance_data('com.xueqiu.android', p, 20))
    #         except:
    #             pass

# driver.quit()
