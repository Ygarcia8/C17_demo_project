from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Initialize the WebDriver (replace 'chromedriver' with the path to your WebDriver if needed)
driver = webdriver.Chrome()

try:
    # Go to Google.com
    driver.get('https://www.google.com')

    # Find the search box, type the query, and submit the search
    search_box = driver.find_element(By.NAME, 'q')
    search_box.send_keys('Mennonite new life center')
    search_box.send_keys(Keys.RETURN)

    # Wait for the results to load
    time.sleep(2)

    # Get the first search result link
    first_result = driver.find_element(By.CSS_SELECTOR, 'h3')
    first_result_link = first_result.find_element(By.XPATH, '..').get_attribute('href')

    # Open a new tab and navigate to the copied link
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(first_result_link)

    # Close the original search result tab
    driver.switch_to.window(driver.window_handles[0])
    driver.close()

    # Switch back to the new tab
    driver.switch_to.window(driver.window_handles[0])

    # Optionally, you can add a delay to see the result
    time.sleep(5)

finally:
    # Close the browser
    driver.quit()