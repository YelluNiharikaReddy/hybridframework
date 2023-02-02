from selenium.webdriver.common.by import By
from selenium import webdriver
class Loginpage:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_Xpath = "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button"
    link_logout_Xpath = "//*[@id='navbarText']/ul/li[3]/a"

    def __init__(self , driver):
        self.driver = driver

    def setusername(self , username):
        self.driver.find_element(By.ID , self.textbox_username_id).clear()
        self.driver.find_element(By.ID , self.textbox_username_id).send_keys("admin@yourstore.com")

    def setpassword(self , password):
        self.driver.find_element(By.ID , self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys("admin")

    def clicklogin(self):
        self.driver.find_element(By.XPATH , self.button_login_Xpath).click()

    def clicklogout(self):
        self.driver.find_element(By.XPATH , self.link_logout_Xpath).click()