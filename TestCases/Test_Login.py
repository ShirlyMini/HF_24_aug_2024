import time

from PageObject.LoginPage import LoginPage
from Utilities.ReadConfig import ReadProperty
from Utilities.CustomLogger import logger

class Test_Suite_Login:
    ss=r"..\ScreenShots\\"
    log = logger()
    def test_verify_LoginPage(self, launch_browser):
        driver = launch_browser
        self.log.info("TC1 Nop Commerce Application launched sucessfully")
        if driver.title=="Your store. Login":
            self.log.info("TC1 test_verify_LoginPage == PASS")
            assert True
        else:
            self.log.error("TC1 test_verify_LoginPage == FAIL")
            driver.save_screenshot(self.ss+"test_verify_LoginPage.png")
            assert False
            


    def test_verify_DashBoardPage(self, launch_browser):
        driver = launch_browser
        self.log.info("TC2 Nop Commerce Application launched sucessfully")
        login_obj = LoginPage(driver)
        login_obj.SetEmail(ReadProperty.GetUsername())
        login_obj.SetPassword(ReadProperty.GetPassword())
        login_obj.ClickLogin()
        self.log.info("TC2 Nop Commerce Application Logged in sucessfully")
        if driver.title=="Dashboard / nopCommerce administration":
            self.log.info("TC2 test_verify_DashBoardPage == PASS")
            time.sleep(5)
            login_obj.ClickLogout()
            assert True
        else:
            self.log.error("TC2 test_verify_DashBoardPage == FAIL")
            driver.save_screenshot(self.ss+"test_verify_DashBoardPage.png")
            assert False
