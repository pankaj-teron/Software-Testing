from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the driver
driver = webdriver.Chrome()
driver.get("https://row.gymshark.com/pages/shop-men")
driver.maximize_window()

# Locating web elements using ID, Name, Link Text, and Partial Link Text
element_by_id = driver.find_element(By.ID, "carousel-heading")
print("Element found by ID")

element_by_name = driver.find_element(By.NAME, "description")
print("Element found by Name")

element_by_link_text = driver.find_element(By.LINK_TEXT, "Accessibility Statement")
print("Element found by Link Text")

element_by_partial_link_text = driver.find_element(By.PARTIAL_LINK_TEXT, "Statement")
print("Element found by Partial Link Text")

print("\nCompleted\t Exercise: 17. Selenium Web driver – Locating web element – id, name, link_text, partial_link_text - Webpage")
driver.quit()
