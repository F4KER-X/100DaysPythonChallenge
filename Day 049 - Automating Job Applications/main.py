from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

import time

chrome_driver_path = "C:\chromedriver.exe"
URL = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(URL)
driver.maximize_window()

log_in_button = driver.find_element_by_class_name("nav__button-secondary")
log_in_button.click()

time.sleep(5)
email = driver.find_element_by_id("username")
email.send_keys("")

password = driver.find_element_by_id("password")
password.send_keys("")

sign_in_button = driver.find_element_by_css_selector("div button")
sign_in_button.click()

job_lists = driver.find_elements_by_css_selector("job-card-container--clickable")

for job in job_lists:
    job.click()
    time.sleep(5)

    try:
        apply_button = driver.find_element_by_css_selector(".jobs-apply-button")
        apply_button.click()
        time.sleep(5)
        phone = driver.find_element_by_id(
            "urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:2689985797,33219042,phoneNumber~nationalNumber)")
        if phone != "":
            phone.send_keys("1234567832")
        submit_application_button = driver.find_element_by_id("ember1196")
        if submit_application_button.get_attribute("aria-label") == "Submit application":
            submit_application_button.click()

            time.sleep(2)
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
        else:
            cancel = driver.find_elements_by_class_name("artdeco-modal__dismiss")
            cancel.click()
            discard = driver.find_element_by_name("discard_application_confirm_btn")
            discard.click()
    except NoSuchElementException:
        continue

time.sleep(5)
driver.quit()