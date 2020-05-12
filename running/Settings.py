# -*- coding: utf-8 -*-
# @Author  : Bruce.Chen
# @Time    : 2020/5/12 14:59
# @File    : Settings.py
# @Software: PyCharm
from time import sleep
from appium import webdriver
from config.ConnectConfig import AppiumServerUrl
from utils.Screen import Screen


class TestSettings:

    def setup(self):
        caps = {
            "platformName": "Android",
            "platformVersion": "7.1.1",
            "deviceName": "emulator-5554",
            "appPackage": "com.android.settings",
            "appActivity": "com.android.settings.Settings",
            "unicodeKeyboard": True,
            "resetKeyborad": True,
        }
        self.driver = webdriver.Remote(AppiumServerUrl, caps)

    def test_set_time_mode(self):
        self.search_element_by_swipe("//*[@text='日期和时间' and contains(@resource-id, 'title')]").click()
        sleep(3)
        summary_list = self.driver.find_elements_by_id("android:id/summary")
        print()
        print(summary_list[-1].get_attribute("text"))
        self.driver.find_element_by_xpath("//*[@text='使用 24 小时制' and contains(@resource-id, 'title')]").click()
        print(summary_list[-1].get_attribute("text"))

    def test_application_storage(self):
        self.search_element_by_swipe("//*[@text='应用' and contains(@resource-id, 'title')]").click()
        sleep(3)
        self.search_element_by_swipe("//*[@text='雪球股票' and contains(@resource-id, 'title')]").click()
        summary_list = self.driver.find_elements_by_id("android:id/summary")
        for summary in summary_list:
            print(summary.get_attribute("text"))

    def test_add_account(self):
        self.search_element_by_swipe("//*[@text='帐号' and contains(@resource-id, 'title')]").click()
        sleep(3)
        self.driver.find_element_by_id("android:id/title").click()
        sleep(3)
        account_list = self.driver.find_elements_by_id("android:id/title")
        print()
        for account in account_list:
            print(account.get_attribute("text"))

    def search_element_by_swipe(self, condition):
        while True:
            Screen(self.driver).screen_swipe()
            if len(self.driver.find_elements_by_xpath(condition)) > 0:
                return self.driver.find_element_by_xpath(condition)

    def teardown(self):
        self.driver.quit()
