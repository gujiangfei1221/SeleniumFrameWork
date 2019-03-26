# coding=utf-8
"""
Created on 2016-8-13
@author: Jennifer
Project:使用unittest框架编写测试用例。
"""
import time
import unittest
from ddt import ddt, data, unpack
from selenium import webdriver

from Pages.MainPage import MainPage
from Pages.RegisterPage import RegisterPage
import Utils.HTMLTestRunner as HTMLTestRunner
from Utils.GetData import get_excel_data


@ddt
class RegisterPageCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='Utils/chromedriver')
        self.url = "https://guxiaofengxltd.xyz:8084/xl_com_register.html"

    # 用例执行体
    @data(*get_excel_data('Data/testdata.xlsx'))
    @unpack
    def test_register(self,danweiname, province, city, area, email, username, phonenum, password1, password2):
        # 声明LoginPage类对象
        register_page = RegisterPage(self.driver, self.url)
        # 调用打开页面组件
        register_page.open()
        register_page.input_danweiname(danweiname)
        # register_page.select_province(int(province))
        # time.sleep(5)
        # register_page.select_city(int(city))
        # time.sleep(5)
        # register_page.select_area(int(area))
        # register_page.input_email(email)
        # register_page.input_username(username)
        # register_page.input_phonenum(phonenum)
        # register_page.input_password1(password1)
        # register_page.input_password2(password2)
        # register_page.click_registerbutton()
        # self.assertEqual(register_page.is_sussess(),"操作完成")

    def tearDown(self):
        self.driver.quit()

class MainPageCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='Utils/chromedriver')
        self.url = "https://guxiaofengxltd.xyz:8084/xl_groups.html?ck=aa0001&wx_openId=sjhfpjhdteidyeidkeidrejaqiiaweiaoeigpeibteiebfafbacfiageaaefgjgcf"


    def test_main(self):
        # 声明LoginPage类对象
        main_page = MainPage(self.driver, self.url)
        # 调用打开页面组件
        main_page.open()
        main_page.click_controller()
        time.sleep(5)


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    # suite = unittest.TestLoader().loadTestsFromTestCase(RegisterPageCase)
    suite = unittest.TestLoader().loadTestsFromTestCase(MainPageCase)

    file_path = "Report/result.html"
    file_result = open(file_path, 'wb')

    runner = HTMLTestRunner.HTMLTestRunner(stream=file_result, title=u"测试报告", description=u"用例执行情况")
    runner.run(suite)
    file_result.close()