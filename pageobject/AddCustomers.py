from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys


class customerPage:
    customer_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    customer_list_xpath = "//li[@class='nav-item has-treeview menu-open']//ul//li[1]"
    button_addnew_xpath = "//a[@class='btn btn-primary']"
    txt_email_xpath = "//input[@id='Email']"
    txt_password_xpath = "//input[@id='Password']"
    txt_firstname_xpath = "//input[@id='FirstName']"
    txt_lastname_xpath = "//input[@id='LastName']"
    button_GenderMale_xpath = "//label[contains(text(),'Male')]"
    button_GenderFemale_xpath = "//label[contains(text(),'Female')]"
    txtDOB_xpath = "//input[@name='DateOfBirth']"
    txt_companyNm_xpath = "//input[@id='Company']"
    selTaxExe_xpath = "//input[@id='IsTaxExempt']"
    listNewletter_xpath = "//div[@class='k-widget k-multiselect k-multiselect-clearable']"
    lisTxt_TestStore_xpath = "//li[contains(text(),'Test store 2')]"
    lisTxt_YourStoreNm_xpath = "//li[contains(text(),'Your store name')]"
    selTxt_CustomerRole_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
    listTxt_Guest_xpath = "//li[contains(text(),'Guests')]"
    lisTxt_registered_xpath = "//li[contains(text(),'Registered')]"
    lisTxt_Administartor_xpath = "//li[contains(text(),'Administrators')]"
    lisTxt_Vendors_xpath = "//li[contains(text(),'Vendors')]"
    lisTxt_ForumMod_xpath = "//li[contains(text(),'Forum Moderators')]"
    selVendor_xpath = "//select[@id='VendorId']"
    button_save = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickonCustomerMenu(self):
        self.driver.find_element_by_xpath(self.customer_menu_xpath).click()

    def clickonCustomerList(self):
        self.driver.find_element_by_xpath(self.customer_list_xpath).click()

    def clickOnAddCust(self):
        self.driver.find_element_by_xpath(self.button_addnew_xpath).click()

    def enterEmailId(self, emailid):
        self.driver.find_element_by_xpath(self.txt_email_xpath).send_keys(emailid)

    def enterPassword(self, password):
        self.driver.find_element_by_xpath(self.txt_password_xpath).send_keys(password)

    def enterFirstName(self, FirstName):
        self.driver.find_element_by_xpath(self.txt_firstname_xpath).send_keys(FirstName)

    def enterLastName(self, LastName):
        self.driver.find_element_by_xpath(self.txt_lastname_xpath).send_keys(LastName)

    def SelGender(self, gender):
        if gender == "Male":
            self.driver.find_element_by_xpath(self.button_GenderMale_xpath).click()
        elif gender == "Female":
            self.driver.find_element_by_xpath(self.button_GenderFemale_xpath).click()
        else:
            self.driver.find_element_by_xpath(self.button_GenderMale_xpath).click()

    def dateOfBirth(self, DOB):
        self.driver.find_element_by_xpath(self.txtDOB_xpath).send_keys(DOB)

    def companyName(self, companyName):
        self.driver.find_element_by_xpath(self.txt_companyNm_xpath).send_keys(companyName)

    def selNewsletter(self, vendor):
        self.driver.find_element_by_xpath(self.listNewletter_xpath).click()
        time.sleep(5)
        if vendor == "Test":
            self.listclick = self.driver.find_element_by_xpath(self.lisTxt_TestStore_xpath)
        elif vendor == "Your":
            self.listclick = self.driver.find_element_by_xpath(self.lisTxt_YourStoreNm_xpath)
        else:
            self.listclick = self.driver.find_element_by_xpath(self.lisTxt_TestStore_xpath)
        time.sleep(3)
        # self.listclick.click();
        self.driver.execute_script("arguments[0].click();", self.listclick)

    def selCustomerRole(self, role):
        self.driver.find_element_by_xpath(self.selTxt_CustomerRole_xpath).click()
        #self.driver.find_element_by_xpath(self.selTxt_CustomerRole_xpath).clear()
        time.sleep(5)
        if role == "Guests":
            self.listkey = self.driver.find_element_by_xpath(self.listTxt_Guest_xpath)
        elif role == "Registered":
            self.listkey = self.driver.find_element_by_xpath(self.lisTxt_registered_xpath)
        elif role == "Forum":
            self.listkey = self.driver.find_element_by_xpath(self.lisTxt_ForumMod_xpath)
        elif role == "vendors":
            self.listkey = self.driver.find_element_by_xpath(self.lisTxt_Vendors_xpath)
        elif role == "admini":
            self.listkey = self.driver.find_element_by_xpath(self.lisTxt_Administartor_xpath)
        else:
            self.listkey = self.driver.find_element_by_xpath(self.lisTxt_Administartor_xpath)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.listkey)

    def selManageOfVendor(self, vendor):
        selectDropdown = Select(self.driver.find_element_by_xpath(self.selVendor_xpath))
        selectDropdown.select_by_visible_text(vendor)

    def saveButton(self):
        self.driver.find_element_by_xpath(self.button_save).click()
