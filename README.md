
本程序仅适用于网页端网络认证。觉得好用请点下右上角Star收藏。
仅在Windows平台测试过，Linux或Mac平台应该也适用。
仅支持Python3版本，python的两种常见安装方法请访问如下网址：
https://www.jianshu.com/p/7cbed2b32e45

使用步骤：
1. 安装第三方依赖库
2. 下载浏览器驱动放在Python根目录（即python.exe所在目录）下
注：IE浏览器驱动可放在主程序所在目录下
3. 打开主程序“Auto_Login_XX_version_Main.py”，填写登录信息
4. 在python的命令行终端中运行 python ‘绝对路径’\Auto_Login_XX_version_Main.py.py
（‘绝对路径’中填入存放主程序的路径名，或直接把主程序拖入命令行终端）

依赖的第三方python库：time、requests和selenium。
若提示“No module named 'xxx'”，使用pip install xxx命令安装。

#=================================================================================
Google浏览器版本
需搭配谷歌浏览器和与谷歌浏览器版本相对应的浏览器驱动“chromedrive”使用。
这里提供了与浏览器71.0.3578.98版本对应的win32位71.0.3578.80版本浏览器驱动。

谷歌浏览器驱动下载网址 http://chromedriver.storage.googleapis.com/index.html。

谷歌浏览器驱动版本号与浏览器版本号最后两位可不同，
例如作者的浏览器版本号为71.0.3578.98，下载网址中71.0.3578.80版本号的驱动可兼容。
#==============================================================================

查看网络认证页面中“用户名框”、“密码框”和“登陆按钮”对应的id的方法：
在谷歌浏览器中打开网络认证页面，鼠标右键单击页面选择查看网页源代码，
或使用快捷键“Ctrl + U”，在网页源代码中找到“用户名/username”、“密码/password”和
“登录/submit”等类型/占位符/名称等对应的id。

例如 id="loginname"，id="password"，id="button"。

当然也可通过其他属性找到关键字，依据是网页中的各个功能对应的某些属性唯一。


参考
https://blog.csdn.net/CosmopolitanMe/article/details/79486477
https://www.cnblogs.com/klb561/p/8839141.html
https://blog.csdn.net/u014240905/article/details/82564356
https://www.cnblogs.com/masako/p/7403293.html
https://blog.csdn.net/wangzhaotongalex/article/details/49157043
