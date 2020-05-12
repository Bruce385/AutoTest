# -*- coding: utf-8 -*-
# @Author  : Bruce.Chen
# @Time    : 2020/5/12 14:46
# @File    : Screen.py
# @Software: PyCharm

class Screen():

    def __init__(self, driver):
        self.driver = driver

    def get_screen_width(self):
        return self.driver.get_window_size()['width']

    def get_sreen_height(self):
        return self.driver.get_window_size()['height']
