from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("http://localhost/shopping/shopping/")
time.sleep(3)

element = driver.find_element(By.XPATH, "/html/body/header/div[2]/div/div/div[1]/div/a")
print("Element text:", element.text)

print("Element href attribute:", element.get_attribute("href"))

print("\nCompleted\t Exercise: 27. Difference between text and get_attribute")
driver.quit()