# -*- coding: utf-8 -*-
# @Author  : Bruce.Chen
# @Time    : 2020/4/4 14:57
# @File    : RunSome.py
# @Software: PyCharm
# coding:utf-8
import os

# popen返回文件对象，跟open操作一样
with os.popen(r'adb devices', 'r') as f:
    text = f.read()
print(text)  # 打印cmd输出结果

# 输出结果字符串处理
s = text.split("\n")  # 切割换行
result = [x for x in s if x != '']  # 列生成式去掉空
print(result)

# 可能有多个手机设备
devices = []  # 获取设备名称
for i in result:
    dev = i.split("\tdevice")
    if len(dev) >= 2:
        devices.append(dev[0])

if not devices:
    print('当前设备未连接上')
else:
    print('当前连接设备：%s' % devices)
