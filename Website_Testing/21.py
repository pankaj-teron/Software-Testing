from selenium import webdriver
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.get("https://row.gymshark.com/pages/shop-men")
driver.maximize_window()
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, ".header_action-bar-item-wrap__m_Rhz .icon-user").click()
time.sleep(2) #Class Selector
driver.find_element(By.CSS_SELECTOR, "input.input.cec61d1fe.c54babdaf").click()
time.sleep(2) #ID Selector
driver.find_element(By.CSS_SELECTOR, "#username").send_keys("john@gmail.com")
time.sleep(2) #Attribute Selector
driver.find_element(By.CSS_SELECTOR, "input[id='password']").click()
time.sleep(2) #Combinators
driver.find_element(By.CSS_SELECTOR, "input[type='password'][autocomplete='current-password']").send_keys("Test!@3")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".ulp-button-icon").click()
time.sleep(2)

print("\nCompleted\t Exercise: 21. Selenium Web driver – Locating web element – CSS_Selector - Webpage \n")
print("Completed")

driver.quit()