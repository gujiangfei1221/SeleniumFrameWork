# coding=utf-8
'''
Created on 2016-8-13
@author: Jennifer
Project:页面基本操作方法：如open，input_username，input_password，click_submit
'''
import time

from selenium.webdriver.common.by import By
# 继承BasePage类
from Utils.BasePage import BasePage


class MainPage(BasePage):
    # 定位器，通过元素属性定位元素对象
    controller_loc = (By.XPATH,'//*[@id="id_group"]/div/a/div[1]')

    # 操作
    # 通过继承覆盖（Overriding）方法：如果子类和父类的方法名相同，优先用子类自己的方法。
    # 打开网页
    def open(self):
        # 调用page中的_open打开连接
        self._open(self.base_url)

    # 输入用户名：调用send_keys对象，输入用户名
    def click_controller(self):
        #        self.find_element(*self.username_loc).clear()
        self.find_element(*self.controller_loc).click()