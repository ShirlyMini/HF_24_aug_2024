import time

import pytest

from PageObject.LoginPage import LoginPage
from Utilities.ReadConfig import ReadProperty
from Utilities.CustomLogger import logger
from TestData.Load_Login_Data import Load_data

class Test_Suite_Login_DDT:
    ss=r"..\ScreenShots\\"
    log = logger()

    @pytest.mark.parametrize("user, pswd, expect", Load_data("../TestData/LoginData.xlsx", "Sheet1"))
    def test_verify_Login_DDT(self, launch_browser, user, pswd, expect):
        driver = launch_browser
        #print(user, pswd, expect)
        self.log.info("TC3 Nop Commerce Application launched sucessfully")

        login_obj = LoginPage(driver)
        login_obj.SetEmail(user)
        login_obj.SetPassword(pswd)
        login_obj.ClickLogin()

        self.log.info("TC3 Nop Commerce Application Logged in sucessfully")
        if driver.title=="Dashboard / nopCommerce administration" and expect=='Pass':
            self.log.info(f"TC3 test_verify_DashBoardPage for {user} {pswd} {expect} == PASS")
            time.sleep(5)
            login_obj.ClickLogout()
            assert True
        elif driver.title != "Dashboard / nopCommerce administration" and expect == 'Fail':
            self.log.info(f"TC3 test_verify_DashBoardPage for {user} {pswd} {expect} == PASS")
            assert True
        else:
            self.log.error(f"TC3 test_verify_DashBoardPage for {user} {pswd} {expect} == FAIL")
            driver.save_screenshot(self.ss+"test_verify_Login_DDT.png")
            assert False
