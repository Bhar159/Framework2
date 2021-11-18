from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import selenium

class DRSubscription:
    subscription_main_button_xpath="//span[contains(text(),'Subscriptions')]"
    managesubscription_button_xpath="//div[@class='mat-tab-list']/div/div[1]"
    addSubscription_button_xpath="//div[@class='mat-tab-list']/div/div[2]"
    newSubscription_page_text="//div[contains(text(),\"Enter new subscription's details\")]"

    sharedsub_checkbox_xpath="//div[@class='ng-star-inserted']/div[2]/div/div[2]/div/div/div[1]/div/div[1]/div[2]/input"
    dedicatedsub_checkbox_xpath="//div[@class='ng-star-inserted']/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div[2]/input"
    #***************azureAD sync*************************
    azureAd_signinButton_xpath="//div[@class='ng-star-inserted']/div[3]/div/div[2]/div/div/div/div[contains(text(),'Azure AD')]"
    addnewsubscription_button = "//button[contains(text(),'Add new subscription')]"
    cancelSubscription_button="//div[@class='ng-star-inserted']/div[6]//div//button[contains(text(),'Cancel')] "
    selectSub_dropdown_xpath = "//div[@class='ng-star-inserted']/div[3]/div/div[2]/div/div/div[3]/div/form/div/select"
    displayName_textbox_xpath = "//div[@class='ng-star-inserted']/div[5]/div/div[2]/div/div/form/div/div/div/input"
    region_select_xpath = "//div[@class='ng-star-inserted']/div[5]/div/div[2]/div/div/form/div/div[2]/div/select"
    connectSub_text="//div[contains(text(),'Connect subscription')]"

    #SignIn page(userID)
    signintoyouraccount_text = "//title[contains(text(),'Sign in to your account')]"
    signIN_text="//div[contains(text(),'Sign in')]"
    wrongEmailId_text="//div[contains(text(),'Enter a valid email address or phone number.')]"
    mutliemailAdress_xpath="//div[@id='otherTileText']"
    signInemailID_textbox_xpath="//input[@id='i0116']"
    emailIdNext_page_button="//input[@id='idSIButton9']"
    emailIdBack_page_button="//input[@id='idBtn_Back']"

    # SignIn page(Password)
    enterPassword_text="//div[contains(text(),'Enter password')]"
    wrongPwd_text="//div[contains(text(),\"Your account or password is incorrect. If you don't remember your password\")]"
    signInPassword_textbox_xpath = "//input[@id='i0118']"
    loginButton_button = "//input[@id='idSIButton9']"
    #staysigned In page
    staysignedIN_text="//div[contains(text(),'Stay signed in?')]"
    noButton_xpath="//input[@id='idBtn_Back']"
    yesButton_xpath="//input[@id='idSIButton9']"


    #*****************Manual entry*****************************
    mEntermanually_Icon_xpath="//div[@class='ng-star-inserted']/div[3]/div/div[2]/div/div/div/div[2]"
    mSubscritionName_textbox_xpath="//div[@class='ng-star-inserted']/div[4]/div/div[2]/div/div/div/form/div[1]/div/input"
    mSubscriptionId_textbox_xpath="//div[@class='ng-star-inserted']/div[4]/div/div[2]/div/div/div/form/div[2]/div/input"
    mAppID_textbox_xpath="//div[@class='ng-star-inserted']/div[4]/div/div[2]/div/div/div/form/div[3]/div/input"
    mClientId_textbox_xpath="//div[@class='ng-star-inserted']/div[4]/div/div[2]/div/div/div/form/div[4]/div/div/input"
    mTenantName_textbox_xapth="//div[@class='ng-star-inserted']/div[4]/div/div[2]/div/div/div/form/div[5]/div/div/input"
    mTenantId_textbox_xpath="//div[@class='ng-star-inserted']/div[4]/div/div[2]/div/div/div/form/div[6]/div/input"
    mGlobalAdmin_username_xpath="//div[@class='ng-star-inserted']/div[4]/div/div[2]/div/div/div/form/div[7]/div[2]/div/input"
    mGlobalAdmin_Password_xpath="//div[@class='ng-star-inserted']/div[4]/div/div[2]/div/div/div/form/div[7]/div[3]/div/input"
    mRegion_dropdown_xapth="//div[@class='ng-star-inserted']/div[4]/div/div[2]/div/div/div/form/div[8]/div/select"
    mCancelButton_xapth="//div[@class='ng-star-inserted']/div[5]/div/div/div/div/button[1]"
    mAddButton_xpath="//div[@class='ng-star-inserted']/div[5]/div/div/div/div/button[2]"

    #***********already subscription existing********
    esubexisting_text_xpath="//div[@class='row py-4 ng-star-inserted']/div[2]/div/div/div//span[contains(text(),' You are currently logged in as')]"
    elogout_button_xpath="//div[@class='row py-4 ng-star-inserted']/div[2]/div/div/div//span[contains(text(),' You are currently logged in as')]/span"
    elogoutFirstoption_xpath="//div[@class='tile-container'][1]"
    eazureAD_text_xapth="//div[@class='ng-star-inserted']/div[3]/div/div[2]/div/div/div/div[contains(text(),'Azure AD')]"


    def __init__(self,driver):
        self.driver=driver

    def drsubscriptionTab(self):
        self.driver.find_element_by_xpath(self.subscription_main_button_xpath).click()
        time.sleep(2)
    def drmanageSubTab(self):
        self.driver.find_element_by_xpath(self.managesubscription_button_xpath).click()
        time.sleep(2)
    def drAddSubscriptionTab(self):
        self.driver.find_element_by_xpath(self.addSubscription_button_xpath).click()
        time.sleep(3)

    def sharedSubCheckBox(self):
        self.driver.find_element_by_xpath(self.sharedsub_checkbox_xpath).click()
    def dedicatedSubCheckBox(self):
        self.driver.find_element_by_xpath(self.dedicatedsub_checkbox_xpath).click()

    def existingAccountLogout(self):
        azureADtext=self.driver.find_element_by_xpath(self.eazureAD_text_xapth)

        if (azureADtext.is_displayed):
            print("Validation pass")

        else:
            existingAccount = self.driver.find_element_by_xpath(self.esubexisting_text_xpath)
            if (existingAccount.is_displayed):
                print("Existing account will be logged off")
                self.driver.find_element_by_xpath(self.elogout_button_xpath).click()
                time.sleep(5)
                self.driver.find_element_by_xpath(self.elogoutFirstoption_xpath).click()
                time.sleep(5)
                self.drAddSubscriptionTab()
                time.sleep(5)
                self.sharedSubCheckBox()



    def azureSignInButton(self,userID,password):
        self.driver.find_element_by_xpath(self.azureAd_signinButton_xpath).click()
        time.sleep(10)
        logintitle=self.driver.find_element_by_xpath(self.signintoyouraccount_text).text
        signInpage=self.driver.find_element_by_xpath(self.signIN_text).text
        if logintitle=="Sign in to your account":
            print("User in correct page")
            self.driver.find_element_by_xpath(self.signInemailID_textbox_xpath).send_keys(userID)
            self.driver.find_element_by_xpath(self.emailIdNext_page_button).click()
            time.sleep(5)
            pwdPagetitle=self.driver.find_element_by_xpath(self.enterPassword_text).text
            if pwdPagetitle == "Enter password":
                print("user in pwd page")
                self.driver.find_element_by_xpath(self.signInPassword_textbox_xpath).send_keys(password)
                self.driver.find_element_by_xpath(self.loginButton_button).click()
                time.sleep(5)
                staySigninPage = self.driver.find_element_by_xpath(self.staysignedIN_text).text
                print(staySigninPage)
                if staySigninPage == "Stay signed in?":
                    print("user in stay signIn page")
                    time.sleep(5)
                    self.driver.find_element_by_xpath(self.noButton_xpath).click()
                    time.sleep(25)
                    subPage = self.driver.find_element_by_xpath(self.newSubscription_page_text).is_displayed()
                    print(subPage)
                    if subPage == True:
                        assert True, "Passed"
                else:
                    pwdWrong = self.driver.find_element_by_xpath(self.wrongPwd_text).text
                    print(pwdWrong)
                    if pwdWrong == "Your account or password is incorrect. If you don't remember your password, reset it now.":
                        print("please enter correct password")
                        assert "Your account or password is incorrect" in pwdWrong
                        print("Please check the given password")

        elif signInpage=="Sign in":
            print("User in sign In page")
            self.driver.find_element_by_xpath(self.signInemailID_textbox_xpath).send_keys(userID)
            self.driver.find_element_by_xpath(self.emailIdNext_page_button).click()
            time.sleep(5)
            pwdPagetitle = self.driver.find_element_by_xpath(self.enterPassword_text).text
            if pwdPagetitle == "Enter password":
                print("user in pwd page")
                self.driver.find_element_by_xpath(self.signInPassword_textbox_xpath).send_keys(password)
                self.driver.find_element_by_xpath(self.loginButton_button).click()
                time.sleep(5)
                staySigninPage = self.driver.find_element_by_xpath(self.staysignedIN_text).text
                print(staySigninPage)
                if staySigninPage == "Stay signed in?":
                    print("user in stay signIn page")
                    time.sleep(5)
                    self.driver.find_element_by_xpath(self.noButton_xpath).click()
                    time.sleep(25)
                    subPage = self.driver.find_element_by_xpath(self.newSubscription_page_text).is_displayed()
                    print(subPage)
                    if subPage == True:
                        assert True, "Passed"
                else:
                    pwdWrong = self.driver.find_element_by_xpath(self.wrongPwd_text).text
                    print(pwdWrong)
                    if pwdWrong == "Your account or password is incorrect. If you don't remember your password, reset it now.":
                        print("please enter correct password")
                        assert "Your account or password is incorrect" in pwdWrong
                        print("Please check the given password")

        else:
            print("Server Down")


    def subscriptionList(self,subvalue):
        subSelectDropDown=Select(self.driver.find_element_by_xpath(self.selectSub_dropdown_xpath))
        selectList = subSelectDropDown.options
        print(len(selectList))
        for x in selectList:
            print(x.text)
        subSelectDropDown.select_by_value(subvalue)

    def display_name(self,name):
        self.driver.find_element_by_xpath(self.displayName_textbox_xpath).send_keys(name)

    def regionlist(self,value):
        regionSelect=Select(self.driver.find_element_by_xpath(self.region_select_xpath))
        regionlist=regionSelect.options
        region_list=[]
        for x in regionlist:
            print(x.text)
            region_list.append(x.text)
        if value <= 14:
            regionSelect.select_by_value(str(value)+": Object")
        else:
            print("country code not available")
            assert False, "Please change the country code"

    def addNewSubscription(self):
        self.driver.find_element_by_xpath(self.addnewsubscription_button).click()
        print("Subscription added successfully")

    def cancelSubscription(self):
        self.driver.find_element_by_xpath(self.cancelSubscription_button).click()
        time.sleep(5)
        entersub_check=self.driver.find_element_by_xpath(self.connectSub_text).is_displayed()
        if entersub_check==True:
            print("Working as expected")
        else:
            print("Error in the scenario")
            assert False,"falsed"


    def selectManualIcon(self):
        self.driver.find_element_by_xpath(self.mEntermanually_Icon_xpath).click()
        time.sleep(2)
    def mSubscriptionName(self,subName):
        self.driver.find_element_by_xpath(self.mSubscritionName_textbox_xpath).send_keys(subName)

    def mSubscriptionId(self,subId):
        self.driver.find_element_by_xpath(self.mSubscriptionId_textbox_xpath).send_keys(subId)
    def msubAppId(self,subAppID):
        self.driver.find_element_by_xpath(self.mAppID_textbox_xpath).send_keys(subAppID)
    def msubClientKey(self,clientKey):
        self.driver.find_element_by_xpath(self.mClientId_textbox_xpath).send_keys(clientKey)
    def mTenantName(self,tenantName):
        self.driver.find_element_by_xpath(self.mTenantName_textbox_xapth).send_keys(tenantName)

    def mTenantID(self,tenantID):
        self.driver.find_element_by_xpath(self.mTenantId_textbox_xpath).send_keys(tenantID)

    def mGlobalAdminName(self,adminName):
        self.driver.find_element_by_xpath(self.mGlobalAdmin_username_xpath).send_keys(adminName)
    def mGlobalAdminPwd(self,gPassword):
        self.driver.find_element_by_xpath(self.mGlobalAdmin_Password_xpath).send_keys(gPassword)

    def mregionlist(self,value):
        regionSelect=Select(self.driver.find_element_by_xpath(self.mRegion_dropdown_xapth))
        regionlist=regionSelect.options
        region_list=[]
        for x in regionlist:
            print(x.text)
            region_list.append(x.text)
        if value <= 14:
            regionSelect.select_by_value(str(value)+": Object")
        else:
            print("country code not available")
            assert False, "Please change the country code"

    def maddNewSubscription(self):
        self.driver.find_element_by_xpath(self.mAddButton_xpath).click()
        print("Subscription added successfully")

    def mcancelSubscription(self):
        self.driver.find_element_by_xpath(self.mCancelButton_xapth).click()
        time.sleep(5)
        entersub_check=self.driver.find_element_by_xpath(self.connectSub_text).is_displayed()
        if entersub_check==True:
            print("Working as expected")
        else:
            print("Error in the scenario")
            assert False,"falsed"














