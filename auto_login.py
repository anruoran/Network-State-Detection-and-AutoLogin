# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 20:40:17 2019

@author: xia
"""

import time
import requests
from selenium import webdriver
while 1:
    try:
        html = requests.get("http://www.baidu.com",timeout=2)
    except:
        username = "网络账号"
        password = "密码"
        option = webdriver.ChromeOptions()
        option.add_argument('disable-infobars')
        
        browser  = webdriver.Chrome(options=option)  #打开浏览器
        #browser.maximize_window()  # 最大化浏览器  
        url = "网络登陆验证网址" # 如 https://10.108.255.12
        browser.get(url)
        browser.implicitly_wait(10)
        name_input = browser.find_element_by_id("loginname")  # 找到用户名的id
        pass_input = browser.find_element_by_id("password")  # 找到输入密码的id
        login_button = browser.find_element_by_id("button")  # 找到登录按钮的id
        
        #name_input.clear()
        name_input.send_keys(username)  # 填写用户名
        time.sleep(0.2)
        #pass_input.clear()
        pass_input.send_keys(password)  # 填写密码
        time.sleep(0.2)
        login_button.click()            # 点击登录
        
        time.sleep(0.2)
        print(browser.get_cookies())
        
        time.sleep(2)
        print(browser.title)
        
        browser.close()
    else:
        print("当前网络处于连通状态")
	time.sleep(300) # 每隔5分钟ping一次网络，检测网络连通性

