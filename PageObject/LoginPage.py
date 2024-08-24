from selenium.webdriver.common.by import By


class LoginPage:
    xpath_email="//input[@id='Email']"
    xpath_password="//input[@id='Password']"
    xpath_login="//button[@type='submit']"
    xpath_logout="//a[text()='Logout']"

    def __init__(self, driver):
        self.driver=driver

    def SetEmail(self,email):
        self.driver.find_element(By.XPATH, self.xpath_email).clear()
        self.driver.find_element(By.XPATH, self.xpath_email).send_keys(email)

    def SetPassword(self,pswd):
        self.driver.find_element(By.XPATH, self.xpath_password).clear()
        self.driver.find_element(By.XPATH, self.xpath_password).send_keys(pswd)

    def ClickLogin(self):
        self.driver.find_element(By.XPATH, self.xpath_login).click()

    def ClickLogout(self):
        self.driver.find_element(By.XPATH, self.xpath_logout).click()