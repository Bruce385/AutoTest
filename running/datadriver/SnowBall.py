# -*- coding: utf-8 -*-
# @Author  : Bruce.Chen
# @Time    : 2020/5/6 16:59
# @File    : SnowBall.py
# @Software: PyCharm
from time import sleep

import pytest
import yaml
from appium import webdriver
from config.ConnectConfig import *
from running.datadriver.DataDrive import TestCase
from utils.Screen import Screen


class TestSearch:

    def setup(self):
        self.driver = webdriver.Remote(AppiumServerUrl, VirtualConnection)
        self.width = Screen(self.driver).get_screen_width()
        self.height = Screen(self.driver).get_screen_height()
        # print("\n屏幕尺寸" + str(self.width) + "*" + str(self.height))
        self.driver.implicitly_wait(10)
        if len(self.driver.find_elements_by_xpath(
                "//*[contains(@text, '同意') and contains(@resource-id, 'tv_agree')]")) > 0:
            self.driver.find_element_by_xpath(
                "//*[contains(@text, '同意') and contains(@resource-id, 'tv_agree')]").click()

    # @pytest.mark.parametrize("keyword", [('阿里巴巴'), ('腾讯'), ('新浪')])
    @pytest.mark.parametrize("keyword", yaml.load(open('searchdata.yaml', 'r', encoding='utf-8')))
    def testsearch(self, keyword):
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

    def testcace(self):
        TestCase("testcase.yaml").run(self.driver)
