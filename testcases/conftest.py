import time

import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_argument('ignore-certificate-errors')
options.add_argument("--no-sandbox")
options.add_argument("--guest")

@pytest.fixture(autouse=True)
def tc_setup(request):
    options.add_argument("--no-sandbox")
    options.add_argument("--guest")
    # options.add_argument("")
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    time.sleep(4)
    request.cls.driver = driver
    # yield
    print("logoff")
    print("close Browser")
