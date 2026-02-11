import time
import logging
import image
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utils.utils import BaseClass


class TestLogin(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    def login_op(self, log):

        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
        time.sleep(3)

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='login-button']"))
        )
        element.click()
        log.info("Login : Success")
        # button = self.driver.find_element(By.XPATH, "//input[@id='login-button']")
        # button.click()


        select = Select(self.driver.find_element(By.XPATH,"//select[@class='product_sort_container']"))
        select.select_by_visible_text("Price (low to high)")
        time.sleep(1)
        buttons = self.driver.find_elements(By.XPATH,"//button[text()='Add to cart']")
        x = 1
        for button in buttons:
            if x <= 2:
                button.click()
                x = x + 1
                time.sleep(2)

            else:
                break
        time.sleep(2)
        time.sleep(1)

        get_url = self.driver.current_url
        str = "https://www.saucedemo.com/inventory.html"
        assert get_url == str
        time.sleep(2)
        self.driver.save_screenshot("../Screenshots/image.png")

#main method
    def login_Operation(self):
        log=self.getLogger()
        self.login_op(log)
