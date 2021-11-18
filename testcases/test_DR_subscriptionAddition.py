import pytest
from selenium import webdriver
from utilities.readProperties import ReadConfig
from utilities.customLog import LogGen
import time
from pageobject.DR_Support import DRSupport
from pageobject.DR_LoginPage import DR_Login
from pageobject.DR_Subscription import DRSubscription
from utilities import Xlutils

class Test_DRSubscriptionAddition:

    @pytest.mark.azureAdSync
    def test_AzureADSync_001(self,HeadlessMode):
        self.path = "C:\\Users\\ADMIN\\PycharmProjects\\Framework2\\TestData\\DR_SupportTestData.xlsx"
        subcount=Xlutils.getRowCount(self.path,'Subscriptions')

        for x in range(2,subcount+1):
            self.url = Xlutils.readData(self.path, 'Subscriptions', x, 1)
            self.userID = Xlutils.readData(self.path, 'Subscriptions', x, 2)
            self.password = Xlutils.readData(self.path, 'Subscriptions', x, 3)
            self.azureEmailID = Xlutils.readData(self.path, 'Subscriptions', x, 4)
            self.azurePwd = Xlutils.readData(self.path, 'Subscriptions', x, 5)
            automationName=Xlutils.readData(self.path,'Subscriptions', x,6)

            self.driver = HeadlessMode
            self.driver.get(self.url)
            print("User able to navigate to webpage ")
            self.driver.maximize_window()
            print(self.driver.title)
            loginPage = DR_Login(self.driver)
            loginPage.setEmailId(self.userID)
            loginPage.setUserPwd(self.password)
            loginPage.mspLoginbutton()
            time.sleep(10)
            print("TestCase001_completed successfully")

            subscriptionadd = DRSubscription(self.driver)
            subscriptionadd.drsubscriptionTab()
            subscriptionadd.drAddSubscriptionTab()
            subscriptionadd.sharedSubCheckBox()
            subscriptionadd.azureSignInButton(self.azureEmailID, self.azurePwd)
            subscriptionadd.subscriptionList("1: Object")
            subscriptionadd.display_name(automationName)
            subscriptionadd.regionlist(5)
            #subscriptionadd.addNewSubscription()
            subscriptionadd.cancelSubscription()


    @pytest.mark.skip(reason="I dont want to run this testcase")
    def test_ManualEntry(self,HeadlessMode):
        # self.customerpath = "C:\\Users\\bhara\\PycharmProjects\\Framework\\TestData\\DR_SupportTestData.xlsx"
        # self.url = Xlutils.readData(self.customerpath, 'Credentials', 7, 1)
        # self.userID = Xlutils.readData(self.customerpath, 'Credentials', 7, 2)
        # self.password = Xlutils.readData(self.customerpath, 'Credentials', 7, 3)

        customerpath = "C:\\Users\\bhara\\PycharmProjects\\Framework\\TestData\\DR_SupportTestData.xlsx"
        url = Xlutils.readData(customerpath, 'Credentials', 7, 1)
        userID = Xlutils.readData(customerpath, 'Credentials', 7, 2)
        password = Xlutils.readData(customerpath, 'Credentials', 7, 3)

        self.subpath = "C:\\Users\\bhara\\PycharmProjects\\Framework\\TestData\\DR_SupportTestData.xlsx"
        subName = Xlutils.readData(self.subpath, 'Tenant', 1, 2)
        subId=Xlutils.readData(self.subpath,'Tenant',2,2)
        appId=Xlutils.readData(self.subpath,'Tenant',3,2)
        clientId = Xlutils.readData(self.subpath, 'Tenant', 4,2)
        tenantName=Xlutils.readData(self.subpath, 'Tenant', 5,2)
        tenantId=Xlutils.readData(self.subpath, 'Tenant', 6,2)
        globalName=Xlutils.readData(self.subpath, 'Tenant', 7,2)
        globalPwd=Xlutils.readData(self.subpath, 'Tenant', 8,2)


        self.driver=HeadlessMode
        self.driver.get(url)
        self.driver.maximize_window()
        print(self.driver.title)
        loginPage = DR_Login(self.driver)
        loginPage.setEmailId(userID)
        loginPage.setUserPwd(password)
        loginPage.mspLoginbutton()
        time.sleep(5)
        print("TestCase001_completed successfully")
        manualaddition=DRSubscription(self.driver)
        manualaddition.drsubscriptionTab()
        manualaddition.drAddSubscriptionTab()
        manualaddition.dedicatedSubCheckBox()
        manualaddition.selectManualIcon()
        manualaddition.mSubscriptionName(subName)
        manualaddition.mSubscriptionId(subId)
        manualaddition.msubAppId(appId)
        manualaddition.msubClientKey(clientId)
        manualaddition.mTenantName(tenantName)
        manualaddition.mTenantID(tenantId)
        manualaddition.mGlobalAdminName(globalName)
        manualaddition.mGlobalAdminPwd(globalPwd)
        manualaddition.mregionlist(6)
        #manualaddition.maddNewSubscription()
        manualaddition.mcancelSubscription()


