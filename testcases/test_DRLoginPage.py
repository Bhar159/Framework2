import pytest
from selenium import webdriver
from pageobject.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLog import LogGen
import time
from pageobject.DR_LoginPage import DR_Login

class Test_DRHomePage:
    baseurl=ReadConfig.getDRurl()
    username=ReadConfig.getdruserid()
    password=ReadConfig.getdrpwd()
    upn=ReadConfig.getdrupn()

    def testMspAdminlogin_TC001(self,SetUp):
        self.driver=SetUp
        self.driver.get(self.baseurl)
        time.sleep(10)
        print(self.driver.title)
        login_pgobj=DR_Login(self.driver)
        login_pgobj.setEmailId(self.username)
        self.driver.get_screenshot_as_file("C:/Users/bhara/PycharmProjects/Framework/Screenshots/Verify_Username.png")
        login_pgobj.setUserPwd(self.password)
        self.driver.get_screenshot_as_file("C:/Users/bhara/PycharmProjects/Framework/Screenshots/Verify_Password.png")
        login_pgobj.mspLoginbutton()
        print("Testcase001_Completed successfully")


    def testUserLogin_TC002(self,SetUp):
        self.driver=SetUp
        self.driver.get(self.baseurl)
        userlogin= DR_Login(self.driver)
        userlogin.usertabChange()
        time.sleep(5)
        userlogin.userIdpage(self.upn)
        self.driver.get_screenshot_as_file("C:/Users/bhara/PycharmProjects/Framework/Screenshots/LoginPage.png")
        userlogin.userLoginbutton()
        time.sleep(10)

    def test_resetEmailID_TC003(self,SetUp):
        self.driver=SetUp
        resetFun=DR_Login(self.driver)
        self.driver.get(self.baseurl)
        resetFun.setforgetpwd("RR2@gmail.com")

    def test_wrongCred_TC004(self,SetUp):
        self.driver=SetUp
        credCheck=DR_Login(self.driver)
        self.driver.get(self.baseurl)
        time.sleep(5)
        credCheck.setEmailId("Q")
        credCheck.setUserPwd("123")
        credCheck.wrongCredAdmin()
        self.driver.get_screenshot_as_file("C:/Users/bhara/PycharmProjects/Framework/Screenshots/WrongCred.png")




