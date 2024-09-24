from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
import time

# Setup WebDriver
driver = webdriver.Chrome()

# Open the test page with the HTML provided (use a local file or URL if hosted)
driver.get("C:\\Users\\Pc Casa\\pythonProject3Demoyas\\Demo\\scrollactivity.html")
driver.maximize_window()

# Step 1: Locate the radio buttons using XPath and select "Option 1"
option1 = driver.find_element(By.XPATH, "//input[@id='option1']")
option1.click()
assert option1.is_selected(), "Option 1 should be selected."
time.sleep(3)
# Step 2: Select "Option 2" and verify "Option 1" is not selected
option2 = driver.find_element(By.XPATH, "//input[@id='option2']")
option2.click()
assert option2.is_selected(), "Option 2 should be selected."
assert not option1.is_selected(), "Option 1 should not be selected after selecting Option 2."
time.sleep(3)
# 2: Dropdown Selection
# Locate the dropdown and select "Option C" /
dropdown = Select(driver.find_element(By.XPATH, "//select[@id='dropdown']"))
dropdown.select_by_visible_text("Option C")
selected_option = dropdown.first_selected_option.text
assert selected_option == "Option C", "Option C should be selected."
time.sleep(3)

# Task 3: Drag and Drop
# Locate the draggable element and the droppable
draggable = driver.find_element(By.XPATH, "//div[@id='draggable']")
droppable = driver.find_element(By.XPATH, "//div[@id='droppable']")

# Perform drag and drop using ActionChains
actions = ActionChains(driver)
actions.drag_and_drop(draggable, droppable).perform()

# Verify the background color of the drop target changes to green
droppable_class = droppable.get_attribute("class")
assert "highlight" in droppable_class, "The drop target should change color to green after a successful drop."
time.sleep(3)
# Task 4: Alert Handling
# Locate the alert trigger button and click it
alert_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Show Alert')]")
alert_button.click()
time.sleep(3)
# Switch to the alert, verify its text, and accept it
alert = Alert(driver)
assert alert.text == "This is an alert!", "Alert text should be 'This is an alert!'"
alert.accept()
time.sleep(3)
# Task 5: Scrolling
# Scroll to the button that scrolls to the top
scroll_button = driver.find_element(By.XPATH, "//button[@id='scrollButton']")
driver.execute_script("arguments[0].scrollIntoView();", scroll_button)
scroll_button.click()
IMAG="C:\\Users\\Pc Casa\\pythonProject3Demoyas\\imag"



time.sleep(5)
scroll_position = driver.execute_script("return window.pageYOffset;")
assert scroll_position == 0, "The page should be scrolled to the top."


driver.quit()

print("Test Passed: All tasks successfully automated.")