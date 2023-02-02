import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class SearchCustomer:
    # add customer page
    txtEmail_id = "SearchEmail"
    txtFirstName_id = "SearchFirstName"
    txtLastName_id = "SearchLastName"
    btnSearch_id = "search-customers"
    table_Xpath = "//table[@id='customers-grid']"

    def __init__(self , driver):
        self.driver = driver

    def SetEmail(self , email):
        self.driver.find_element(By.ID , self.txtEmail_id).clear()
        self.driver.find_element(By.ID , self.txtEmail_id).send_keys(email)

    def SetFirstName(self,fname):
        self.driver.find_element(By.ID , self.txtFirstName_id).clear()
        self.driver.find_element(By.ID , self.txtFirstName_id).send_keys(fname)

    def SetLastName(self , lname):
        self.driver.find_element(By.ID , self.txtLastName_id).clear()
        self.driver.find_element(By.ID , self.txtLastName_id).send_keys(lname)

    def ClickOnSearch(self):
        self.driver.find_element(By.ID , self.btnSearch_id).click()


    def SearchCustomerByEmail(self,email):
        flag = False
        table = self.driver.find_element(By.XPATH , self.table_Xpath)
        mail = table.find_elements(By.XPATH , "//table[@id='customers-grid']/tbody/tr/td[2]")
        for r in range(len(mail)):
            emailid = mail[r].text
            if emailid == email:
                    flag = True
                    break
        return flag


    def SearchCustomerByName(self,Name):
        flag = False
        table = self.driver.find_element(By.XPATH,self.table_Xpath)
        time.sleep(5)
        fname = table.find_elements(By.XPATH , "//table[@id='customers-grid']/tbody/tr/td[3]")
        for r in range(len(fname)):
            name = fname[r].text
            if name == Name:
                flag = True
                break
        return flag


