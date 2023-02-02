import pytest
from selenium import webdriver
from pageObjects.LoginPage import Loginpage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_HomePageTitle(self , setup):
        self.logger.info("*****************Test_homepage *************")
        self.driver = setup
        self.driver.get(self.baseurl)
        act_title = self.driver.title
        self.driver.close()
        self.logger.info("*****************verifying Homepage*************")
        if act_title == "Your store. Login":
            assert True
            self.logger.info("*****************Home page is passed *************")
        else:
            self.driver.close()
            self.logger.info("*****************Home page is failed*************")
            assert False
    @pytest.mark.sanity
    @pytest.mark.regression

    def test_login(self,setup):
        self.logger.info("*****************Test Login started*************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = Loginpage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        act_title = self.driver.title
        self.driver.close()
        self.logger.info("*****************Verifying Test login*************")
        if act_title == "Dashboard / nopCommerce administration":
            self.logger.info("*****************Test Login passed*************")
            assert True
        else:
            self.driver.get_screenshot_as_file(".\\Screenshots\\"+"test_login.png")
            self.driver.close()
            self.logger.info("*****************Test Login failed*************")
            assert False


