import pytest
from selenium import webdriver
from pageobject.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLog import LogGen
import time
from pageobject.AddCustomers import customerPage

class Test_003_Login:
    baseurl=ReadConfig.getApplicationUrl()
    username=ReadConfig.getUsername()
    password=ReadConfig.getPassword()

    def testloginPageCust(self,SetUp):
        self.driver=SetUp
        self.driver.get(self.baseurl)
        time.sleep(5)
        self.driver.maximize_window()
        self.loginpage=LoginPage(self.driver)
        self.loginpage.setUserName(self.username)
        self.loginpage.setPassWord(self.password)
        self.loginpage.clickLogin()
        time.sleep(5)
        self.addCustomer=customerPage(self.driver)
        self.addCustomer.clickonCustomerMenu()
        time.sleep(5)
        self.addCustomer.clickonCustomerList()
        time.sleep(5)
        self.addCustomer.clickOnAddCust()
        time.sleep(5)
        self.addCustomer.enterEmailId("Bharani@gmail.com")
        self.addCustomer.enterPassword("Pass@123")
        self.addCustomer.enterFirstName("Bharani")
        self.addCustomer.enterLastName("Murali")
        self.addCustomer.SelGender("Female")
        self.addCustomer.dateOfBirth("15/15/1994")
        self.addCustomer.companyName("AnuntaTech")
        self.addCustomer.selNewsletter("Your")
        self.addCustomer.selCustomerRole("Guests")
        self.addCustomer.selManageOfVendor("Vendor 1")
        self.addCustomer.saveButton()

        self.msg= self.driver.find_element_by_tag_name("body").text

        if "The customer cannot be in both 'Guests' and 'Registered' customer roles" in self.msg:
            print("Completed stage 1")
            assert True
            if "The value '15/12/1994' is not valid for Date of birth." in self.msg:
                print("Test execution Completed--Passed 2")
                assert True

        else:
            print("Test execution completed--Fail")
            assert False
