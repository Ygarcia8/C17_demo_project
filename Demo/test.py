import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

print("sample test case started")
driver = webdriver.Chrome()

# Load the HTML file
driver.get("C:\\Users\\Pc Casa\\pythonProject3Demoyas\\Demo\\test.html")
time.sleep(3)

# Interact with various elements on the page
try:
    # Enter text into the input field
    name_field = driver.find_element(By.ID, 'name')
    name_field.send_keys('Yasmin Garcia')
    time.sleep(3)
    # Click the Submit button
    submit_button = driver.find_element(By.ID, 'submitBtn')
    submit_button.click()
    time.sleep(3)
    # Check the checkbox
    checkbox = driver.find_element(By.ID, 'subscribe')
    checkbox.click()
    time.sleep(3)

    gender_radio = driver.find_element(By.ID, 'female')
    gender_radio.click()
    time.sleep(3)

    dropdown = driver.find_element(By.ID, 'tool')
    dropdown.send_keys('Selenium')

    time.sleep(3)
finally:
    # Close the browser
    driver.quit()