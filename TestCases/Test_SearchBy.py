import time

from PageObject.LoginPage import LoginPage
from PageObject.AddCustomer import AddCustomer
from PageObject.SearchBy import SearchBy
from Utilities.ReadConfig import ReadProperty
from Utilities.CustomLogger import logger
from Utilities.common_utilities import gen_random_string


class Test_Suite_AddingCustomer:
    ss = r"..\ScreenShots\\"
    log = logger()

    def test_search_by_email(self, launch_browser):
        driver = launch_browser
        self.log.info("TC5 Nop Commerce Application launched sucessfully")
        login_obj = LoginPage(driver)
        login_obj.SetEmail(ReadProperty.GetUsername())
        login_obj.SetPassword(ReadProperty.GetPassword())
        login_obj.ClickLogin()
        self.log.info("TC5 Nop Commerce Application Logged in sucessfully")
        ac = AddCustomer(driver)
        ac.NavigateCustomerPage()
        self.log.info("TC5 Nop Commerce Application navigated to customer page sucessfully")
        search_obj = SearchBy(driver)
        search_obj.Search_Email("james_pan@nopCommerce.com")
        search_obj.ClickSearch()
        time.sleep(4)
        list_of_email = search_obj.GetEmail()

        if len(list_of_email) == 1 and list_of_email[0] == "james_pan@nopCommerce.com":
            self.log.info("TC5 test_search_by_email == PASS")
            assert True
        else:
            self.log.error("TC5 test_search_by_email == FAIL")
            driver.save_screenshot(self.ss + "test_search_by_email.png")
            assert False

    def test_search_by_firstname(self, launch_browser):
        driver = launch_browser
        self.log.info("TC5 Nop Commerce Application launched sucessfully")
        login_obj = LoginPage(driver)
        login_obj.SetEmail(ReadProperty.GetUsername())
        login_obj.SetPassword(ReadProperty.GetPassword())
        login_obj.ClickLogin()
        self.log.info("TC5 Nop Commerce Application Logged in sucessfully")
        ac = AddCustomer(driver)
        ac.NavigateCustomerPage()
        self.log.info("TC5 Nop Commerce Application navigated to customer page sucessfully")
        search_obj = SearchBy(driver)
        search_obj.SearchByFirstName("John")
        search_obj.ClickSearch()
        time.sleep(4)
        list_of_name = search_obj.GetNames()
        self.log.info(list_of_name)  # ['john Bell', 'John Smith']
        for name in list_of_name:
            if "John".lower() in name.lower():
                continue
            else:
                self.log.error("TC5 test_search_by_firstname == FAIL")
                driver.save_screenshot(self.ss + "test_search_by_firstname.png")
                assert False
        self.log.info("TC5 test_search_by_firstname == PASS")
        assert True

    def test_search_by_lastname(self, launch_browser):
        driver = launch_browser
        self.log.info("TC6 Nop Commerce Application launched sucessfully")
        login_obj = LoginPage(driver)
        login_obj.SetEmail(ReadProperty.GetUsername())
        login_obj.SetPassword(ReadProperty.GetPassword())
        login_obj.ClickLogin()
        self.log.info("TC6 Nop Commerce Application Logged in sucessfully")
        ac = AddCustomer(driver)
        ac.NavigateCustomerPage()
        self.log.info("TC6 Nop Commerce Application navigated to customer page sucessfully")
        search_obj = SearchBy(driver)
        search_obj.SearchByLastName("Smith")
        search_obj.ClickSearch()
        time.sleep(4)
        list_of_name = search_obj.GetNames()
        self.log.info(list_of_name)  # ['john Bell', 'John Smith']
        status_list = []

        for name in list_of_name:
            if "Smith".lower() in name.lower():
                status_list.append(True)
            else:
                status_list.append(False)
        self.log.info(status_list)

        if False in status_list:
            self.log.error("TC6 test_search_by_lastname == FAIL")
            driver.save_screenshot(self.ss + "test_search_by_lastname.png")
            assert False
        else:
            self.log.info("TC6 test_search_by_lastname == PASS")
            assert True
