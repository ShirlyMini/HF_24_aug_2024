from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddCustomer:
    xpath_main="//ul[@role='menu']/li/a/p[contains(text(), 'Customers')]"
    xpath_option="//ul[@role='menu']/li/a/p[contains(text(), 'Customers')]/parent::a/following-sibling::ul/li/a/p[contains(text(),'Customers')]"
    xpath_add_new_btn = "//a[@class='btn btn-primary']"
    xpath_email="//input[@id='Email']"
    xpath_password="//input[@id='Password']"
    xpath_first_name="//input[@id='FirstName']"
    xpath_last_name="//input[@id='LastName']"
    xpath_male_gender="//input[@id='Gender_Male']"
    xpath_female_gender="//input[@id='Gender_Female']"
    xpath_dob="//input[@id='DateOfBirth']"
    xpath_company="//input[@id='Company']"
    xpath_tax_exempt="//input[@id='IsTaxExempt']"
    xpath_newsletter="//select[@id='SelectedNewsletterSubscriptionStoreIds']"
    xpath_role="//select[@id='SelectedCustomerRoleIds']"
    xpath_vendor="//select[@id='VendorId']"
    xpath_active="//input[@id='Active']"
    xpath_admin_content="//textarea[@id='AdminComment']"
    xpath_save="//button[@name='save']"
    xpath_alert="//div[@class='alert alert-success alert-dismissable']"

    def __init__(self, driver):
        self.driver=driver

    def NavigateCustomerPage(self):
        sleep(3)
        self.driver.find_element(By.XPATH, self.xpath_main).click()
        sleep(3)
        self.driver.find_element(By.XPATH, self.xpath_option).click()

    def ClickAddNew(self):
        self.driver.find_element(By.XPATH, self.xpath_add_new_btn).click()

    def InputEmail(self, email):
        self.driver.find_element(By.XPATH, self.xpath_email).send_keys(email)

    def InputPassword(self, pswd):
        self.driver.find_element(By.XPATH, self.xpath_password).send_keys(pswd)

    def InputFirstName(self, name):
        self.driver.find_element(By.XPATH, self.xpath_first_name).send_keys(name)

    def InputLastName(self, name):
        self.driver.find_element(By.XPATH, self.xpath_last_name).send_keys(name)

    def SelectGender(self, gender):
        if gender.lower()=="male":
            self.driver.find_element(By.XPATH, self.xpath_male_gender).click()
        elif gender.lower()=="female":
            self.driver.find_element(By.XPATH, self.xpath_female_gender).click()

    def InputDOB(self, dob):
        self.driver.find_element(By.XPATH, self.xpath_dob).send_keys(dob)

    def InputCompany(self, company):
        self.driver.find_element(By.XPATH, self.xpath_company).send_keys(company)

    def SelectTaxExempt(self, tax):
        if tax.lower() == "yes":
            self.driver.find_element(By.XPATH, self.xpath_tax_exempt).click()

    def SelectNewsletter(self, newletter):
        drp_down = Select(self.driver.find_element(By.XPATH, self.xpath_newsletter))
        drp_down.select_by_visible_text(newletter)

    def SelectRole(self, role):
        drp_down = Select(self.driver.find_element(By.XPATH, self.xpath_role))
        drp_down.select_by_visible_text(role)

    def SelectVendor(self, vendor):
        drp_down = Select(self.driver.find_element(By.XPATH, self.xpath_vendor))
        drp_down.select_by_visible_text(vendor)

    def ClickActive(self, active):
        if self.driver.find_element(By.XPATH, self.xpath_active).is_selected():# it ll work only with input tag
            if active=="No":
                self.driver.find_element(By.XPATH, self.xpath_active).click()

    def InputAdminComment(self):
        self.driver.find_element(By.XPATH, self.xpath_admin_content).send_keys("this is admin comment")

    def ClickSave(self):
        self.driver.find_element(By.XPATH, self.xpath_save).click()

    def GetAlertText(self):
        return self.driver.find_element(By.XPATH, self.xpath_alert).text