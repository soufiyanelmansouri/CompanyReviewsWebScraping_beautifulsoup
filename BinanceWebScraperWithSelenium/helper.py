from selenium import webdriver
from selenium.webdriver.common.by import By


def accept_terms():
    driver.implicitly_wait(10)
    while True:
        try:
            element = driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
            print(element.text)
            element.click()
            break
        except:
            pass
        
PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

