from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import selenium


class DRManageDesktop:
    # Customer button
    customerMenu_button_xapth = "//span[contains(text(),'Customers')]"
    # customerlist
    customerlist_Name_xpath = "//div[@class='col']/div[4]/div/div/table/tbody/tr/td[2]"

    #user
    desktopbutton_xpath = "//div[@class='mx-n4 ng-star-inserted']/div/div/button"
    userAlloptions_xpath="//div[@class='mx-n4 ng-star-inserted']/div/div/button/span"
    userButton_xpath="//button[@id='usersButton']"
    userCreate_single_xpath="//div[@class='mx-n4 ng-star-inserted']/div/div[2]/div[@class='ng-star-inserted']/button[2]"
    userFirstName_xpath="//div[@class='col-md-8']/div/div[1]/div/input"
    userSecondName="//div[@class='col-md-8']/div/div[2]/div/input"
    userEmailId_xpath="//div[@class='col-md-8']/div/div[3]/div/input"
    userPhone_xapth="//div[@class='col-md-8']/div/div[4]/div/div/input"
    userCreate_button_Xpath="//div[@class='mx-n4 ng-star-inserted']/div[2]/app-customer-upsert-user/div/form/div[3]/button[2]"
    userConfirmationButton_xapth="//div[@class='p-5']/div/div[3]/div/button[1]"

    listofitems_xpath = "//div[@class='mat-menu-content']"
    desktoplist_header_xpath = "//div[@class='row px-1']/div/div/table/thead"
    dektoplist_displayed_xpath = "//div[@class='row px-1']/div/div/table/tbody"
    assignUser_ToDesktop_xpath = "//tbody/tr[1]/td[6]/div[1]/i[1]"
    add_desktopIcon_xpath = "//span[contains(text(),'+ Add more desktops')]"
    # Desktop pooled
    pooledDesktop_Icon_xpath = "//div[@class='sub-content py-4'][2]/div/div[2]/mat-tab-group/mat-tab-header/div[2]/div/div/div[1]/div"
    lightDesktop_minus_button = "//div[@class='sub-content py-4'][2]/div/div[2]/mat-tab-group/div/mat-tab-body/div/div/app-desktop-card[1]/div/div/div[2]/div/app-number-input/div/div[2]/i[1]"
    lightDesktop_plus_button = "//div[@class='sub-content py-4'][2]/div/div[2]/mat-tab-group/div/mat-tab-body/div/div/app-desktop-card[1]/div/div/div[2]/div/app-number-input/div/div[2]/i[2]"
    medDesktop_plus_btn = "//div[@class='sub-content py-4'][2]/div/div[2]/mat-tab-group/div/mat-tab-body/div/div/app-desktop-card[2]/div/div/div[2]/div/app-number-input/div/div[2]/i[2]"
    medDesktop_minus_btn = "//div[@class='sub-content py-4'][2]/div/div[2]/mat-tab-group/div/mat-tab-body/div/div/app-desktop-card[2]/div/div/div[2]/div/app-number-input/div/div[2]/i[1]"
    heavyDesktop_minus_btn = "//div[@class='sub-content py-4'][2]/div/div[2]/mat-tab-group/div/mat-tab-body/div/div/app-desktop-card[3]/div/div/div[2]/div/app-number-input/div/div[2]/i[1]"
    heavyDesktop_plus_btn = "//div[@class='sub-content py-4'][2]/div/div[2]/mat-tab-group/div/mat-tab-body/div/div/app-desktop-card[3]/div/div/div[2]/div/app-number-input/div/div[2]/i[2]"
    # Desktop personal
    personalDesktop_icon_xpath = "//div[@class='sub-content py-4'][2]/div/div[2]/mat-tab-group/mat-tab-header/div[2]/div/div/div[2]/div"
    powerDesktop_minus_btn = "//div[@class='row pt-3 p-0 m-0 ng-star-inserted']/app-desktop-card[1]/div/div/div[2]/div[1]/app-number-input/div/div[2]/i[1]"
    powerDesktop_plus_btn = "//div[@class='row pt-3 p-0 m-0 ng-star-inserted']/app-desktop-card[1]/div/div/div[2]/div[1]/app-number-input/div/div[2]/i[2]"
    multiDesktop_plus_btn = "//div[@class='row pt-3 p-0 m-0 ng-star-inserted']/app-desktop-card[2]/div/div/div[2]/div[1]/app-number-input/div/div[2]/i[2]"
    multiDesktop_minus_btn = "//div[@class='row pt-3 p-0 m-0 ng-star-inserted']/app-desktop-card[2]/div/div/div[2]/div[1]/app-number-input/div/div[2]/i[1]"
    # create desktop button
    createDesktop_button = "//span[contains(text(),'Create Desktops')]"

    # ManageDesktop
    mtablelist = "//div[@class='mt-4 ng-star-inserted']//div[@class='table-responsive']/table/tbody/tr"
    mheavyModel = "//span[contains(text(),'heavy')]"
    mlightModel = "//span[contains(text(),'light')]"
    mMediumModel = "//span[contains(text(),'medium')]"
    mMultiModel = "//span[contains(text(),'multimedia')]"
    mpowerModel = "//span[contains(text(),'power')]"

    # AssignMent:
    massignUserPlusbutton = "//div[@class='row px-1']/div/div/table/tbody/tr[1]/td[6]/div/i"
    mNofreedesktoptext = "//mat-tooltip-component//div[contains(text(),'No Free')]"
    mAssignUser = "//mat-tooltip-component//div[contains(text(),'Assign Users')]"
    mAssignUserCancelButton = "//mat-dialog-container/app-modal/div/div[2]/div/button[2]"
    mApplyChanges = "//mat-dialog-container/app-modal/div/div[2]/div/button[1]"
    mNorecordinUserText = "//td[contains(text(),'No Record')]"
    mCreateNewUsertext = "//span[contains(text(),'Create new User')]"
    multiUserAssignUnassign = "//div[@class='mx-n4 ng-star-inserted']/div[2]/app-customer-single-session-desktop/div/div[2]/div/div/table/tbody/tr[1]/td[9]/div/i"
    mAddExistingUserPlusButton = "//mat-dialog-container/app-modal/div/div/div[2]/div/table/tbody/tr[2]/td[2]/div/i"
    mUserApplyChangesButton = "//mat-dialog-container/app-modal/div/div[2]/div/button[1]"
    mUserCancelButton = "//mat-dialog-container/app-modal/div/div[2]/div/button[2]"

    def __init__(self, driver):
        self.driver = driver

    def customerMenu(self):
        self.driver.find_element_by_xpath(self.customerMenu_button_xapth).click()
        time.sleep(5)

    def customerlist(self):
        customerNameList = self.driver.find_elements_by_xpath(self.customerlist_Name_xpath)
        # colour = self.driver.find_element_by_xpath("//div[@class='col']/div[4]/div/div/table/tbody/tr[1]/td[2]")
        colour = self.driver.find_element_by_xpath("//div[@class='col']/div[4]/div/div/table/tbody/tr[1]/td[2]/div[1]")
        backgroundcolour = colour.value_of_css_property('background-color')

        for customername in customerNameList:
            print(customername.text)

        if backgroundcolour == "rgba(255, 0, 0, 0.25)":
            self.driver.find_element_by_xpath("//div[@class='col']/div[4]/div/div/table/tbody/tr[2]/td[2]").click()
            time.sleep(5)
            print("Red colour2")
        else:
            self.driver.find_element_by_xpath("//div[@class='col']/div[4]/div/div/table/tbody/tr[1]/td[2]").click()
            time.sleep(5)

    def desktopIcon(self):
        self.driver.find_element_by_xpath(self.desktopbutton_xpath).click()

    def addDesktop(self):
        self.driver.find_element_by_xpath(self.add_desktopIcon_xpath).click()
        time.sleep(5)

    def pooledDesktopSelect(self):
        self.driver.find_element_by_xpath(self.pooledDesktop_Icon_xpath).click()
        time.sleep(2)

    def lightPooledInc(self, Incr):
        a = 1
        while a <= Incr:
            self.driver.find_element_by_xpath(self.lightDesktop_plus_button).click()
            a = a + 1

    def lightPooledDec(self, decrease):
        a = 1
        while a <= decrease:
            self.driver.find_element_by_xpath(self.lightDesktop_minus_button).click()
            a = a + 1

    def mediumPooledInc(self, Incr):
        a = 1
        while a <= Incr:
            self.driver.find_element_by_xpath(self.medDesktop_plus_btn).click()
            a = a + 1

    def mediumPooledDec(self, decrease):
        a = 1
        while a <= decrease:
            self.driver.find_element_by_xpath(self.medDesktop_minus_btn).click()
            a = a + 1

    def heavyPooledInc(self, Incr):
        a = 1
        while a <= Incr:
            self.driver.find_element_by_xpath(self.heavyDesktop_plus_btn).click()
            a = a + 1

    def heavyPooledDec(self, decrease):
        a = 1
        while a <= decrease:
            self.driver.find_element_by_xpath(self.heavyDesktop_minus_btn).click()
            a = a + 1

    def personalDesktopIcon(self):
        self.driver.find_element_by_xpath(self.personalDesktop_icon_xpath).click()
        time.sleep(2)

    def powerPersonalInc(self, Incr):
        a = 1
        while a <= Incr:
            self.driver.find_element_by_xpath(self.powerDesktop_plus_btn).click()
            a = a + 1

    def powerPersonalDec(self, decrease):
        a = 1
        while a <= decrease:
            self.driver.find_element_by_xpath(self.powerDesktop_minus_btn).click()
            a = a + 1

    def multiPersonalInc(self, Incr):
        a = 1
        while a <= Incr:
            self.driver.find_element_by_xpath(self.multiDesktop_plus_btn).click()
            a = a + 1

    def multiPersonalDec(self, decrease):
        a = 1
        while a <= decrease:
            self.driver.find_element_by_xpath(self.multiDesktop_minus_btn).click()
            a = a + 1

    def createDesktopButton(self):
        self.driver.find_element_by_xpath(self.createDesktop_button).click()

    def userCreationallbutton(self):
        self.driver.find_element_by_xpath(self.userAlloptions_xpath).click()
        time.sleep(2)

    def userCreationIcon(self):
        self.driver.find_element_by_xpath(self.userButton_xpath).click()
        time.sleep(5)

    def userCreationNewButton(self):
        self.driver.find_element_by_xpath(self.userCreate_single_xpath).click()
        time.sleep(3)

    def userFirstName(self,FirstName):
        self.driver.find_element_by_xpath(self.userFirstName_xpath).send_keys(FirstName)

    def userLastName(self,lastName):
        self.driver.find_element_by_xpath(self.userSecondName).send_keys(lastName)

    def userEmailID(self,emailID):
        self.driver.find_element_by_xpath(self.userEmailId_xpath).send_keys(emailID)
        time.sleep(10)

    def userPhoneNumber(self,phoneNm):
        self.driver.find_element_by_xpath(self.userPhone_xapth).send_keys(phoneNm)
        time.sleep(2)

    def userCreateButton(self):
        self.driver.find_element_by_xpath(self.userCreate_button_Xpath).click()
        time.sleep(2)

    def userCOnfirmationPopUp(self):
        self.driver.find_element_by_xpath(self.userConfirmationButton_xapth).click()
        time.sleep(2)