
from selenium import webdriver
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("http://localhost/shopping/shopping/")
driver.maximize_window()
time.sleep(3)

driver.find_element(By.XPATH, "/html/body/header/div[2]/div/div/div[2]/div/form/div/input").send_keys("Phone")
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/header/div[2]/div/div/div[2]/div/form/div/button").click()
time.sleep(3)
# product.send_key(Keys.ENTER)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/a/img").click()
time.sleep(3)
driver.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/div[2]/div[1]/div[2]/div/div[6]/div/div[3]/a").click()
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[4]/table/tbody/tr/td/div/button").click()
time.sleep(3)


print("\nCompleted\t Exercise: 22. Selenium web driver - Locating web element - xpath - Application")
driver.quit()