import time

from PageObject.LoginPage import LoginPage
from PageObject.AddCustomer import AddCustomer
from Utilities.ReadConfig import ReadProperty
from Utilities.CustomLogger import logger
from Utilities.common_utilities import gen_random_string

class Test_Suite_AddingCustomer:
    ss=r"..\ScreenShots\\"
    log = logger()
    def test_verify_alert_after_adding_customer(self, launch_browser):
        driver = launch_browser
        self.log.info("TC4 Nop Commerce Application launched sucessfully")
        login_obj = LoginPage(driver)
        login_obj.SetEmail(ReadProperty.GetUsername())
        login_obj.SetPassword(ReadProperty.GetPassword())
        login_obj.ClickLogin()
        self.log.info("TC4 Nop Commerce Application Logged in sucessfully")
        ac = AddCustomer(driver)
        ac.NavigateCustomerPage()
        ac.ClickAddNew()
        random_string = gen_random_string()
        ac.InputEmail(random_string+"@gmail.com")
        ac.InputPassword("abcd123")
        ac.InputFirstName("John")
        ac.InputLastName("Scott")
        ac.SelectGender("Male")
        ac.InputDOB("12-03-1999")
        ac.InputCompany("xyz company")
        ac.SelectTaxExempt("yes")
        ac.SelectNewsletter("Your store name")
        ac.SelectRole("Vendors")
        ac.SelectVendor("Vendor 1")
        ac.ClickActive("Yes")
        ac.InputAdminComment()
        ac.ClickSave()
        self.log.info("TC4 Nop Customer Application User added successfully")
        time.sleep(10)
        txt=ac.GetAlertText()
        if "The new customer has been added successfully." in txt:
            self.log.info("TC4 test_verify_alert_after_adding_customer == PASS")
            assert True
        else:
            self.log.error("TC4 test_verify_alert_after_adding_customer == FAIL")
            driver.save_screenshot(self.ss+"test_verify_alert_after_adding_customer.png")
            assert False