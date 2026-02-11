import time

import pytest
from selenium.webdriver.common.by import By

from Pages.loginpage import TestLogin
from Pages.AddtocartPage import Addtocart

@pytest.mark.usefixtures("tc_setup")
class Test:

    def test_swaglabs (self):
        tl=TestLogin(self.driver)
        tl.login_Operation()
        ac = Addtocart(self.driver)
        ac.add_operation()

