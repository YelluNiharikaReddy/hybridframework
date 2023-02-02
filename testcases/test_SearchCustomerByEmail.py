import time
import pytest
from pageObjects.LoginPage import Loginpage
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen



class Test_SearchCustomerByEmail_004:
    baseURL = ReadConfig.getApplicationURL()
    Username = ReadConfig.getUsername()
    Password = ReadConfig.getPassword()

    logger = LogGen.loggen()   # logger
    @pytest.mark.regression
    def test_searchCustomerByEmail(self,setup):
        self.logger.info("*********** Search customer by email *****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Loginpage(self.driver)        # variable
        self.lp.setusername(self.Username)
        self.lp.setpassword(self.Password)
        self.lp.clicklogin()

        self.logger.info("****************** Login sucessfull *************")

        self.logger.info("************** starting search customer by email **********")

        self.addcust = AddCustomer(self.driver)    # variable
        self.addcust.ClickOnCustomersMenu()
        self.addcust.ClickOnCustomersMenuitem()

        self.logger.info("************** Searching customer by email ***************** ")

        searchcust = SearchCustomer(self.driver)
        searchcust.SetEmail("ArjuL@gmail.com")
        searchcust.ClickOnSearch()
        time.sleep(5)
        status = searchcust.SearchCustomerByEmail("ArjuL@gmail.com")
        assert True == status
        self.logger.info("********** tc_searchcustomer by email_004 finished *************")
        self.driver.close()

