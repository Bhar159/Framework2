import pytest
from selenium import webdriver
from pageobject.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLog import LogGen
import time
from pageobject.DR_Support import DRSupport
from pageobject.DR_LoginPage import DR_Login
from utilities import Xlutils

class Test_DrSupport_Func:
    # path = "C:\\Users\\bhara\\PycharmProjects\\Framework\\TestData\\DR_SupportTestData.xlsx"

    # baseUrl=ReadConfig.getDRurl()
    # userID = ReadConfig.getdruserid()
    # password=ReadConfig.getdrpwd()

    def test_anuntaOne_Tc001(self,SetUp):
        self.path = "C:\\Users\\bhara\\PycharmProjects\\Framework\\TestData\\DR_SupportTestData.xlsx"

        self.baseUrl =Xlutils.readData(self.path,'Credentials',2,1)
        self.userID = Xlutils.readData(self.path,'Credentials',2,2)
        self.password = Xlutils.readData(self.path,'Credentials',2,3)
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

        anuntaOne = Xlutils.getRowCount(self.path, 'AnuntaOne')

        for r in range(2,anuntaOne+1):
            self.title=Xlutils.readData(self.path,'AnuntaOne',r,1)
            self.description=Xlutils.readData(self.path, 'AnuntaOne', r,2)
            self.file_attachment=Xlutils.readData(self.path,'AnuntaOne', r,3)

            support=DRSupport(self.driver)
            support.drSupportTab()
            support.drCreateSPTicket('1')

            support.drCrTitle(self.title)
            support.drCrDescription(self.description)
            time.sleep(5)
            support.drCrUploadFile(self.file_attachment)
            time.sleep(5)
            support.drCrSubmit()
            time.sleep(10)

    def test_anuntaTwo_Tc002(self, SetUp):
        self.path = "C:\\Users\\bhara\\PycharmProjects\\Framework\\TestData\\DR_SupportTestData.xlsx"

        self.baseUrl = Xlutils.readData(self.path, 'Credentials', 3, 1)
        self.userID = Xlutils.readData(self.path, 'Credentials', 3, 2)
        self.password = Xlutils.readData(self.path, 'Credentials', 3, 3)
        self.driver = SetUp
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        print(self.driver.title)
        loginPage = DR_Login(self.driver)
        loginPage.setEmailId(self.userID)
        loginPage.setUserPwd(self.password)
        loginPage.mspLoginbutton()
        time.sleep(5)
        print("TestCase001_completed successfully")

        anuntaOne = Xlutils.getRowCount(self.path, 'AnuntaTwo')

        for r in range(2, anuntaOne + 1):
            self.title = Xlutils.readData(self.path, 'AnuntaTwo', r, 1)
            self.description = Xlutils.readData(self.path, 'AnuntaTwo', r, 2)
            self.file_attachment = Xlutils.readData(self.path, 'AnuntaTwo', r, 3)

            support = DRSupport(self.driver)
            support.drSupportTab()
            support.drCreateSPTicket('1')

            support.drCrTitle(self.title)
            support.drCrDescription(self.description)
            time.sleep(5)
            support.drCrUploadFile(self.file_attachment)
            time.sleep(5)
            support.drCrSubmit()
            time.sleep(10)




        # support.drCustomerTab()
        # time.sleep(5)
        # support.drCusIncCheck('1',"Closed")
        # support.drCusTicketCancel()
        # myticket=support.drmyTicketTab()
        # if myticket is True:
        #     print("NO Ticket raised")
        #     self.driver.get_screenshot_as_file("C:/Users/bhara/PycharmProjects/Framework/Screenshots/Noticket.png")
        # else:
        #     time.sleep(5)
        #     support.drMyTicketIncCheck('Reopen',"Reopen")
        #     support.drMyTicketSave_Reopen()
