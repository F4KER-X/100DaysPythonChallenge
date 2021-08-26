from selenium import webdriver
from time import sleep
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

# launch chrome
chrome_driver_path = "C:\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://www.tinder.com")
driver.maximize_window()

# accept cookies
sleep(2)
i_accept_button = driver.find_element_by_xpath('//*[@id="t812761606"]/div/div[2]/div/div/div[1]/button')
i_accept_button.click()

# click on login-tinder
sleep(2)
login_button = driver.find_element_by_xpath(
    '//*[@id="t812761606"]/div/div[1]/div/main/div[1]/div/div/div/div/div[3]/div/div[2]/button')
login_button.click()

# choose FB and change window
sleep(2)
fb_button = driver.find_element_by_xpath('//*[@id="t-915619470"]/div/div/div[1]/div/div[3]/span/div[2]/button/span[2]')
fb_button.click()
windows = driver.window_handles
main = windows[0]
fb = windows[1]
driver.switch_to.window(fb)

# enter FB info and login
sleep(2)
email = driver.find_element_by_xpath('//*[@id="email"]')
email.send_keys("dannypython1@gmail.com")

password = driver.find_element_by_xpath('//*[@id="pass"]')
password.send_keys("642819375")
fb_login = driver.find_element_by_xpath('//*[@id="loginbutton"]')
fb_login.click()

# switch back to main tab and some buttons to click in order to work with tinder
sleep(2)
driver.switch_to.window(main)
sleep(2)
allow_button = driver.find_element_by_xpath('//*[@id="t-915619470"]/div/div/div/div/div[3]/button[1]/span')
allow_button.click()
sleep(2)
not_interested_button = driver.find_element_by_xpath('//*[@id="t-915619470"]/div/div/div/div/div[3]/button[2]/span')
not_interested_button.click()

# first x has different xpath than the n X.
sleep(2)
x_button = driver.find_element_by_xpath(
    '//*[@id="t812761606"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button')
x_button.click()

while True:
    try:
        print("clicked X")
        sleep(5)
        x_button = driver.find_element_by_xpath(
            '//*[@id="t812761606"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[2]/button')
        x_button.click()

    except ElementClickInterceptedException:
        print("X not found/Hidden")
        try:
            # only if it asks you to add tinder to your notifications.
            sleep(2)
            back_button = driver.find_element_by_xpath('//*[@id="t-915619470"]/div/div/div[2]/button[2]')
            back_button.click()
        except NoSuchElementException:
            print("X not found 2")
            sleep(4)
