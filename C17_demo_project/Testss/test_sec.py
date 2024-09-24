import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException


# Test data (can be modified for reruns with unique usernames)
@pytest.fixture
def user_data():
    return {
        "first_name": "Yasmin",
        "last_name": "Garcia",
        "phone": "647",
        "email": "johndoe@example.com",
        "username": "uniqueusername123",  # Change this for reruns
        "password": "password123"
    }


# Setup fixture for browser
@pytest.fixture
def setup():
    driver_path = "path/to/chromedriver"
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get("https://demo.guru99.com/test/newtours/index.php")

    yield driver

    driver.quit()


# Define the test class
class TestUserFlow:

    # Test Case 1: Registering a new user
    def test_register_user(self, setup, user_data):
        driver = setup

        # Step 1: Click on "Register here" link
        register_link = driver.find_element(By.LINK_TEXT, "REGISTER")
        register_link.click()

        # Step 2: Fill out the registration form using user_data fixture
        driver.find_element(By.NAME, "firstName").send_keys(user_data["first_name"])
        driver.find_element(By.NAME, "lastName").send_keys(user_data["last_name"])
        driver.find_element(By.NAME, "phone").send_keys(user_data["phone"])
        driver.find_element(By.NAME, "userName").send_keys(user_data["email"])
        driver.find_element(By.NAME, "address1").send_keys("123 Test Street")
        driver.find_element(By.NAME, "city").send_keys("Test City")
        driver.find_element(By.NAME, "state").send_keys("Test State")
        driver.find_element(By.NAME, "postalCode").send_keys("12345")
        driver.find_element(By.NAME, "country").send_keys("UNITED STATES")
        driver.find_element(By.NAME, "email").send_keys(user_data["username"])
        driver.find_element(By.NAME, "password").send_keys(user_data["password"])
        driver.find_element(By.NAME, "confirmPassword").send_keys(user_data["password"])

        # Step 3: Click on the "Submit" button
        driver.find_element(By.NAME, "submit").click()

        # Step 4: Assert successful registration by verifying the username label
        try:
            success_message = driver.find_element(By.XPATH,f"//b[contains(text(), 'Note: Your user name is {user_data['username']}.')]")
            assert user_data["username"] in success_message.text, "Registration failed or username not displayed"
        except NoSuchElementException:
            pytest.fail("Registration failed or confirmation message not found.")

    # Test Case 2: Initial sign-in
    def test_sign_in(self, setup, user_data):
        driver = setup

        # Step 1: Click on "SIGN-ON" link
        sign_in_link = driver.find_element(By.LINK_TEXT, "SIGN-ON")
        sign_in_link.click()

        # Step 2: Enter the username and password
        driver.find_element(By.NAME, "userName").send_keys(user_data["username"])
        driver.find_element(By.NAME, "password").send_keys(user_data["password"])

        # Step 3: Click "Submit" button
        driver.find_element(By.NAME, "submit").click()

        # Step 4: Verify successful login by asserting the "Login Successfully" message
        try:
            success_message = driver.find_element(By.XPATH, "//h3[contains(text(),'Login Successfully')]")
            assert "Login Successfully" in success_message.text, "Login failed"
        except NoSuchElementException:
            pytest.fail("Login failed or confirmation message not found.")

    # Test Case 3: Log out
    def test_log_out(self, setup):
        driver = setup

        # Step 1: Click on "SIGN-OFF" button
        sign_off_link = driver.find_element(By.LINK_TEXT, "SIGN-OFF")
        sign_off_link.click()

        # Step 2: Verify successful logout by checking for the "SIGN-ON" link
        try:
            sign_on_link = driver.find_element(By.LINK_TEXT, "SIGN-ON")
            assert sign_on_link.is_displayed(), "Logout failed"
        except NoSuchElementException:
            pytest.fail("Logout failed or SIGN-ON link not found.")