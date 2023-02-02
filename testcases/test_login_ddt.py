import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import Loginpage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import Xlutils

class Test_002_DDT_Login:
    baseurl = ReadConfig.getApplicationURL()
    path = ".//TestData/commerce login.xlsx"

    logger = LogGen.loggen()

    @pytest.mark.regression

    def test_login_ddt(self , setup):
        self.logger.info("********* Test_002_DDT_login *********")
        self.logger.info("***************** verifying Login test *************")
        self.driver = setup
        self.driver.get(self.baseurl)

        self.lp = Loginpage(self.driver)
        self.rows = Xlutils.getRowcount(self.path,"Sheet1")
        print("no of rows:",self.baseurl)


        list_status = []                    # empty list variable

        for r in range(2,self.rows+1):
            self.user = Xlutils.readData(self.path,'Sheet1',r,1)
            self.password = Xlutils.readData(self.path,'Sheet1',r,2)
            self.exp = Xlutils.readData(self.path,'Sheet1',r,3)
            self.lp.setusername(self.user)
            self.lp.setpassword(self.password)
            self.lp.clicklogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == 'pass':
                    self.logger.info('**pass**')
                    self.lp.clicklogout()
                    list_status.append('pass')
                elif self.exp == 'fail':
                     self.logger.info('***failed***')
                     list_status.append('fail')
            elif act_title != exp_title:
                 if self.exp == 'pass':
                     self.logger.info('***failed***')
                     list_status.append('fail')
                 elif self.exp == 'fail':
                     self.logger.info('*****passed****')
                     list_status.append('pass')

        if 'fail' not in list_status:
            self.logger.info('Login DDT test passed')
            self.driver.close()
            assert True
        else:
            self.logger.info('*******Login DDT test Failed********')
            self.driver.close()
            assert False