from selenium import webdriver
from time import sleep
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

chrome_driver_path = "C:\chromedriver.exe"
USERNAME = ""
PASSWORD = ""
SCROLL_PAUSE_TIME = 0.5


class InstaFollower:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.login()
        self.find_followers()
        self.follow()

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")

        sleep(2)
        username_file = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_file.send_keys(USERNAME)

        password_file = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_file.send_keys(PASSWORD)

        sleep(2)

        login_button = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
        login_button.click()

        sleep(4)
        not_now_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/section/main/div/div/div/div/button')
        not_now_button.click()

        sleep(8)
        try:
            notification_button = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
            notification_button.click()
        except NoSuchElementException:
            notification_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
            notification_button.click()

    def find_followers(self):
        self.driver.get('https://www.instagram.com/selenagomez/')

        followers = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        sleep(5)

        scroll = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]')

        for n in range(2):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll)
            sleep(2)

    def follow(self):
        follow_button = self.driver.find_elements_by_css_selector('li button')
        try:
            for button in follow_button:
                button.click()
                print("Button clicked")
                sleep(2)
        # some times a popup will appear to ask you if you want to unfollow
        # didn't encounter that myself. I don't have any code for it as of now
        except ElementClickInterceptedException:
            sleep(2)
