# -*- coding: utf-8 -*-
# @Author  : Bruce.Chen
# @Time    : 2020/5/12 22:58
# @File    : DataDrive.py
# @Software: PyCharm
import yaml
from appium.webdriver.webdriver import WebDriver

from utils.Screen import Screen


class TestCase:

    def __init__(self, path):
        file = open(path, 'r', encoding='utf-8')
        self.steps = yaml.load(file)

    def run(self, driver: WebDriver):
        for step in self.steps:
            element = None
            elements = None
            # print(step)
            if isinstance(step, dict):
                if "id" in step.keys():
                    element = driver.find_element_by_id(step["id"])
                elif "xpath" in step.keys():
                    element = driver.find_element_by_xpath(step["xpath"])
                elif "ids" in step.keys():
                    elements = driver.find_elements_by_id(step["ids"])
                else:
                    print(step.keys())
                if "input" in step.keys():
                    element.send_keys(step["input"])
                elif "get" in step.keys():
                    print(element.get_attribute(step["get"]))
                elif "click" in step.keys():
                    element.click()
                elif "loopPrint" in step.keys():
                    for ele in elements:
                        print(ele.get_attribute(step["loopPrint"]))
                else:
                    print(step.keys())
                if "swipe" in step.keys():
                    for i in range(0, step["swipe"]):
                        Screen(driver).screen_swipe()
