from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

class DR_Login:

    textbox_EmailId_Xpath="//div[@class='p-4 ng-star-inserted']/form/div[1]/div/input"
    textbox_pwd_xpath="//div[@class='p-4 ng-star-inserted']/form/div[2]/div/input"
    text_Msg_email_xpath="//div[@class='p-4 ng-star-inserted']/form/div[1]/div/div[contains(text(),' Please enter your Username / Email ID ')]"
    text_msg_pwd_xpath="//div[@class='p-4 ng-star-inserted']/form/div[2]/div/div[contains(text(),'Please enter your Password')]"
    button_login_xpath="//button/span[contains(text(),'Login')]"
    User_tab_xpath="//div[@class='col-lg-5 bg-white']/mat-tab-group/mat-tab-header/div[2]/div/div/div[2]"
    admin_tab_xpath="//div[@class='col-lg-5 bg-white']/mat-tab-group/mat-tab-header/div[2]/div/div/div[1]"
    text_UPN_xpath="//div[@class='p-4 ng-star-inserted']/form/div/div/input"
    text_UpnMsg_xpath="//div[@class='p-4 ng-star-inserted']/form/div/div/div[contains(text(),'Please')]"
    incorrectMsg_UPN_xpath="//span[contains(text(),'is incorrect')]"
    incorrectmsg_Admin_xpath="//span[contains(text(),'Username or password is incorrect')]"
    button_LoginUPN_xpath="//span[contains(text(),'Login')]"
    display_userid="//label[contains(text(),'User ID')]"
    link_forgetpwd_xpath="//label[contains(text(),'Forgot password ?')]"
    button_forgetCancel_xpath="//span[contains(text(),'Cancel')]"
    button_forgetReset_xpath="//span[contains(text(),'Reset')]"
    textbox_forgotemailID_xpath="//div[@class='p-0']/mat-tab-group/div/mat-tab-body/div/div/form/div/div/input"
    msg_forgotpwd_xpath="//div[contains(text(),'Email ID must be a valid email address')]"



    def __init__(self,driver):
        self.driver=driver

    def setEmailId(self,DRusername):
        self.driver.find_element_by_xpath(self.textbox_EmailId_Xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_EmailId_Xpath).click()
        self.driver.find_element_by_xpath(self.textbox_pwd_xpath).click()
        self.driver.find_element_by_xpath(self.textbox_EmailId_Xpath).click()
        time.sleep(2)

        userMsg=self.driver.find_element_by_xpath(self.text_Msg_email_xpath).text
        if userMsg=="Please enter your Username / Email ID":
            self.driver.find_element_by_xpath(self.textbox_EmailId_Xpath).send_keys(DRusername)
            assert True
        else:
            print("message displayed wrong")
            assert False

    def setUserPwd(self,password):
        #self.driver.find_element_by_xpath(self.textbox_pwd_xpath).clear()
        #self.driver.find_element_by_xpath(self.textbox_pwd_xpath).click()
        pwdMsg=self.driver.find_element_by_xpath(self.text_msg_pwd_xpath).text
        if pwdMsg=="Please enter your Password":
            self.driver.find_element_by_xpath(self.textbox_pwd_xpath).send_keys(password)
            assert True
        else:
            print("Message displayed wrong")
            assert False

    def usertabChange(self):
        self.driver.find_element_by_xpath(self.User_tab_xpath).click()

    def userIdpage(self,userid):
        self.driver.find_element_by_xpath(self.text_UPN_xpath).click()
        self.driver.find_element_by_xpath(self.display_userid).click()
        usermsg=self.driver.find_element_by_xpath(self.text_UpnMsg_xpath)
        if (usermsg.is_displayed()):
            self.driver.find_element_by_xpath(self.text_UPN_xpath).send_keys(userid)
        else:
            print("UserID message displayed wrong")
            assert False

    def mspLoginbutton(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()
        title_home=self.driver.title
        if title_home=="The Modern Digital Workplace":
            print("Login successful")
        else:
            print("Login failed")

    def wrongCredAdmin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()
        title_home = self.driver.title
        time.sleep(5)
        display = self.driver.find_element_by_xpath(self.incorrectmsg_Admin_xpath)
        if(display.is_displayed):
            print("Cred is worng ")
        else:
            print("Something is missing")

    def userLoginbutton(self):
        self.driver.find_element_by_xpath(self.button_LoginUPN_xpath).click()
        title_userHome=self.driver.title
        time.sleep(5)
        if title_userHome=="The Modern Digital Workplace":
            print("Login successful")
        else:
            print("Login failed")

    def setforgetpwd(self,restemailID):
        self.driver.find_element_by_xpath(self.link_forgetpwd_xpath).click()
        self.driver.find_element_by_xpath(self.textbox_forgotemailID_xpath).send_keys(restemailID)
        self.driver.find_element_by_xpath(self.button_forgetReset_xpath).click()
        worndEmailid=self.driver.find_element_by_xpath(self.msg_forgotpwd_xpath)
        if (worndEmailid.is_displayed):
            print("Wrong Cred functionality working fine..!!")
        else:
            print("Execution completed")

















