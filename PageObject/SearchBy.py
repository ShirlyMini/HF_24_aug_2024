from selenium.webdriver.common.by import By


class SearchBy:
    xpath_email_field="//input[@id='SearchEmail']"
    xpath_first_name_field="//input[@id='SearchFirstName']"
    xpath_last_name_field="//input[@id='SearchLastName']"
    xpath_search_btn="//button[@id='search-customers']"
    xpath_email_column="//table[@id='customers-grid']/tbody/tr/td[2]"
    xpath_name_column="//table[@id='customers-grid']/tbody/tr/td[3]"

    def __init__(self, driver):
        self.driver=driver


    def Search_Email(self, email):
        self.driver.find_element(By.XPATH, self.xpath_email_field).send_keys(email)

    def SearchByFirstName(self, name):
        self.driver.find_element(By.XPATH, self.xpath_first_name_field).send_keys(name)

    def SearchByLastName(self, name):
        self.driver.find_element(By.XPATH, self.xpath_last_name_field).send_keys(name)

    def ClickSearch(self):
        self.driver.find_element(By.XPATH, self.xpath_search_btn).click()

    def GetEmail(self):
        elem = self.driver.find_elements(By.XPATH, self.xpath_email_column)
        list_email = []
        for ele in elem:
            list_email.append(ele.text)
        return list_email

    def GetNames(self):
        elem = self.driver.find_elements(By.XPATH, self.xpath_name_column)
        list_name = []
        for ele in elem:
            list_name.append(ele.text)
        return list_name