import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

print("sample test case started")
driver = webdriver.Chrome()
#driver=webdriver.Firefox()
# driver=webdriver.ie()
# maximize the window size
driver.maximize_window()#C:\Users\Pc Casa\pythonProject3Demoyas
# navigate to the url
driver.get("C:\\Users\\Pc Casa\\pythonProject3Demoyas\\Example.html")
btn_element = driver.find_element(By.CSS_SELECTOR,".btn")
btn_myNameIs_attr_val = btn_element.get_attribute("myNameis")
print(btn_myNameIs_attr_val)
time.sleep(3)
#input
input_element = driver.find_element(By.CSS_SELECTOR,"[id^='user1_btn_']")
input_element.send_keys("Great To See You!")

time.sleep(60)
# close the browser
driver.close()
print("sample test case successfully completed")