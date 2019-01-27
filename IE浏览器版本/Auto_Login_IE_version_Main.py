# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 22:31:33 2019

@author: xia
"""

import time
import requests
from selenium import webdriver

while 1:

    try:
	
        html = requests.get("http://www.baidu.com",timeout=2)# 网络连通性测试
		
    except:
	
        url = "网络登陆验证网址" # 如 https://10.108.255.12
        username = "网络账号" # 此处输入网络认证账号
        password = "密码"     # 此处输入网络认证密码
		
        browser = webdriver.Ie()   #调用IE浏览器
        #browser.minimize_window()  # 最小化浏览器
        
        browser.get(url)
        browser.implicitly_wait(10) 
		# 等待网页加载完毕（隐式等待），避免因网页未加载完成查找不到所需元素出现异常
		
        name_input = browser.find_element_by_id("loginname")  # 找到用户名的id
        pass_input = browser.find_element_by_id("password")  # 找到输入密码的id
        login_button = browser.find_element_by_id("button")  # 找到登录按钮的id
        
        #name_input.clear()              # 清空用户名框中的已有信息 
        name_input.send_keys(username)  # 填入用户名
        time.sleep(0.2)
        #pass_input.clear()              # 清空密码框中的已有信息
        pass_input.send_keys(password)  # 填入密码
        time.sleep(0.2)
        login_button.click()            # 点击登录
        
        # time.sleep(0.2)
        # print(browser.get_cookies())
        
        time.sleep(2)
        print(browser.title)
        
        browser.close()

    else:
        date_time = time.asctime( time.localtime(time.time()) );
        print("当前网络处于连通状态 " + date_time)
    time.sleep(300) # 每隔一段时间检测一次当前网络连通性，该时间间隔可根据需要修改
