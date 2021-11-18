import pytest
from selenium import webdriver
from utilities.readProperties import ReadConfig
from utilities.customLog import LogGen
import time
from pageobject.DR_DesktopAddition import DRManageDesktop
from pageobject.DR_LoginPage import DR_Login
from utilities import Xlutils
import random as r
import string

class Test_DR_User:
    url = ReadConfig.getDRurl()
    userID = ReadConfig.getdruserid()
    userPwd = ReadConfig.getdrpwd()

    def randomNames(self):
        Nonvowels = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y',
                     'z']
        vowels = ['a', 'e', 'i', 'o', 'u']
        randomNumber = r.randint(2, 4)
        name = ""
        for x in range(randomNumber):
            randomNonVowels = r.choice(Nonvowels)
            randomVowels = r.choice(vowels)
            name = name + randomVowels + randomNonVowels
        return name

    # userFirstName = randomNames()
    # userLastName = randomNames()

    def UseremailID(self,size=4, chars=string.ascii_lowercase + string.digits + string.ascii_uppercase):
        return ''.join(r.choice(chars) for x in range(size))





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
        customerPage.customerMenu()
        customerPage.customerlist()
        customerPage.userCreationallbutton()
        customerPage.userCreationIcon()
        a=1
        while a<=2:
            customerPage.userCreationNewButton()
            customerPage.userFirstName(self.randomNames())
            customerPage.userLastName(self.randomNames())
            userEmailid=self.UseremailID() +"@gmail.com"
            customerPage.userEmailID(userEmailid)
            #customerPage.userPhoneNumber("9632587412")
            customerPage.userCreateButton()
            time.sleep(5)
            customerPage.userCOnfirmationPopUp()
            a=a+1





