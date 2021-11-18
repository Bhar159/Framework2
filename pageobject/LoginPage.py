from selenium import webdriver

class LoginPage:

    textbox_username_xpath="//input[@id='Email']"
    textbox_passowrd_xpath="//input[@id='Password']"
    button_login_xpath="//button[contains(text(),'Log in')]"
    button_logout_linktext="Logout"


    def __init__(self,driver):
        self.driver=driver

    def setUserName(self,username):
        self.driver.find_element_by_xpath(self.textbox_username_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_username_xpath).send_keys(username)

    def setPassWord(self,password):
        self.driver.find_element_by_xpath(self.textbox_passowrd_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_passowrd_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()
    def clickLogout(self):
        self.driver.find_element_by_link_text(self.button_logout_linktext).click()
