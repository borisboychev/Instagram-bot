import time
import secrets
import sys

from selenium import webdriver

"""BEFORE RUNNING THE SCRIPT MAKE SURE YOU HAVE GIVEN YOUR CREDENTIALS IN SECRETS.PY
AND YOU HAVE GIVEN THE CORRECT PATH FOR CHROMEDRIVER.
THIS IS MY FIRST TIME WRITING SOMETHING LIKE THAT SO THERE MIGHT BE SOME BUGS

YOU RUN THE SCRIPT BY:
python main.py follow user1 user2 userN TO FOLLOW
python main.py unfollow user1 user2 userN TO UNFOLLOW
AND MAKE SURE YOU ARE IN THE InstagramBot DIR BEFORE RUNNING IT"""


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

    def unfollow(self, accounts):

        # Only perform action once if one user is given as an command line argument
        if len(accounts) == 1:
            self.perform_unfollow_action(accounts[0])
        else:
            for username in accounts:
                self.perform_unfollow_action(username)

        print(self.complete_message())

    def follow(self, accounts):

        # Only perform action once if one user is given as an command line argument
        if len(accounts) == 1:
            self.perform_follow_action(accounts[0])
        else:
            for username in accounts:
                self.perform_follow_action(username)

        print(self.complete_message())

        time.sleep(5)
        self.driver.quit()

    def perform_follow_action(self, username):
        try:
            self.driver.get(f"https://instagram.com/" + username)
        except Exception:
            raise ValueError(f"No such username found ({username})")

        follow_button = self.driver.find_element_by_css_selector('button')

        # Checks if you are not following the user you want to follow
        if follow_button.text == "Follow" or follow_button.text == "Follow Back":
            follow_button.click()
            print(f"{username} followed successfully!")

    def complete_message(self):
        return f"Action complete https://www.instagram.com/" + secrets.username + "/following/ \nExiting..."

    def perform_unfollow_action(self, username):
        try:
            self.driver.get(f"https://instagram.com/" + username)
        except Exception:
            raise ValueError(f"No such username found ({username})")

        try:
            # Following button
            follow_button = self.driver.find_elements_by_css_selector('button')

            # Checks if you are following the user you want to unfollow
            follow_button[1].click()
            confirm_button = self.driver.find_element_by_xpath("//*[text()=\"Unfollow\"]")

            if confirm_button.text == "Unfollow":
                print(confirm_button)
                confirm_button.click()
                print(f"{username} unfollowed successfully!")

        except Exception as ex:
            raise ex


if __name__ == "__main__":
    try:
        command = sys.argv[1].strip()
        accounts = sys.argv[2:]
    except Exception:
        raise Exception("You should enter the needed arguments!")

    ig_bot = InstagramBot(secrets.password, secrets.username)
    ig_bot.sign_in()

    if command == "follow":
        ig_bot.follow([u.strip() for u in accounts])

    if command == "unfollow":
        ig_bot.unfollow([u.strip() for u in accounts])
