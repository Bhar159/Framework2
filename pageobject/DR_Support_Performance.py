from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import selenium

class DRSupport:
    mainButton_Support_xpath="//span[contains(text(),'Support')]"
    tab_raiseticket_xpath="//div[@class='mat-tab-list']/div/div[3]"
    tab_myTicket_xpath="//div[@class='mat-tab-list']/div/div[1]"
    tab_customer_xpath="//div[@class='mat-tab-list']/div/div[2]"
    cr_dropDown_Affected_xpath="//div[@class='col-12']/select"
    cr_textbox_title_xpath="//div[@class='col-12']/input"
    cr_textbox_description_xpath="//div[@class='col-12']/textarea"
    cr_fileattach_xpath="//input[@id='fileAttachment']"
    cr_button_submit_xpath="//button[contains(text(),'Submit')]"
    cus_incident_ticket_xpath="//div[@class='col-12 ng-star-inserted']//table/tbody/tr[1]/td[1]"
    cus_inc_number_xpath="//span[contains(text(),'INC02092021M35540001')]"
    cus_inc_createdDate_xpath="//div[@class='ml-3 ng-star-inserted']/span"
    cus_inc_title_xpath="//div[@class='p-2 col ng-star-inserted']/div/b"
    cus_inc_Enhance_xpath="//div[@class='p-2 col ng-star-inserted']/div[2]"
    cus_select_Status_xpath="//div[@class='col-sm-8']/select"
    cus_textbox_remark_xpath="//div[@class='form-group']/div/textarea"
    cus_attachfile_icon_xpath="//div[@class='form-group col ng-star-inserted']/div/button"
    cus_button_savechanges_xpath="//div[@class='sub-action py-4 pull-right']/button[1]/span"
    cus_button_cancel_xpath="//div[@class='sub-action py-4 pull-right']/button[2]/span"
    myt_Inc_ticket_xpath="//div[@class='col-12 ng-star-inserted']/div/table/tbody/tr[1]/td[1]"
    myt_NoTicket_rasied_xpath="//label[contains(text(),'No Tickets Raised')]"
    myt_Inc_Number_xpath="//b[contains(text(),'INC13072021M12000002')]"
    myt_Inc_CreatedDate_Xpath="//div[@class='ml-3 ng-star-inserted']/span"
    myt_Inc_Title_Xpath="//div[@class='p-2 col ng-star-inserted']/div/b"
    myt_Inc_Enhance_xpath = "//div[@class='p-2 col ng-star-inserted']/div[2]"
    myt_select_Status_xpath = "//div[@class='col-sm-8']/select"
    myt_textbox_remark_xpath = "//div[@class='form-group']/div/textarea"
    myt_attachfile_icon_xpath = "//div[@class='form-group col ng-star-inserted']/div/button"
    myt_button_savechanges_xpath = "//div[@class='sub-action py-4 pull-right']/button[1]/span"
    myt_button_cancel_xpath = "//div[@class='sub-action py-4 pull-right']/button[2]/span"
    myt_statusChange_xpath="//div[@class='col-12 ng-star-inserted']/div/table/tbody/tr/td[5]/span"

    def __init__(self,driver):
        self.driver=driver

    def drSupportTab(self):
        self.driver.find_element_by_xpath(self.mainButton_Support_xpath).click()
        time.sleep(5)
        print(self.driver.title)
        self.driver.get_screenshot_as_file("C:/Users/bhara/PycharmProjects/Framework/Screenshots/Supportticket.png")

    def drCreateSPTicket(self,selectDropdown):
        self.driver.find_element_by_xpath(self.tab_raiseticket_xpath).click()
        time.sleep(5)
        select_Dropdown=Select(self.driver.find_element_by_xpath(self.cr_dropDown_Affected_xpath))
        select_Dropdown.select_by_index(selectDropdown)

    def drCrTitle(self,title):
        self.driver.find_element_by_xpath(self.cr_textbox_title_xpath).send_keys(title)

    def drCrDescription(self,description):
        self.driver.find_element_by_xpath(self.cr_textbox_description_xpath).send_keys(description)

    def drCrUploadFile(self,upload):
        self.driver.find_element_by_xpath(self.cr_fileattach_xpath).send_keys(upload)

    def drCrSubmit(self):
        self.driver.find_element_by_xpath(self.cr_button_submit_xpath).click()
        time.sleep(5)
        self.driver.get_screenshot_as_file("C:/Users/bhara/PycharmProjects/Framework/Screenshots/CompleteTicket.png")

    # def drCustomerTab(self):
    #     self.driver.find_element_by_xpath(self.tab_customer_xpath).click()
    #     time.sleep(5)
    #     self.driver.find_element_by_xpath(self.cus_incident_ticket_xpath).click()
    #
    # def drCusIncCheck(self,dropDownstatus,remark):
    #     incNumber=self.driver.find_element_by_xpath(self.cus_inc_number_xpath).text
    #     print(incNumber)
    #     incDate=self.driver.find_element_by_xpath(self.cus_inc_createdDate_xpath).text
    #     print(incDate)
    #     incEnhance=self.driver.find_element_by_xpath(self.cus_inc_Enhance_xpath).text
    #     print(incEnhance)
    #     selectStatus=Select(self.driver.find_element_by_xpath(self.cus_select_Status_xpath))
    #     selectStatus.select_by_index(dropDownstatus)
    #     self.driver.find_element_by_xpath(self.cus_attachfile_icon_xpath).click()
    #     self.driver.find_element_by_xpath(self.cus_textbox_remark_xpath).send_keys(remark)
    #
    # def drCusTicketCancel(self):
    #     self.driver.find_element_by_xpath(self.cus_button_cancel_xpath).click()
    #
    # def drCusTicketSave(self):
    #     self.driver.find_element_by_xpath(self.cus_button_savechanges_xpath).click()
    #
    # def drmyTicketTab(self):
    #     self.driver.find_element_by_xpath(self.tab_myTicket_xpath).click()
    #     time.sleep(5)
    #     noticketraised=self.driver.find_element_by_xpath(self.myt_NoTicket_rasied_xpath)
    #     if (noticketraised.is_displayed):
    #         print(noticketraised)
    #         return True
    #     else:
    #         self.driver.find_element_by_xpath(self.myt_Inc_ticket_xpath).click()
    #         return False
    # def drMyTicketIncCheck(self,dropDownstatus,remark):
    #     incNumber=self.driver.find_element_by_xpath(self.myt_Inc_Number_xpath).text
    #     print(incNumber)
    #     incDate=self.driver.find_element_by_xpath(self.myt_Inc_CreatedDate_Xpath).text
    #     print(incDate)
    #     incEnhance=self.driver.find_element_by_xpath(self.myt_Inc_Enhance_xpath).text
    #     print(incEnhance)
    #     selectStatus=Select(self.driver.find_element_by_xpath(self.myt_select_Status_xpath))
    #     selectStatus.select_by_value(dropDownstatus)
    #     time.sleep(5)
    #     self.driver.find_element_by_xpath(self.myt_attachfile_icon_xpath).click()
    #     self.driver.find_element_by_xpath(self.myt_textbox_remark_xpath).send_keys(remark)
    #
    # def drMyTicketCancel(self):
    #     self.driver.find_element_by_xpath(self.myt_button_cancel_xpath).click()
    #
    # def drMyTicketSave_Reopen(self):
    #     self.driver.find_element_by_xpath(self.myt_button_savechanges_xpath).click()
    #     time.sleep(5)
    #     status_Code=self.driver.find_element_by_xpath(self.myt_statusChange_xpath).text
    #     if status_Code=="Reopen":
    #         print("Ticket has been Reponed")
    #     else:
    #         print("Issue with the ticket closing")
    #         assert False
    #
    # def drMyTicketSave_Closed(self):
    #     self.driver.find_element_by_xpath(self.myt_button_savechanges_xpath).click()
    #     time.sleep(5)
    #     status_Code=self.driver.find_element_by_xpath(self.myt_statusChange_xpath).text
    #     if status_Code=="Closed":
    #         print("Ticket has been closed")
    #     else:
    #         print("Issue with the ticket closing")
    #         assert False
    #
    #
    #







