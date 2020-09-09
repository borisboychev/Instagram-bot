import time
import secrets
import sys

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

        login_button = self.driver.find_element_by_xpath("//button[@type=\"submit\"]")
        login_button.click()
        time.sleep(5)

    def unfollow(self, *args):
        pass

    def follow(self, accounts):

        # Only perform action once if one user is given as an command line argument
        if len(accounts) == 1:
            self.perform_follow_action(accounts[0])
        else:
            for username in accounts:
                self.perform_follow_action(username)

        print(self.complete_message_follow())

        time.sleep(5)
        self.driver.quit()

    def perform_follow_action(self, username):
        try:
            self.driver.get(f"https://instagram.com/" + username)
        except Exception:
            raise ValueError(f"No such username found ({username})")

        follow_button = self.driver.find_element_by_css_selector('button')
        follow_button.click()
        print(f"{username} followed successfully!")


    def complete_message_follow(self):
        return f"Action complete https://www.instagram.com/" + secrets.username + "/following/ \nExiting..."


if __name__ == "__main__":
    try:
        command = sys.argv[1].strip()
        accounts = sys.argv[2:]
    except Exception:
        raise Exception("You should enter the needed arguments!")

    ig_bot = InstagramBot(secrets.password, secrets.username)

    if command == "follow":
        ig_bot.sign_in()
        ig_bot.follow([u.strip() for u in accounts])
