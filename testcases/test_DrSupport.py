import pytest
from selenium import webdriver
from pageobject.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLog import LogGen
import time
from pageobject.DR_Support import DRSupport
from pageobject.DR_LoginPage import DR_Login

class Test_DrSupport_Func:
    baseUrl=ReadConfig.getDRurl()
    userID = ReadConfig.getdruserid()
    password=ReadConfig.getdrpwd()

    def test_loginPage_Tc001(self,SetUp):
        self.driver=SetUp
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        print(self.driver.title)
        loginPage=DR_Login(self.driver)
        loginPage.setEmailId(self.userID)
        loginPage.setUserPwd(self.password)
        loginPage.mspLoginbutton()
        time.sleep(5)
        print("TestCase001_completed successfully")
        support=DRSupport(self.driver)
        support.drSupportTab()
        support.drCreateSPTicket('1')
        support.drCrTitle("SampleCheck")
        support.drCrDescription("Not able to login Vm with valid cred")
        time.sleep(5)
        support.drCrUploadFile("C://Users/bhara/Downloads/file.png")
        time.sleep(5)
        support.drCrSubmit()
        time.sleep(10)
        support.drCustomerTab()
        time.sleep(5)
        support.drCusIncCheck('1',"Closed")
        support.drCusTicketCancel()
        myticket=support.drmyTicketTab()
        if myticket is True:
            print("NO Ticket raised")
            self.driver.get_screenshot_as_file("C:/Users/bhara/PycharmProjects/Framework/Screenshots/Noticket.png")
        else:
            time.sleep(5)
            support.drMyTicketIncCheck('Reopen',"Reopen")
            support.drMyTicketSave_Reopen()
