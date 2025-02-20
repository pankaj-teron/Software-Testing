from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("http://localhost/shopping/shopping/")
time.sleep(3)

# Conditional Commands
element = driver.find_element(By.TAG_NAME, "body")
if element.is_displayed():
    print("Element is displayed")
if element.is_enabled():
    print("Element is enabled")
if element.is_selected():
    print("Element is selected")
time.sleep(3)

# Navigation Commands
driver.get("https://row.gymshark.com/pages/shop-men")

time.sleep(3)
print("Navigated to Application")

driver.back()
time.sleep(3)
print("Navigated back")

driver.forward()
time.sleep(4)
print("Navigated forward")

driver.refresh()
time.sleep(3)
print("Page refreshed again")

print("\nCompleted\t Exercise: 25. Conditional Commands and Navigation Commands")
driver.quit()