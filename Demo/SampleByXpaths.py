from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver (using Chrome in this example)
driver = webdriver.Chrome()

try:
    # Step 1: Navigate to the Udemy homepage
    driver.get("https://www.udemy.com/")
    driver.maximize_window()

    # Step 2: Locate the search bar using relative XPath
    search_bar = driver.find_element(By.XPATH, "//input[@name='q']")
    time.sleep(3)

    # Step 3: Enter a search query (e.g., 'Python')
    search_bar.send_keys("Python")
    time.sleep(5)

    # Step 4: Submit the search query
    search_bar.send_keys(Keys.ENTER)

    # Wait for search results to load
    time.sleep(5)

    # Step 5: Verify that search results are displayed
    # Relative XPath for search result containers (You can adjust based on actual HTML structure)
    results = driver.find_elements(By.XPATH, "
    if results:
        print("Search results are displayed.")
    else:
        print("No search results found.")

finally:
    # Capture a screenshot
    driver.save_screenshot("udemy_search_test.png")

    # Close the browser
    driver.quit()