from selenium import webdriver
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.get("http://localhost/shopping/shopping/")
driver.maximize_window()
time.sleep(1) #Class Selector
driver.find_element(By.CSS_SELECTOR, "a .fa-sign-in").click()
time.sleep(3) #ID Selector
driver.find_element(By.CSS_SELECTOR, '#exampleInputEmail1').send_keys("johndeo@gmail.com")
time.sleep(2) # Attribute Selector
driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys("Test@123")

time.sleep(2) # Combinator Selector
driver.find_element(By.CSS_SELECTOR, 'form button[name="login"]').click()
driver.find_element(By.LINK_TEXT, "Shopping Portal").click()
time.sleep(2)
print("Login Successful\n")

print("Completed\t Exercise: 20. Selenium Web driver - Locating web element - CSSSelector - Application")
driver.quit()