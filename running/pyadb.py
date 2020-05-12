# -*- coding: utf-8 -*-
# @Author  : Bruce.Chen
# @Time    : 2020/5/11 10:32
# @File    : pyadb.py
# @Software: PyCharm

import os
import time

# from mobileDetecting import get_serialno

package_name = "com.xueqiu.android"

# get mobile sn
# phone_sn = get_serialno()
phone_sn = "emulator-5554"
info = []


# 统计pss值（实际使用的物理内存（比例分配共享库占用的内存）
def mem_info(phone_sn, apk_package_name):
    try:
        meminfo = os.popen(
            "adb -s {0} shell dumpsys meminfo {1} | findstr TOTAL".format(phone_sn, apk_package_name)).read()
        pss = meminfo.split()[1]
    except IndexError:
        pss = ""
    return pss


# 获取内存pss值，并写入到文件
with open("mem.txt", 'w+') as m:
    for i in range(10):
        pss_value = mem_info(phone_sn, package_name)
        time.sleep(2)
        m.write(pss_value + "\n")
