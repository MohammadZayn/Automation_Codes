import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as chromeservice
from selenium.webdriver.chrome.options import Options
import time
import schedule


def update_naukri_resume():
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(service=chromeservice(ChromeDriverManager().install(), options=options))
    username = 'mohammadshaik776@gmail.com'
    password = 'Mohammad47@'
    path = os.path.abspath("C:\\Users\\local_\\OneDrive\\Documents\\Mohammad_Automation_Tester .pdf")

    try:
        # Open naukri login page
        driver.get('https://www.naukri.com/nlogin/login')
        time.sleep(5)
        driver.find_element(By.ID, 'usernameField').send_keys(username)
        driver.find_element(By.ID, 'passwordField').send_keys(password)
        driver.find_element(By.XPATH, '//button[text()="Login"]').click()
        time.sleep(5)
        driver.get('https://www.naukri.com/mnjuser/profile?id=&orgn=homepage')
        time.sleep(5)  # Wait for page to load
        # Update the resume
        driver.find_element(By.XPATH, "//input[@type='file']").send_keys(path)
        time.sleep(5)  # Wait for upload to complete

    finally:
        driver.quit()

# Schedule the job
schedule.every().day.at("08:00").do(update_naukri_resume)
schedule.every().day.at("13:00").do(update_naukri_resume)
schedule.every().day.at("17:00").do(update_naukri_resume)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)



