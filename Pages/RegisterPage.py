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


class RegisterPage(BasePage):
    # 定位器，通过元素属性定位元素对象
    danweiname_loc = (By.ID, 'id_com_name')
    # province_loc = (By.XPATH, '//*[@id="id_page_context"]/div[10]/div/div/div')
    # province2_loc_value = '//*[@id="id_page_context"]/div[10]/div/div/div/dl/dd['
    # city_loc = (By.XPATH, '//*[@id="id_city"]/div/div/div/div')
    # city2_loc_value = '//*[@id="id_city"]/div/div/div/div/dl/dd['
    # area_loc = (By.XPATH, '//*[@id="id_area"]/div/div/div/div')
    # area2_loc_value = '//*[@id="id_area"]/div/div/div/div/dl/dd['
    # email_loc = (By.ID, "id_com_email")
    # username_loc = (By.ID, "id_leader_name")
    # phonenum_loc = (By.ID, "id_leader_phone")
    # password1_loc = (By.ID, "id_leader_psd")
    # password2_loc = (By.ID, "id_leader_psd2")
    # registerbutton_loc = (By.ID,'id_register_submit')
    # assert_loc = (By.XPATH,'//*[@id="id_page_context"]/div[1]/label')

    # 操作
    # 通过继承覆盖（Overriding）方法：如果子类和父类的方法名相同，优先用子类自己的方法。
    # 打开网页
    def open(self):
        # 调用page中的_open打开连接
        self._open(self.base_url)

    # 输入用户名：调用send_keys对象，输入用户名
    def input_danweiname(self, danweiname):
        #        self.find_element(*self.username_loc).clear()
        self.find_element(*self.danweiname_loc).send_keys(str(danweiname))

    # def select_province(self, province):
    #     #        self.find_element(*self.username_loc).clear()
    #     self.find_element(*self.province_loc).click()
    #     self.find_element(*(By.XPATH, self.province2_loc_value+str(province)+']')).click()
    #
    # def select_city(self, city):
    #     #        self.find_element(*self.username_loc).clear()
    #     self.find_element(*self.city_loc).click()
    #     self.find_element(*(By.XPATH, self.city2_loc_value+str(city)+']')).click()
    #
    # def select_area(self, area):
    #     #        self.find_element(*self.username_loc).clear()
    #     self.find_element(*self.area_loc).click()
    #     self.find_element(*(By.XPATH, self.area2_loc_value+str(area)+']')).click()
    #
    # def input_email(self, email):
    #     #        self.find_element(*self.username_loc).clear()
    #     self.find_element(*self.email_loc).send_keys(str(email))
    #
    # def input_username(self, username):
    #     #        self.find_element(*self.username_loc).clear()
    #     self.find_element(*self.username_loc).send_keys(str(username))
    #
    # def input_phonenum(self, phonenum):
    #     #        self.find_element(*self.username_loc).clear()
    #     self.find_element(*self.phonenum_loc).send_keys(str(phonenum))
    #
    # def input_password1(self, password1):
    #     #        self.find_element(*self.username_loc).clear()
    #     self.find_element(*self.password1_loc).send_keys(str(password1))
    #
    # def input_password2(self, password2):
    #     #        self.find_element(*self.username_loc).clear()
    #     self.find_element(*self.password2_loc).send_keys(str(password2))
    #
    # def click_registerbutton(self):
    #     #        self.find_element(*self.username_loc).clear()
    #     self.find_element(*self.registerbutton_loc).click()
    #
    # def is_sussess(self):
    #     actualval = self.find_element(*self.assert_loc).text
    #     return actualval

    # # 用户名或密码不合理是Tip框内容展示
    # def show_span(self):
    #     return self.find_element(*self.span_loc).text
    #
    # # 切换登录模式为动态密码登录（IE下有效）
    # def swich_DynPw(self):
    #     self.find_element(*self.dynpw_loc).click()
    #
    # # 登录成功页面中的用户ID查找
    # def show_userid(self):
    #     return self.find_element(*self.userid_loc).text