import pytest
from selenium import webdriver
from pageobject.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLog import LogGen
import time
from pageobject.DR_VmIMages import DRVmImage
from pageobject.DR_LoginPage import DR_Login

class TestDrVmImages:
    baseUrl=ReadConfig.getDRurl()
    emailId=ReadConfig.getdruserid()
    passWord=ReadConfig.getdrpwd()

    def test_VmImagePage(self,SetUp):
        self.driver=SetUp
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        loginPage=DR_Login(self.driver)
        loginPage.setEmailId(self.emailId)
        loginPage.setUserPwd(self.passWord)
        loginPage.mspLoginbutton()
        print("----User Login in Sucessfully")
        time.sleep(5)
        vmImagePage=DRVmImage(self.driver)
        vmImagePage.clickVmIcon()
        time.sleep(5)
        vmImagePage.clickAddImage()
        time.sleep(5)
        vmImagePage.enterImageName("VmTest")
        time.sleep(5)
        vmImagePage.enterImDescription("Sample QAtest")
        vmImagePage.modelPersonalicon()
        time.sleep(3)
        vmImagePage.regionSelect(12,5)
        time.sleep(3)
        vmImagePage.vmInstance(1)
        vmImagePage.imageGallery('1: Object')
        vmImagePage.addButton()

    def test_Error_message(self,SetUp):
        self.driver=SetUp
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        loginPage = DR_Login(self.driver)
        loginPage.setEmailId(self.emailId)
        loginPage.setUserPwd(self.passWord)
        loginPage.mspLoginbutton()
        print("##User Login in Sucessfully##")
        time.sleep(5)
        vmAddError=DRVmImage(self.driver)
        vmAddError.clickVmIcon()
        time.sleep(5)
        vmAddError.clickAddImage()
        time.sleep(3)
        vmAddError.addButton()
        vmAddError.errorVMImage()
        vmAddError.errorVmModels()
        vmAddError.errorVMDescription()
        vmAddError.errorVmImGallery()
        vmAddError.errorVmInstance()




