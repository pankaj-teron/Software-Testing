from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("http://localhost/shopping/shopping/")
time.sleep(3)

element = driver.find_element(By.TAG_NAME, "a")
print("Single element found by tag name:", element.text)

elements = driver.find_elements(By.TAG_NAME, "p")
print("\n\nMultiple elements found by tag name:")
for e in elements:
    print(e.text)


print("\nCompleted\t Exercise: 26. Difference between find_element and find_elements: ")

driver.close()