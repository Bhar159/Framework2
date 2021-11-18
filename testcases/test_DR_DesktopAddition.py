import pytest
from selenium import webdriver
from pageobject.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLog import LogGen
import time
from pageobject.DR_DesktopAddition import DRManageDesktop
from pageobject.DR_LoginPage import DR_Login
from utilities import Xlutils

class Test_DRDesktopaddition:

    def test_Desktopaddition_001(self,SetUp):
        self.path = "C:\\Users\\ADMIN\\PycharmProjects\\Framework2\\TestData\\DR_SupportTestData.xlsx"
        mspRowCount=Xlutils.getRowCount(self.path,'DesktopAddition')

        for x in range(2,mspRowCount+1):

            self.url=Xlutils.readData(self.path,'DesktopAddition',x,1)
            self.userID=Xlutils.readData(self.path,'DesktopAddition',x,2)
            self.password=Xlutils.readData(self.path,'DesktopAddition',x,3)

            self.driver =SetUp
            self.driver.get(self.url)
            self.driver.maximize_window()
            print(self.driver.title)
            loginPage = DR_Login(self.driver)
            loginPage.setEmailId(self.userID)
            loginPage.setUserPwd(self.password)
            loginPage.mspLoginbutton()
            time.sleep(5)
            print("TestCase001_completed successfully")

            #Desktop functionality

            desktopAdd=DRManageDesktop(self.driver)
            desktopAdd.customerMenu()
            desktopAdd.customerlist()
            desktopAdd.addDesktop()
            desktopAdd.pooledDesktopSelect()
            desktopAdd.lightPooledInc(1)
            desktopAdd.mediumPooledInc(2)
            desktopAdd.heavyPooledInc(2)
            desktopAdd.personalDesktopIcon()
            desktopAdd.powerPersonalInc(2)
            desktopAdd.multiPersonalInc(2)