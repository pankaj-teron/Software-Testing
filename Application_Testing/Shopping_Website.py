from selenium import webdriver
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.get("http://localhost/shopping/shopping/")
driver.maximize_window()
time.sleep(4)

driver.find_element(By.XPATH, '/html/body/header/div[1]/div/div/div[1]/ul/li[4]/a').click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, 'input[name="email"]').send_keys("johndeo@gmail.com")
time.sleep(4)
driver.find_element(By.ID, "exampleInputPassword1").send_keys("Test@123")
time.sleep(4)
driver.find_element(By.CSS_SELECTOR, 'button[name="login"]').click()
driver.find_element(By.LINK_TEXT, "Shopping Portal").click()
time.sleep(4)


act_title = driver.title
print(act_title)
time.sleep(4)
exp_title = "Shopping Portal Home Page"
if act_title == exp_title:
    print("Title is Matched")
else:
    print("Title is not matched")
print("Logged in")


driver.find_element(By.XPATH, "/html/body/header/div[3]/div/div/div[2]/div/div/ul/li[2]/a").click()
time.sleep(4)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[2]/div/div/div/div/div[1]/div/div/div[1]/div/a/img").click()
time.sleep(4)
driver.find_element(By.LINK_TEXT, "ADD TO CART").click()
time.sleep(6)
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[4]/table/tbody/tr/td/div/button").click()
time.sleep(4)

print("Order Placed Successfully")
driver.quit()