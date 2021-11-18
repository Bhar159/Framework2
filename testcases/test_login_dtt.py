import pytest
from selenium import webdriver
from pageobject.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLog import LogGen
from utilities import Xlutils
import time

class Test_002_Login_DTT:
    baseUrl=ReadConfig.getApplicationUrl()
    path="C:\\Users\\bhara\\PycharmProjects\\Framework\\TestData\\loginData.xlsx"

    log_generator=LogGen.log()

    def test_homePageTitle(self,SetUp):
        self.log_generator.info("******************Test_002_Login_DTT*************************")
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

    def test_login_DDT(self,SetUp):
        self.log_generator.info("******************test_login_testcase_002*********************************")
        self.log_generator.info("//Started///")
        self.driver=SetUp
        self.driver.get(self.baseUrl)
        self.ip=LoginPage(self.driver)

        list_status=[]

        xutil=Xlutils.getRowCount(self.path,'Sheet1')

        for r in range(2,xutil+1):
            self.username=Xlutils.readData(self.path,'Sheet1',r,1)
            self.password=Xlutils.readData(self.path, 'Sheet1', r,2)
            self.exp=Xlutils.readData(self.path,'Sheet1',r,3)

            self.ip.setUserName(self.username)
            self.ip.setPassWord(self.password)
            self.ip.clickLogin()
            time.sleep(5)
            page_title=self.driver.title
            if page_title==self.driver.title:
                if self.exp=="Pass":
                    self.ip.clickLogout()
                    list_status.append('Pass')
                    self.log_generator.info("*******Pass*******")
                elif self.exp=="Fail":
                    #self.ip.clickLogout()
                    list_status.append('Fail')

            elif page_title != self.driver.title:
                if self.exp=="Pass":
                    list_status.append('Pass')
                    self.log_generator.info("*******Pass*******")
                elif self.exp=="Fail":
                    list_status.append('Fail')
                    self.log_generator.info("*******Fail*******")

        if 'Fail' not in list_status:
            self.driver.close()
            self.log_generator.info("******************BDD completed**********")







