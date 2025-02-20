
from selenium import webdriver
from time import sleep
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.get("https://row.gymshark.com/pages/shop-men")
driver.maximize_window()
time.sleep(2)

driver.find_element(By.CLASS_NAME, "header_mobile-header-search__AfHPq").click()
time.sleep(2)
driver.find_element(By.ID, "gymshark-header-search-search-enter").send_keys("running")
time.sleep(2)
driver.find_element(By.ID, "gymshark-header-search-search-enter").send_keys(Keys.ENTER)
time.sleep(3)

element_by_tag_name = driver.find_element(By.TAG_NAME, "p")
print("\nElement found by Tag Name\n\n")


print("\nCompleted\t Exercise: 19. Selenium Web driver – Locating web element – class name and tag name – Webpage\n")
driver.quit()
