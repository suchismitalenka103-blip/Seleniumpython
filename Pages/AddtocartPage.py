import time

import pytest
from selenium.webdriver.common.by import By

from Utils.utils import BaseClass


class Addtocart(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    def add_op(self,log):
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
        time.sleep(2)
        log.info("Items added to cart successfully")

        # self.driver.find_element(By.XPATH, "//button[@id='continue-shopping']").click()
        # time.sleep(2)
        # self.driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']").click()
        # time.sleep(5)
        # self.driver.find_element(By.XPATH, "//a[@id='logout_sidebar_link']").click()
        # time.sleep(10)
        self.driver.find_element(By.XPATH,"//button[@id='remove-sauce-labs-bike-light']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//button[@id='remove-sauce-labs-onesie']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[@id='checkout']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@id='first-name']").send_keys("Suchismita")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@id='last-name']").send_keys("Lenka")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@id='postal-code']").send_keys("754029")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@id='continue']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//button[@id='finish']").click()
        time.sleep(2)
        get_url = self.driver.current_url
        str = "https://www.saucedemo.com/checkout-complete.html"
        assert get_url == str
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//button[@id='back-to-products']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//a[@id='logout_sidebar_link']").click()
        time.sleep(2)

    def add_operation(self):
        log=self.getLogger()
        self.add_op(log)
