import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class AddCustomer:
    lnkCustomer_menu_Xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a/p"
    lnkCustomer_menuitem_Xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p"
    btnAddnew_Xpath = "/html/body/div[3]/div[1]/form[1]/div/div/a"
    txtEmail_Xpath = "//*[@id='Email']"
    txtPassword_Xpath = "//*[@id='Password']"
    txtFirstName_Xpath = "//*[@id='FirstName']"
    txtLastName_Xpath ="//*[@id='LastName']"
    rdMaleGender_id="Gender_Male"
    rdFemale_id = "Gender_Female"
    txtDob_Xpath = "//*[@id='DateOfBirth']"
    txtCompanyName_xpath ="//*[@id='Company']"
    btnTax_Xpath= "//*[@id='IsTaxExempt']"
    txtNewsLetter = "//*[@id='customer-info']/div[2]/div[9]/div[2]/div/div[1]/div/div"
    lstitemYourstore_Xpath = "//*[@id='SelectedNewsletterSubscriptionStoreIds_listbox']/li[1]"
    lstitemTestStore_Xpath = "//*[@id='SelectedNewsletterSubscriptionStoreIds_listbox']/li[2]"
    txtCustomerRoles_Xpath ="//*[@id='customer-info']/div[2]/div[10]/div[2]/div/div[1]/div/div"
    lstitemAdministrators_Xpath = "//*[@id='SelectedCustomerRoleIds_listbox']/li[1]"
    lstitemForumModrators_Xpath ="//*[@id='SelectedCustomerRoleIds_listbox']/li[2]"
    lstitemGuest_Xpath = "//*[@id='SelectedCustomerRoleIds_listbox']/li[3]"
    lstitemRegestered_Xpath = "//*[@id='SelectedCustomerRoleIds_listbox']/li[4]"
    lstitemVendor_Xpath = "//*[@id='SelectedCustomerRoleIds_listbox']/li[5]"
    drpmrofVendor_Xpath ="//*[@id='VendorId']"
    txtAdminComment_Xpath ="//*[@id='AdminComment']"
    btnSave_Xpath ="/html/body/div[3]/div[1]/form/div[1]/div/button[1]"

    def __init__(self , driver):
        self.driver = driver

    def ClickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH,self.lnkCustomer_menu_Xpath).click()

    def ClickOnCustomersMenuitem(self):
        self.driver.find_element(By.XPATH,self.lnkCustomer_menuitem_Xpath).click()

    def ClickOnAddNewbtn(self):
        self.driver.find_element(By.XPATH,self.btnAddnew_Xpath).click()

    def SetEmail(self,email):
        self.driver.find_element(By.XPATH,self.txtEmail_Xpath).send_keys(email)

    def Setpassword(self,password):
        self.driver.find_element(By.XPATH,self.txtPassword_Xpath).send_keys(password)

    def SetFirstName(self,fname):
        self.driver.find_element(By.XPATH,self.txtFirstName_Xpath).send_keys(fname)

    def SetLastName(self,lname):
        self.driver.find_element(By.XPATH,self.txtLastName_Xpath).send_keys(lname)

    def SetGender(self,gender):
        if gender == "male":
            self.driver.find_element(By.ID,self.rdMaleGender_id).click()
        elif gender == "female":
            self.driver.find_element(By.ID,self.rdFemale_id).click()
        else:
            self.driver.find_element(By.ID,self.rdMaleGender_id).click()      # as defult

    def SetDob(self,dob):
        self.driver.find_element(By.XPATH,self.txtDob_Xpath).send_keys(dob)

    def SetCompanyName(self,comname):
        self.driver.find_element(By.XPATH,self.txtCompanyName_xpath).send_keys(comname)

    def ClickOnTaxbtn(self):
        self.driver.find_element(By.XPATH,self.btnTax_Xpath).click()

    def SetNewsLetter(self,NewsLetter):
        self.driver.find_element(By.XPATH,self.txtNewsLetter).click()
        time.sleep(3)
        if NewsLetter == "your store name":
            self.value = self.driver.find_element(By.XPATH,self.lstitemYourstore_Xpath)
        elif NewsLetter == "Test store 2":
            self.value = self.driver.find_element(By.XPATH,self.lstitemTestStore_Xpath)
        else:
            self.value = self.driver.find_element(By.XPATH,self.lstitemYourstore_Xpath)       # as defult
            time.sleep(3)
            # self.value.click()
            #self.driver.execute_script("arguments[0].click():", self.value)
            ActionChains(self.driver).click(self.value)
            

    def SetCustomerRole(self, Role):
            self.driver.find_element(By.XPATH  , self.txtCustomerRoles_Xpath).click()
            time.sleep(3)
            if Role == "Administrators":
                self.lstitem = self.driver.find_element(By.XPATH , self.lstitemAdministrators_Xpath)
            elif Role == "Registered":
                self.lstitem = self.driver.find_element(By.XPATH , self.lstitemRegestered_Xpath)
            elif Role == "Guests":
                # here user can be Registered (or)Guest only one
                time.sleep(3)
                self.driver.find_element(By.XPATH , "//*[@id='SelectedCustomerRoleIds_taglist']/li/span[1]").click()   # to clear already selected one
                self.lstitem = self.driver.find_element(By.XPATH , self.lstitemGuest_Xpath)
            elif Role == "Vendor":
                self.lstitem = self.driver.find_element(By.XPATH,self.lstitemVendor_Xpath)

            else:
                self.lstitem = self.driver.find_element(By.XPATH,self.lstitemGuest_Xpath)     #defult value
                time.sleep(3)

            #self.lstitem.click()
            #self.driver.execute_script("arguments[0].click():", self.lstitem)     # to keep the defult first value in drp down
            ActionChains(self.driver).click(self.lstitem)

    def SetMangerOfVendor(self , value):
        drp = Select(self.driver.find_element(By.XPATH , self.drpmrofVendor_Xpath))
        drp.select_by_visible_text(value)


    def SetAdmincontent(self,content):
        self.driver.find_element(By.XPATH,self.txtAdminComment_Xpath).send_keys(content)

    def ClickOnSave(self):
        self.driver.find_element(By.XPATH,self.btnSave_Xpath).click()

