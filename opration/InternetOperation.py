# /usr/bin/env python
# -*- coding: utf-8 -*-
from appium.webdriver.connectiontype import ConnectionType


class InternetOperation():
    # WIFI: ConnectionType.WIFI_ONLY
    # 数据流量: ConnectionType.DATA_ONLY
    # 飞行模式: ConnectionType.AIRPLANE_MODE
    # 无网络模式: ConnectionType.NO_CONNECTION
    # 全部都打开: ConnectionType.ALL_NETWORK_ON

    def __init__(self, driver):
        self.driver = driver

    def getwebstate(self):
        '''
        获取当前网络的状态
        :return:
        '''
        info = {0: "NO_CONNECTION（没网络）",
                1: "AIRPLANE_MODE（飞行模式）",
                2: "WIFI_ONLY（仅wifi）",
                4: "DATA_ONLY（仅数据）",
                6: "ALL_NETWORK_ON（所有网络都打开）"}
        state = self.driver.network_connection
        return info.get(state)

    def no_connection(self):
        # 关闭所有网络
        self.driver.set_network_connection(ConnectionType.NO_CONNECTION)
        print(self.getwebstate())

    def airplane_mode(self):
        # 飞行模式
        self.driver.set_network_connection(ConnectionType.AIRPLANE_MODE)
        print(self.getwebstate())

    def wifi(self):
        # 仅wifi
        # 设置 网络
        self.driver.set_network_connection(ConnectionType.WIFI_ONLY)
        print(self.getwebstate())

    def only(self):
        # 仅数据数据
        self.driver.set_network_connection(ConnectionType.DATA_ONLY)
        print(self.getwebstate())

    def all_networe_on(self):
        # 所有网络都打开
        self.driver.set_network_connection(ConnectionType.ALL_NETWORK_ON)
        print(self.getwebstate())
