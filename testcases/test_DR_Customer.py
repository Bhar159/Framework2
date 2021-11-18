import pytest
from selenium import webdriver
from pageobject.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLog import LogGen
import time
from pageobject.DR_Customer import DRCustomer
from pageobject.DR_LoginPage import DR_Login
from utilities import Xlutils


class Test_DrSupport_Func:


    def test_AddNewCustomer(self,SetUp):
        self.path = "C:\\Users\\bhara\\PycharmProjects\\Framework\\TestData\\DR_SupportTestData.xlsx"
        subcount = Xlutils.getRowCount(self.path, 'MultiCred')

        for x in range(2, subcount + 1):
            self.url = Xlutils.readData(self.path, 'MultiCred', x, 1)
            self.userID = Xlutils.readData(self.path, 'MultiCred', x, 7)
            self.password = Xlutils.readData(self.path, 'MultiCred', x, 8)
            self.azureEmailID = Xlutils.readData(self.path, 'MultiCred', x, 4)
            self.azurePwd = Xlutils.readData(self.path, 'MultiCred', x, 5)
            self.companyName=Xlutils.readData(self.path,'MultiCred',x,10)
            self.Address1 = Xlutils.readData(self.path, 'MultiCred', x, 11)
            self.Address2 = Xlutils.readData(self.path, 'MultiCred', x, 12)
            self.country=Xlutils.readData(self.path, 'MultiCred', x, 13)
            self.zipCode=Xlutils.readData(self.path, 'MultiCred', x, 14)
            self.firstNm=Xlutils.readData(self.path, 'MultiCred', x, 15)
            self.secondNm = Xlutils.readData(self.path, 'MultiCred', x, 16)
            self.emailId = Xlutils.readData(self.path, 'MultiCred', x, 17)
            self.phoneNm = Xlutils.readData(self.path, 'MultiCred', x, 18)
            self.customDesktopCount = Xlutils.readData(self.path, 'MultiCred', x, 19)


            self.log_generator = LogGen.log()
            self.log_generator.info("****Started*****")
            self.driver=SetUp
            self.driver.get(self.url)
            self.log_generator.info("*******login page opened successfully*********")
            self.driver.maximize_window()
            print(self.driver.title)
            loginPage = DR_Login(self.driver)
            loginPage.setEmailId(self.userID)
            loginPage.setUserPwd(self.password)
            loginPage.mspLoginbutton()
            self.log_generator.info("*******login page validation completed successfully*********")
            time.sleep(5)
            print("TestCase001_completed successfully")
            addCustomer=DRCustomer(self.driver)
            self.log_generator.info("*******Home dashboard*********")
            addCustomer.customertab()
            self.log_generator.info("*******customer dashboard*********")
            addCustomer.addCustomer()
            self.log_generator.info("*******Customer addition started successfully*********")
            addCustomer.addCompanyName(self.companyName)
            addCustomer.addAddress1(self.Address1)
            addCustomer.addAddress2(self.Address2)
            addCustomer.addCountry(self.country)
            addCustomer.addZipCode(self.zipCode)
            time.sleep(3)
            addCustomer.addFirstName(self.firstNm)
            addCustomer.addLastName(self.secondNm)
            addCustomer.addEmailAddress(self.emailId)
            addCustomer.addPhoneNumber(self.phoneNm)
            time.sleep(5)
            addCustomer.customerNextpage()
            self.log_generator.info("*******Subscription addition started*********")
            addCustomer.infra_SharedOption()
            addCustomer.infra_subscription_select()
            addCustomer.infra_nextButton()
            self.log_generator.info("*******Subscription selected successfully*********")
            self.log_generator.info("*******Desktop addition started*********")
            addCustomer.desktopSelection_personal()
            # addCustomer.powerdesktop_personalInc(5)
            # addCustomer.multiDesktop_Inc(5)
            # time.sleep(5)
            # addCustomer.desktopSelection_pooled()
            # time.sleep(5)
            # addCustomer.lightdesktop_pooledInc(5)
            # addCustomer.mediumdesktop_pooledInc(2)
            # addCustomer.heavydesktop_pooledInc(8)
            addCustomer.customDesktop_Inc(self.customDesktopCount)
            addCustomer.desktop_NextButton()
            self.log_generator.info("*******Desktop addition completed*********")
            self.log_generator.info("*******Addons addition started*********")
            addCustomer.addOns_BackFile()
            addCustomer.addOns_Firewall()
            addCustomer.addOns_NextButton()
            self.log_generator.info("*******Addons added successfully*********")
            self.log_generator.info("*******Customer review page*********")
            addCustomer.reviewPage_AddCustomerButton()
            self.log_generator.info("*******New customer added successfully*********")
            time.sleep(5)