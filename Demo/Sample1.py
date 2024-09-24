import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

print("sample test case started")
driver = webdriver.Chrome()
#driver=webdriver.Firefox()
# driver=webdriver.ie()
# maximize the window size
driver.maximize_window()
# navigate to the url
driver.get("https://www.google.com/")
time.sleep(3)
# identify the Google search text box and enter the value
driver.find_element(By.NAME, "q").send_keys("Mennonite new life center")
time.sleep(3)
# click on the Google search button
driver.find_element(By.NAME,"btnK").send_keys(Keys.ENTER)
time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='rso']/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a").click()
time.sleep(3)
# close the browser
driver.close()
print("sample test case successfully completed")