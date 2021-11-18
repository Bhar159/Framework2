from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import selenium

class DRCustomer:
    #-----------------------Customer details-------------------------
    mainButton_Customer_xpath="//span[contains(text(),'Customers')]"
    button_myCustomers_Xpath="//div[@class='mat-tab-label-container']/div/div/div[1]"
    button_addCustomers_xpath="//div[@class='mat-tab-label-container']/div/div/div[2]"
    text_addCustomer_xpath="//div[contains(text(),'Enter customer details')]"
    addCustomer_CompanyName_xpath="//div[@class='sub-content py-4']/div/div[2]/div/div[1]/div/input"
    addCustomer_Address1_xpath="//div[@class='sub-content py-4']/div/div[2]/div/div[2]/div/input"
    addCustomer_Address2_xpath="//div[@class='sub-content py-4']/div/div[2]/div/div[3]/div/input"
    addCustomer_country_xpath="//div[@class='sub-content py-4']/div/div[2]/div/div[4]/div/select"
    addCustomer_ZipCode_xpath="//div[@class='sub-content py-4']/div/div[2]/div/div[5]/div/input"
    addCustomer_FirstN_xpath="//mat-tab-body/div[1]/div[1]/form[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/input[1]"
    addCustomer_LastN_xpath="//mat-tab-body/div[1]/div[1]/form[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]/input[1]"
    addCustomer_EmailAddress_xpath="//mat-tab-body/div[1]/div[1]/form[1]/div[3]/div[1]/div[2]/div[1]/div[3]/div[1]/input[1]"
    addCustomer_PhoneN_xpath="//div[@class='p-4 ng-star-inserted']/form/div[3]//div[@class='col-sm-9']/div[1]/input"
    back_button_xpath="//span[contains(text(),'Back')]"
    next_button_xpath="//span[contains(text(),'Next')]"
    #----------------Infrastructure destails--------------------------------------
    text_InfraPage_xpath="//div[contains(text(),'Enter infrastructure details')]"
    plan_sharedCheckBox_xpath="//div[@class='p-0 ng-star-inserted']/form/div[2]/div/div[2]/div/div[1]/div/div/div/input"
    plan_DediatedCheckBox_xpath="//div[@class='p-0 ng-star-inserted']/form/div[2]/div/div[2]/div/div[2]/div/div/div/input"
    sharedPlan_dropdown_xpath="//div[@class='p-0 ng-star-inserted']/form/div[3]/div/div[2]/div/div/div/div/div/div/select"
    plan_back_button="//span[contains(text(),'Back')]"
    plan_next_button="//span[contains(text(),'Next')]"
    #------------------------------Desktop-Plan----------------------------------------
    text_addDesktop_xpath="//div[contains(text(),'Add desktops')]"
    #personal
    desktop_PersonalButton_xpath="//div[@class='p-4 ng-star-inserted']/form/div[2]/div/div[2]/div/mat-tab-group/mat-tab-header/div/div/div/div[1]"
    powerdesktop_plus_button = "//mat-tab-body/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/app-number-input[1]/div[1]/div[2]/i[2]"
    powerdesktop_minus_button = "//mat-tab-body/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/app-number-input[1]/div[1]/div[2]/i[1]"
    multiDesktop_plusButton_xpath="//mat-tab-body/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/app-number-input[1]/div[1]/div[2]/i[2]"
    multiDesktop_minusButton_xpath="//mat-tab-body/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/app-number-input[1]/div[1]/div[2]/i[1]"
    #Pooled
    desktop_pooledButton_xpath="//div[@class='p-4 ng-star-inserted']/form/div[2]/div/div[2]/div/mat-tab-group/mat-tab-header/div/div/div/div[2]"
    lightDesktop_plusbutton_xpath = "//mat-tab-body/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/app-number-input[1]/div[1]/div[2]/i[2]"
    lightDesktop_minusbutton_xpath = "//mat-tab-body/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/app-number-input[1]/div[1]/div[2]/i[1]"
    mediumDesktop_plusbutton_xpath="//mat-tab-body/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/app-number-input[1]/div[1]/div[2]/i[2]"
    mediumDesktop_minusbutton_xpath="//mat-tab-body/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/app-number-input[1]/div[1]/div[2]/i[1]"
    heavyDesktop_plusButton_xpath="//mat-tab-body/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/app-number-input[1]/div[1]/div[2]/i[2]"
    heavyDesktop_minusButton_xpath="//mat-tab-body/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/app-number-input[1]/div[1]/div[2]/i[1]"
    desktop_backButton_xpath="//span[contains(text(),'Back')]"
    desktop_nextButton_xpath="//span[contains(text(),'Next')]"
    #customModel
    cDesktop_plus_button="//mat-tab-body/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/app-number-input[1]/div[1]/div[2]/i[2]"
    cDesktop_minus_button="//mat-tab-body/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/app-number-input[1]/div[1]/div[2]/i[1]"

    #--------Select ADD Ons -------------------------------------
    backUp_filesetup_xpath="//input[@id='BackUp']"
    firewall_setup_xpath="//input[@id='Firewall']"
    addOns_back_button = "//span[contains(text(),'Back')]"
    addOns_next_button = "//span[contains(text(),'Next')]"

    #-------------------------Review Page-------------------------------
    reviewPage_back_button = "//span[contains(text(),'Back')]"
    submit_button_xpath = "//span[contains(text(),'Add Customer')]"



    def __init__(self,driver):
        self.driver=driver

    def customertab(self):
        self.driver.find_element_by_xpath(self.mainButton_Customer_xpath).click()
        time.sleep(5)

    def addCustomer(self):
        self.driver.find_element_by_xpath(self.button_addCustomers_xpath).click()
        time.sleep(3)
        pageheader=self.driver.find_element_by_xpath(self.text_addCustomer_xpath).text
        if pageheader=="Enter customer details":
            print("User in customer addition page")
        else:
            print("Error in code")
            assert False

    def addCompanyName(self,name):
        self.driver.find_element_by_xpath(self.addCustomer_CompanyName_xpath).send_keys(name)

    def addAddress1(self,address1):
        self.driver.find_element_by_xpath(self.addCustomer_Address1_xpath).send_keys(address1)

    def addAddress2(self,address2):
        self.driver.find_element_by_xpath(self.addCustomer_Address2_xpath).send_keys(address2)

    def addCountry(self,value):
        selectCountry=Select(self.driver.find_element_by_xpath(self.addCustomer_country_xpath))
        selectCountry.select_by_value(value)
        print("Select country"+str(value))

    def addZipCode(self,zipCode):
        self.driver.find_element_by_xpath(self.addCustomer_ZipCode_xpath).send_keys(zipCode)

    def addFirstName(self,fName):
        self.driver.find_element_by_xpath(self.addCustomer_FirstN_xpath).send_keys(fName)

    def addLastName(self,lName):
        self.driver.find_element_by_xpath(self.addCustomer_LastN_xpath).send_keys(lName)

    def addEmailAddress(self,emailId):
        self.driver.find_element_by_xpath(self.addCustomer_EmailAddress_xpath).send_keys(emailId)

    def addPhoneNumber(self,phoneNumber):
        self.driver.find_element_by_xpath(self.addCustomer_PhoneN_xpath).send_keys(phoneNumber)

    def customerNextpage(self):
        self.driver.find_element_by_xpath(self.next_button_xpath).click()
        time.sleep(5)
        infraPage=self.driver.find_element_by_xpath(self.text_InfraPage_xpath).text
        print(infraPage)
        if infraPage=="Enter infrastructure details":
            print("Validation passed")
        else:
            print("Validation failed")

    def customerBackpage(self):
        self.driver.find_element_by_xpath(self.back_button_xpath).click()

    def infra_SharedOption(self):
        self.driver.find_element_by_xpath(self.plan_sharedCheckBox_xpath).click()
        #time.sleep(2)
    def infra_DedicatedOption(self):
        self.driver.find_element_by_xpath(self.plan_DediatedCheckBox_xpath).click()

    def infra_subscription_select(self):
        self.driver.find_element_by_xpath(self.sharedPlan_dropdown_xpath).send_keys(Keys.ARROW_DOWN+Keys.ENTER)
        time.sleep(3)
        # subscription=Select(self.driver.find_element_by_xpath(self.sharedPlan_dropdown_xpath))
        # subscription.select_by_value(subValue)
        # time.sleep(2)

    def infra_backButton(self):
        self.driver.find_element_by_xpath(self.plan_back_button).click()
        time.sleep(5)

    def infra_nextButton(self):
        self.driver.find_element_by_xpath(self.plan_next_button).click()
        time.sleep(5)
        addDesktopText=self.driver.find_element_by_xpath(self.text_addDesktop_xpath).text
        print(addDesktopText)
        if addDesktopText=="Add desktops":
            print("Validation Pass")
        else:
            print("validation failed")
            assert False

    def desktopSelection_pooled(self):
        self.driver.find_element_by_xpath(self.desktop_pooledButton_xpath).click()
    def desktopSelection_personal(self):
        self.driver.find_element_by_xpath(self.desktop_PersonalButton_xpath).click()
    def powerdesktop_personalInc(self,increaseValue):
        a=1
        while a <= increaseValue:
            self.driver.find_element_by_xpath(self.powerdesktop_plus_button).click()
            #time.sleep(1)
            a=a+1

    def powerdesktop_personalDesc(self,decreaseValue):
        self.driver.find_element_by_xpath(self.powerdesktop_minus_button).click()

    def multiDesktop_Inc(self,incValue):
        a = 1
        while a <= incValue:
            self.driver.find_element_by_xpath(self.multiDesktop_plusButton_xpath).click()
            # time.sleep(1)
            a = a + 1
    def multiDesktop_Desc(self,decreaseValue):
        self.driver.find_element_by_xpath(self.multiDesktop_minusButton_xpath).click()

    def lightdesktop_pooledInc(self,incrValue):
        b=1
        while b <= incrValue:
            self.driver.find_element_by_xpath(self.lightDesktop_plusbutton_xpath).click()
            b=b+1

    def lightdesktop_pooledDesc(self,decreaseValue):
        self.driver.find_element_by_xpath(self.lightDesktop_minusbutton_xpath).click()

    def mediumdesktop_pooledInc(self,incrValue):
        b=1
        while b <= incrValue:
            self.driver.find_element_by_xpath(self.mediumDesktop_plusbutton_xpath).click()
            b=b+1

    def mediumdesktop_personalDesc(self,decreaseValue):
        self.driver.find_element_by_xpath(self.mediumDesktop_minusbutton_xpath).click()

    def heavydesktop_pooledInc(self,incrValue):
        b=1
        while b <= incrValue:
            self.driver.find_element_by_xpath(self.heavyDesktop_plusButton_xpath).click()
            b=b+1

    def heavydesktop_personalDesc(self,decreaseValue):
        self.driver.find_element_by_xpath(self.heavyDesktop_minusButton_xpath).click()



    def customDesktop_Inc(self,incValue):
        a = 1
        while a <= incValue:
            self.driver.find_element_by_xpath(self.cDesktop_plus_button).click()
            # time.sleep(1)
            a = a + 1
    def customDesktop_Desc(self,decreaseValue):
        self.driver.find_element_by_xpath(self.cDesktop_minus_button).click()

    def desktop_BackButton(self):
        self.driver.find_element_by_xpath(self.desktop_backButton_xpath).click()

    def desktop_NextButton(self):
        self.driver.find_element_by_xpath(self.desktop_nextButton_xpath).click()
        time.sleep(5)

    def addOns_BackFile(self):
        self.driver.find_element_by_xpath(self.backUp_filesetup_xpath).click()

    def addOns_Firewall(self):
        self.driver.find_element_by_xpath(self.firewall_setup_xpath).click()

    def addOns_BackButton(self):
        self.driver.find_element_by_xpath(self.addOns_back_button).click()
    def addOns_NextButton(self):
        self.driver.find_element_by_xpath(self.addOns_next_button).click()
        time.sleep(5)

    def reviewPage_backButton(self):
        self.driver.find_element_by_xpath(self.reviewPage_back_button).click()
    def reviewPage_AddCustomerButton(self):
        self.driver.find_element_by_xpath(self.submit_button_xpath).click()









