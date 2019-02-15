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
	
        html = requests.get("http://www.baidu.com", timeout=5)# 网络连通性测试
		
    except (KeyboardInterrupt,SystemExit):
    # SystemExit 是由于当前 Python 应用程序需要退出
    # KeyboardInterupt 代表用户按下了 CTRL-C (^C) , 想要关闭 Python
    
        # user wangts to quit
        raise # reraise back to caller
            
    except Exception: 
	
        url = "网络登陆验证网址" # 如 https://10.108.255.12
        username = "网络账号" # 此处输入网络认证账号
        password = "密码"     # 此处输入网络认证密码
		
		# 关闭浏览器的信息提示，解决“Chrome正在收到自动测试软件的控制”遮蔽问题
        option = webdriver.ChromeOptions()
        option.add_argument('disable-infobars') 
        
        browser  = webdriver.Chrome(options=option)  #打开浏览器
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

        # 解决因网络连通性检测异常导致的非断网状态下登陆报错问题
        try:
        
            login_button.click()            # 点击登录
            
        except (KeyboardInterrupt,SystemExit):
        
            # user wangts to quit
            raise # reraise back to caller
            
        except Exception:
        
            print('非断网状态下异常登陆')
        
        # time.sleep(0.2)
        # print(browser.get_cookies())
        
        time.sleep(2)
        print(browser.title)
        
        browser.close()
        browser.quit()

    else:
        date_time = time.asctime( time.localtime(time.time()) );
        print("当前网络处于连通状态 " + date_time)
    time.sleep(300) # 每隔一段时间检测一次当前网络连通性，该时间间隔可根据需要修改

