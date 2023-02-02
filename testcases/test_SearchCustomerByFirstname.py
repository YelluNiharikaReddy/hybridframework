import time
import pytest
from pageObjects.LoginPage import Loginpage
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_SearchCustomerByFirstname_005:
    baseURL = ReadConfig.getApplicationURL()
    Username = ReadConfig.getUsername()
    Password = ReadConfig.getPassword()
    Logger = LogGen.loggen()      # Logger

    @pytest.mark.regression
    def test_SerachCustomerByName(self , setup):
        self.Logger.info("*********** Search customer by first name *********************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Loginpage(self.driver)
        self.lp.setusername(self.Username)
        self.lp.setpassword(self.Password)
        self.lp.clicklogin()


        self.Logger.info("********** login sucessful ********************")

        self.addcust = AddCustomer(self.driver)
        self.addcust.ClickOnCustomersMenu()
        self.addcust.ClickOnCustomersMenuitem()
        self.Logger.info("*********** searching customer by first name **********")

        searchcust = SearchCustomer(self.driver)
        searchcust.SetFirstName("laxmikan")
        searchcust.SetLastName("Berade")
        searchcust.ClickOnSearch()
        time.sleep(5)
        status = searchcust.SearchCustomerByName("laxmikan Berade")
        assert True == status
        self.Logger.info("************ Tc_searchcustomer By fist name finished ************** ")
        self.driver.close()