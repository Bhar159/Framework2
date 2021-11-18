import pytest
from selenium import webdriver
from utilities.readProperties import ReadConfig
from utilities.customLog import LogGen
import time
from pageobject.DR_DesktopAddition import DRManageDesktop
from pageobject.DR_LoginPage import DR_Login
from pageobject.DR_Subscription import DRSubscription
from utilities import Xlutils
import random as r
import string

class Test_DR_User:
    url = ReadConfig.getDRurl()
    userID = ReadConfig.getdruserid()
    userPwd = ReadConfig.getdrpwd()

    def test_DrUserCreation001(self,SetUp):
        self.driver=SetUp
        self.driver.get(self.url)
        self.driver.maximize_window()
        loginPage=DR_Login(self.driver)
        customerPage=DRManageDesktop(self.driver)
        loginPage.setEmailId(self.userID)
        loginPage.setUserPwd(self.userPwd)
        loginPage.mspLoginbutton()
        time.sleep(5)
        subtest=DRSubscription(self.driver)
        subtest.drsubscriptionTab()
        subtest.drAddSubscriptionTab()
        subtest.sharedSubCheckBox()
        subtest.existingAccountLogout()
        subtest.azureSignInButton('admin@Performancetesting19.onmicrosoft.com','Anunta@12345')