import time
import secrets

from selenium import webdriver


class InstagramBot:
    """PATH FOR CHROMEDRIVER MIGHT BE DIFFERENT"""
    __PATH = r"C:\\Program Files (x86)\\chromedriver.exe"

    def __init__(self, pw, username):
        """SETTING UP CREDS"""
        self.pw = pw
        self.username = username

        """SETTING UP WEBDRIVER"""
        self.driver = webdriver.Chrome(InstagramBot.__PATH)

    def sign_in(self):
        self.driver.get("https://www.instagram.com")
        time.sleep(2)

        """LOGIN SCREEN"""
        login_field = self.driver.find_element_by_xpath("//input[@name=\"username\"]")
        password_field = self.driver.find_element_by_xpath("//input[@name=\"password\"]")
        login_field.clear()
        password_field.clear()

        login_field.send_keys(self.username)
        password_field.send_keys(self.pw)

        self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
        time.sleep(5)

    # TODO finish unfollow method
    def unfollow(self):
        # Try to go to profile trough nav-menu
        try:
            # Profile in nav-menu
            self.driver.find_element_by_xpath(
                "//*[@id=\"react-root\"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img") \
                .click()

            # Profile button in drop down menu
            self.driver.find_element_by_xpath(
                "//*[@id=\"react-root\"]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[2]/div[2]/a[1]") \
                .click()

            # following = int(self.driver.
            #                 find_element_by_xpath(
            #     "//*[@id='react-root']/section/main/article/header/div[2]/ul/li[2]/a/span")
            # .text)
            # followers = self.driver.find_element_by_css_selector('div[role=\'dialog\'] ul')

            # print(len(followers.find_elements_by_css_selector('li')))
        except Exception as ex:
            print(str(ex))

        time.sleep(10)
        self.driver.quit()


ig = InstagramBot(secrets.password, secrets.username)

ig.sign_in()
ig.unfollow()
