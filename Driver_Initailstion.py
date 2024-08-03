
def setup():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.service import Service as chromeservice
    driver = webdriver.Chrome(service=chromeservice(ChromeDriverManager().install()))
    driver.maximize_window()
    return driver