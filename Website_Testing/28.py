
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get("http://localhost/shopping/shopping/")
driver.maximize_window()
time.sleep(3)

wait = WebDriverWait(driver, 10)
product_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name=product]")))
product_input.send_keys("Book")
time.sleep(3)
print("Entered 'Book' in the product input field.")


search_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name=search]")))
search_button.click()
time.sleep(3)
print("Clicked the search button.")
time.sleep(2)

print("\nCompleted\tExercise: 28. Wait Commands")
driver.quit()