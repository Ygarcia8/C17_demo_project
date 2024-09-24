import time
from selenium import webdriver
from selenium.webdriver.common.by import By

print("sample test case started")
driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.google.com/")

time.sleep(5)
profile_btn = driver.find_element(By.XPATH,"//span[@class='gb_Rd']/parent::a")
profile_btn.click()

time.sleep(60)
# close the browser
driver.close()
print("sample test case successfully completed")