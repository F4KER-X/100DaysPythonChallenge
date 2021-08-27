from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException

TWITTER_URL = "https://twitter.com"
INTERNET_SPEED_URL = "https://www.speedtest.net/"
chrome_driver_path = "C:\chromedriver.exe"
UP_SPEED = 750
DOWN_SPEED = 1000
EMAIL = ''
PASSWORD = ''


class InternetSpeedTwitterBot:
    def __init__(self):
        self.up = 0
        self.down = 0

        self.chrome_driver_path = "C:\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        # call the function to check internet speed
        self.get_internet_speed()
        # compare the speeds
        if self.up < UP_SPEED or self.down < DOWN_SPEED:
            self.tweet_at_provider()
        self.driver.quit()

    def tweet_at_provider(self):
        self.driver.get(TWITTER_URL)

        sleep(2)
        login = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/div[4]/span/span')
        login.click()

        sleep(2)
        login_email = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a/div/span/span')
        login_email.click()

        try:
            sleep(2)
            email = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
            email.send_keys(EMAIL)

            password = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
            password.send_keys(PASSWORD)

            sleep(2)

            login_button = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span/span')
            login_button.click()

            # in case twitter login uses the second option where it asks for email only first
        except NoSuchElementException:
            email = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
            email.send_keys(EMAIL)

            sleep(2)
            next_button = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div[2]/div[3]/div/div/span/span')
            sleep(2)

            password = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div[2]/div[1]/div/div[2]/div/label/div/div[2]/div/input')
            password.send_keys(PASSWORD)

            sleep(2)
            login_button = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div[2]/div[3]/div')
            login_button.click()

        sleep(2)
        message_field = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div/div/div/div')
        message_field.send_keys(
            f"@InternetProvider, why my internet is {self.down} Mbps down and {self.up} Mbps up when I pay for {DOWN_SPEED} Mbps down and {UP_SPEED} Mbps up!!")
        sleep(2)
        tweet_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        tweet_button.click()

    def get_internet_speed(self):
        self.driver.get(INTERNET_SPEED_URL)
        sleep(2)
        start_button = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        start_button.click()
        sleep(60)
        dismiss_button = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/a')
        dismiss_button.click()
        sleep(5)

        self.up = float(self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
        self.down = float(self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text)

        print(self.up)
        print(self.down)
