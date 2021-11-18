from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import selenium

class DRVmImage:
    icon_VmImage_Xpath="//span[contains(text(),'VM Images')]"
    tab_ManageVm_xpath="//div[@class='col-12']/div/div/mat-tab-group/mat-tab-header/div[2]/div/div/div[1]/div"
    tab_AddVm_Xpath="//div[@class='col-12']/div/div/mat-tab-group/mat-tab-header/div[2]/div/div/div[2]/div"
    ad_title_AddVm_xpath="//div[contains(text(),'Fill in the form to add a new image')]"
    ad_textbox_imageName_xpath="//div[@class='col-sm-10']/input"
    ad_text_Description_xpath="//mat-tab-body/div[1]/div[2]/div[1]/div[1]/div[2]/form[1]/div[2]/div[1]/textarea[1]"
    ad_button_SharePersonal_xpath=("//div[@class='col-12 pl-0 pr-0']/div/div[1]/div[1]")
    ad_button_SharedPooled_xpath="//div[@class='col-12 pl-0 pr-0']/div/div[2]/div[1]"
    ad_click_avRegion_xpath="//div[@class='col-sm-10']/mat-select/div"
    ad_dropdown_avRegion_xpath="//body/div[4]/div[2]/div[1]/div[1]/div[1]"
    region_list="//body/div[3]/div[2]/div[1]/div[1]/div[1]/mat-option"
    ad_link_Csupport_xpath="//div[@class='field-guide col mt-3']/div/a"
    ad_select_VmInstance_xpath="//mat-tab-body/div/div[2]/div[2]/div[2]/form/div[1]/div/select"
    ad_select_ImageGal_xpath="//mat-tab-body/div/div[2]/div[2]/div[2]/form/div[2]/div/select"
    ad_button_cancel_Xpath="//mat-tab-body/div/div[2]/div[3]/div/div/button[1]"
    ad_button_AddImage_Xpath='//mat-tab-body/div/div[2]/div[3]/div/div/button[2]'
    ad_eMsg_ImageNm_Xpath="//div[contains(text(),'Image Name is required')]"
    ad_eMsg_ImageNmExisted_Xpath="//div[contains(text(),' This Image Name is already exists ')]"
    ad_eMsg_Description_Xpath="//div[contains(text(),'Image Description is required')]"
    ad_eMsg_SelectModel_xpath="//div[contains(text(),'Select any model')]"
    ad_eMsg_VmInst_Xpath="//div[contains(text(),'VM Instance is required')]"
    ad_eMsg_ImGallery_Xpath="//div[contains(text(),'Image gallery is required')]"
    mg_Icon_Personaldesk_Xpath="//div[@class='mat-tab-body-wrapper']/mat-tab-body/div/div/div/div/div/div[1]/div/span"
    mg_Icon_Pooled_Xpath="//div[@class='mat-tab-body-wrapper']/mat-tab-body/div/div/div/div/div/div[2]/div/span"
    mg_SearchButton_name_Xpath="//div[@class='mat-tab-body-wrapper']/mat-tab-body/div/div/div[2]/div/div/div/div/label"
    mg_SearchName_Type_Xpath="//input[@id='inputGroupSelect01']"
    mg_DropDown_SortBY_Xpath="//select[@id='inputGroupSelect01']"
    mg_DropDown_Update_Xpath="//label[contains(text(),'Last Updated:')]"
    mg_sort_Image_xpath="//a[contains(text(),'Image Name')]"
    mg_sort_Last_xpath="//a[contains(text(),'Last Updated')]"
    mg_modify_xpath="//span[contains(text(),'Modify')]"
    mg_delete_button_xpath="//div[@class='mat-menu-content']/button"
    

    def __init__(self,driver):
        self.driver=driver

    def clickVmIcon(self):
        self.driver.find_element_by_xpath(self.icon_VmImage_Xpath).click()
        time.sleep(5)
        pageCheck=self.driver.find_element_by_xpath(self.tab_ManageVm_xpath).text
        print(pageCheck)
        if pageCheck=="MANAGE IMAGES":
            print("Your in Vm Manage Page")
            assert True
        else:
            print("testcase got failed")
            assert False

    def clickAddImage(self):
        self.driver.find_element_by_xpath(self.tab_AddVm_Xpath).click()
        time.sleep(5)
        self.driver.get_screenshot_as_file("C:/Users/bhara/PycharmProjects/Framework/Screenshots/addNewImage.png")
        pageTitle=self.driver.find_element_by_xpath(self.ad_title_AddVm_xpath).text
        print(pageTitle)
        if pageTitle=="Fill in the form to add a new image":
            print("Your in Add Image page ")
        else:
            print("testcasefailed")
            assert False

    def enterImageName(self,imageName):
        self.driver.find_element_by_xpath(self.ad_textbox_imageName_xpath).send_keys(imageName)
        time.sleep(5)
        self.driver.find_element_by_xpath(self.ad_text_Description_xpath).click()


    def enterImDescription(self,description):
        self.driver.find_element_by_xpath(self.ad_text_Description_xpath).send_keys(description)

    def modelPooledicon(self):
        self.driver.find_element_by_xpath(self.ad_button_SharedPooled_xpath).click()

    def modelPersonalicon(self):
        self.driver.find_element_by_xpath(self.ad_button_SharePersonal_xpath).click()

    def regionSelect(self,value1,value2):
        self.driver.find_element_by_xpath(self.ad_click_avRegion_xpath).click()
        region_list = self.driver.find_element_by_xpath(self.ad_dropdown_avRegion_xpath).text
        print(region_list)
        regions = {1: 'East US', 2: 'West US 2', 3: 'Central US', 4: 'Brazil South', 5: 'South Africa North',
                   6: 'North Europe', 7: 'Germany West Central',
                   8: 'France Central', 9: 'Korea Central', 10: 'Japan East', 11: 'UAE North', 12: 'Australia East',
                   13: 'Central India', 14: 'Southeast Asia'}

        if value1 in regions:
            self.driver.find_element_by_xpath("//body/div[4]/div[2]/div[1]/div[1]/div[1]/mat-option[" + str(value1) + "]").click()
            print("Added new region 2" + regions.get(value1))
            if value2 in regions:
                self.driver.find_element_by_xpath("//body/div[4]/div[2]/div[1]/div[1]/div[1]/mat-option[" + str(value2) + "]").click()
                print("Added new region 3" + regions.get(value2))
                # if value3 in regions:
                #     self.driver.find_element_by_xpath("//body/div[4]/div[2]/div[1]/div[1]/div[1]/mat-option[" + str(value3) + "]").click()
                #     print(regions.get(value3))
                self.driver.get_screenshot_as_file("C:/Users/bhara/PycharmProjects/Framework/Screenshots/Regionselection.png")

    def vmInstance(self,value):
        dropDown=Select(self.driver.find_element_by_xpath(self.ad_select_VmInstance_xpath))
        dropDown.select_by_index(value)
        self.driver.get_screenshot_as_file("C:/Users/bhara/PycharmProjects/Framework/Screenshots/VmInstance.png")

    def imageGallery(self,value1):
        dropDown2 = Select(self.driver.find_element_by_xpath(self.ad_select_ImageGal_xpath))
        dropDown2.select_by_value(value1)
        self.driver.get_screenshot_as_file("C:/Users/bhara/PycharmProjects/Framework/Screenshots/ImageGallery.png")

    def addButton(self):
        self.driver.find_element_by_xpath(self.ad_button_AddImage_Xpath).click()
        self.driver.get_screenshot_as_file("C:/Users/bhara/PycharmProjects/Framework/Screenshots/addButton.png")

    def errorVMImage(self):
        vmImageEr=self.driver.find_element_by_xpath(self.ad_eMsg_ImageNm_Xpath)
        if (vmImageEr.is_displayed()):
            print("Error message displayed")
        else:
            print("Scenario failed")

    def errorVMDescription(self):
        vmImageDesEr=self.driver.find_element_by_xpath(self.ad_eMsg_Description_Xpath)
        if (vmImageDesEr.is_displayed()):
            print("Error message displayed")
        else:
            print("Scenario failed")

    def errorVmModels(self):
        vmImageModelsEr=self.driver.find_element_by_xpath(self.ad_eMsg_SelectModel_xpath)
        if (vmImageModelsEr.is_displayed()):
            print("Error message displayed")
        else:
            print("Scenario failed")

    def errorVmInstance(self):
        vmImageInstanceEr=self.driver.find_element_by_xpath(self.ad_eMsg_VmInst_Xpath)
        if (vmImageInstanceEr.is_displayed()):
            print("Error message displayed")
        else:
            print("Scenario failed")

    def errorVmImGallery(self):
        vmImageGalleryEr=self.driver.find_element_by_xpath(self.ad_eMsg_ImGallery_Xpath)
        if (vmImageGalleryEr.is_displayed()):
            print("Error message displayed")
        else:
            print("Scenario failed")














