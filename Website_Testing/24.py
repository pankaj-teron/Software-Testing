from selenium import webdriver
driver = webdriver.Chrome()
import time

#application command
driver.get("http://localhost/shopping/shopping/")
time.sleep(3)
print("Title:", driver.title)
time.sleep(1)

current_url = driver.current_url
print("Current URL:", current_url)
time.sleep(1)

# page_source = driver.page_source
# print("Page Source:", page_source)
# time.sleep(1)


#browser command
driver.maximize_window()
time.sleep(3)
driver.minimize_window()
time.sleep(3)
driver.maximize_window()
time.sleep(3)

print("\nCompleted\t Exercise: 24.Application commands and Browser commands\n")
driver.quit()