#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/27 15:40
# @Author  : bgzhou
import pytest
from appium import webdriver
import unittest

from appium.webdriver.common.touch_action import TouchAction


class TestXueQiu(unittest.TestCase):

    def setUp(self):
        setting = {
            'platformName': 'Android',
            'automationName': 'uiautomator2',
            'deviceName': 'Android Emulator',
            'appActivity': '.view.WelcomeActivityAlias',
            'autoGrantPermissions': True,
            'appPackage': 'com.xueqiu.android',
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', setting)
        self.driver.implicitly_wait(30)

    def loaded(self):
        list1 = ["x", "y"]
        while list1[-2] != list1[-1]:
            list1.append(self.driver.find_element_by_xpath
                         ("//*[contains(@resource-id, 'tab_name') and @text='自选']").location)

    def test_add_us(self):
        self.loaded()
        self.driver.find_element_by_xpath("//*[contains(@resource-id, 'tab_name') and @text='自选']").click()
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='美股']").click()
        self.driver.find_element_by_id("recommend_name_one").click()
        self.driver.find_element_by_id("//android.widget.ImageView[contains(@resource-id, 'floating_action_image_view_id')]/following::android.widget.TextView[@text='加自选']")
        try:
            self.driver.find_element_by_id("md_buttonDefaultNegative").click()
        except Exception as e:
            print(e)

    def test_delete_us(self):
        self.loaded()
        self.driver.find_element_by_xpath("//*[contains(@resource-id, 'indicator')]//*[@text='美股']").click()
        TouchAction(self.driver).long_press(self.driver.find_element_by_id("portfolio_whole_item")).perform()
        self.driver.find_element_by_xpath("//*[@text='删除']").clcik()
        assert 1 == len(self.driver.find_elements_by_id("recommend_name_one"))
        self.driver.find_element_by_xpath("//*[contains(@resource-id, 'indicator')]//*[@text='全部']").click()
        assert 1 == len(self.driver.find_elements_by_id("recommend_name_one"))


    @pytest.param()
    def test_add_batch(self):


    def tearDown(self):
        self.driver.quit()

