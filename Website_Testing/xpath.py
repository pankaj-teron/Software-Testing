from selenium import webdriver
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.get("https://row.gymshark.com/pages/shop-men")
driver.maximize_window()
time.sleep(1)
# driver.find_element(By.CSS_SELECTOR, ".slick-active a")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, ".header_mobile-header-search__AfHPq > .search_search-trigger__U6dOW")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, ".header_mobile-header-search__AfHPq > .search_search-trigger__U6dOW").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "body")
time.sleep(1)
driver.find_element(By.ID, "gymshark-header-search-search-enter").send_keys("running")
time.sleep(2)
driver.find_element(By.ID, "gymshark-header-search-search-enter").send_keys(Keys.ENTER)
time.sleep(2)
driver.find_element(By.CLASS_NAME, "product-card_product-title-link__jDI6f").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, ".add-to-cart_section__GygMh:nth-child(5) .size_size__saJiQ:nth-child(5)").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, ".add-to-cart_button-container__aKAUo:nth-child(6) .button_success-overlay__aqLb7").click()
time.sleep(4)

# click on discount input
driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div[2]/div[3]/div/div[4]/div/div/fieldset/input").click()
time.sleep(2)
driver.find_element(By.CLASS_NAME, "input_input__iz_H4").send_keys("PROMO")
time.sleep(2)


driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div[2]/div[3]/div/div[4]/div/div/button/span[2]").click()
time.sleep(2)


print("\nOrder Placed Successfully")
print("\nCompleted\t Exercise: 23.Selenium web driver - Locating web element - xpath - Webpage")
driver.quit()
