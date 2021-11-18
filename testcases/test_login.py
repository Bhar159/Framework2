import pytest
from selenium import webdriver
from pageobject.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLog import LogGen

class Test_001_Login:
    baseUrl=ReadConfig.getApplicationUrl()
    username=ReadConfig.getUsername()
    password=ReadConfig.getPassword()

    log_generator=LogGen.log()

    def test_homePageTitle(self,SetUp):
        self.log_generator.info("******************test_homePageTitle*************************")
        self.log_generator.info("******************Started*************************")
        self.driver=SetUp
        self.driver.get(self.baseUrl)
        act_title=self.driver.title
        #self.driver.close()
        if act_title=="Your store. Login":
            assert True
            self.driver.close()
            self.log_generator.info("******************Pass_test_homePageTitle*********************************")
        else:
            self.driver.save_screenshot("C:/Users/bhara/PycharmProjects/Framework/Screenshots/test_homePageTitle.png")
            self.driver.close()
            self.log_generator.info("******************Failed_test_homePageTitle*********************************")
            assert False

    def test_login(self,SetUp):
        self.log_generator.info("******************test_login_testcase_002*********************************")
        self.log_generator.info("//Started///")
        self.driver=SetUp
        self.driver.get(self.baseUrl)
        self.ip=LoginPage(self.driver)
        self.ip.setUserName(self.username)
        self.ip.setPassWord(self.password)
        self.ip.clickLogin()
        act_title2=self.driver.title
        #self.driver.close()
        if act_title2=="Dashboard / nopCommerce administration":
            self.driver.close()
            assert True
            self.log_generator.info("******************Pass_test_login*********************************")
        else:
            self.driver.save_screenshot("C:/Users/bhara/PycharmProjects/Framework/Screenshots/test_login.png")
            self.driver.close()
            self.log_generator.info("******///failed////************")
            assert False

