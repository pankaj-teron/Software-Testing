
from selenium import webdriver
from time import sleep

import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.get("http://localhost/shopping/shopping/")
driver.maximize_window()
sleep(1)

driver.find_element(By.CLASS_NAME, "search-field").click()
time.sleep(1)
driver.find_element(By.CLASS_NAME, "search-field").send_keys("Shoes")
sleep(2)
driver.find_element(By.CLASS_NAME, "search-field").send_keys(Keys.ENTER)
sleep(2)

element_by_tag_name = driver.find_element(By.TAG_NAME, "p")
print("\nElement found by Tag Name\n")

print("Completed\t Exercise: 18. Selenium Web driver – Locating web element – class name and tag name – Application")
driver.quit()
