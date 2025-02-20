from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

# Set an Implicit Wait (applies to all elements globally)
driver.implicitly_wait(5)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# Explicit Wait setup
wait = WebDriverWait(driver, 10)
username = driver.find_element(By.NAME, "username")
username.send_keys("Admin")

password = driver.find_element(By.NAME, "password")
password.send_keys("admin123")

login_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "oxd-button")))
login_button.click()

button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "oxd-glass-button")))

print("Login successful!")
driver.quit()
