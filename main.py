from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import os

search_query_url = ("https://www.linkedin.com/jobs/search/?currentJobId=3834822363&f_AL=true&f_E=1%2C2&f_JT=I"
                    "&f_PP=103804675&f_TPR=r86400&f_WT=1&geoId=102454443&keywords=intern&location=Singapore"
                    "&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=R")
MY_EMAIL = os.environ["MY_EMAIL"]
MY_PASSWORD = os.environ["MY_PASSWORD"]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(search_query_url)
time.sleep(2)

# Clicks the sign-in button to fill out details:
sign_in_link = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_link.click()
time.sleep(2)

# Fills in login credentials:
email_input = driver.find_element(By.ID, "username")
email_input.send_keys(MY_EMAIL)

password_input = driver.find_element(By.ID, "password")
password_input.send_keys(MY_PASSWORD)

sign_in_button = driver.find_element(By.TAG_NAME, "button")
sign_in_button.click()
time.sleep(4.5)

# Finds the first 5 most relevant job listings and saves them:
jobs = driver.find_elements(By.CSS_SELECTOR, ".job-card-container")[:5]

for job_listing in jobs:
    time.sleep(1)
    job_listing.click()

    # Saves the job listing to your account:
    save_button = driver.find_element(By.CSS_SELECTOR, ".jobs-save-button")
    driver.execute_script("arguments[0].click();", save_button)
    time.sleep(2)

    # Follows the company who posted the job:
    follow_button = driver.find_element(By.CSS_SELECTOR, ".follow")
    # Bypasses visibility issues due to follow button not being visible:
    driver.execute_script("arguments[0].click();", follow_button)

    time.sleep(2)
