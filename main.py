import time
import secrets

from selenium import webdriver


class InstagramBot:
    __PATH = r"C:\\Program Files (x86)\\chromedriver.exe"

    def __init__(self, pw, username):
        self.pw = pw
        self.username = username
        self.driver = webdriver.Chrome(InstagramBot.__PATH)
        self.driver.get("https://www.instagram.com")

        """"LOGIN SCREEN"""
        login_field = self.driver.find_element_by_xpath("//input[@name=\"username\"]")
        password_field = self.driver.find_element_by_xpath("//input[@name=\"password\"]")
        time.sleep(2)

    def login(self):
        self.login_field.send_keys(self.username)
        self.send_keys(self.pw)

        login_button = self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
        time.sleep(5)
        self.driver.quit()


ig = InstagramBot(secrets.password, secrets.username)

ig.login()
