import pytest

import time
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import Loginpage
from pageObjects.AddCustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random


class Test_003_AddCustomer:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()


    @pytest.mark.sanity
    def test_addcustomer(self,setup):

        self.logger.info("**********************Test_003_addcustomer Started*****************************")

        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = Loginpage(self.driver)                # variable
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()

        self.logger.info("**************Login success ***************")

        self.logger.info("*******starting add customer test**********")

        self.addcust = AddCustomer(self.driver)       #variable
        self.addcust.ClickOnCustomersMenu()
        self.addcust.ClickOnCustomersMenuitem()
        self.addcust.ClickOnAddNewbtn()

        self.logger.info("*********providing customer info************")

        self.email = random_generator() +'@gmail.com'
        self.addcust.SetEmail(self.email)
        self.addcust.Setpassword("test123")
        self.addcust.SetFirstName("Niharika")
        self.addcust.SetLastName("Reddy")
        self.addcust.SetGender("female")
        self.addcust.SetDob("7/12/1997")
        self.addcust.SetCompanyName("construction company")
        self.addcust.ClickOnTaxbtn()
        self.addcust.SetNewsLetter("Test store 2")
        self.addcust.SetCustomerRole("Registered")
        self.addcust.SetMangerOfVendor("Vendor 2")
        self.addcust.SetAdmincontent("This is for testing")
        self.addcust.ClickOnSave()

        self.logger.info("********** saving customer info*********")

        self.logger.info("************* Add customer validation started*****************")

        self.msg = self.driver.find_element(By.TAG_NAME,"body").text
        print(self.msg)

        if "The new customer has been added successfully." in self.msg:
            assert True == True
            self.logger.info("******************** Add customer test passed*****************")

        else:
            self.driver.save_screenshot('.\\Screenshots\\+test_addcustomer_screen.png')
            self.logger.error("********Add customer Test failed ********")
            assert True == False
            self.driver.close()
            self.logger.info("************** testcase end ****************** ")


# to generate random mail id

def random_generator(size=8,chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars)for x in range(size))


