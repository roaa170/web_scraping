from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import time

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
driver.get("https://www.google.com")
search_box = driver.find_element(By.NAME , "q")
search_box.send_keys("Open AI")
search_box.submit()
time.sleep(50)
results  = driver.find_elements(By.XPATH, '//h3')
for i , result in enumerate(results[:5],1):
    print(f'{i} {result.text}')