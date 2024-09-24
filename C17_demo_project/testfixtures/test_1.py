import time

import pytest
from selenium.webdriver.common.by import By

class Test1:
    def test_1(self,driver):
        driver.get(" https://demo.guru99.com/test/newtours/index.php")

        driver.find_element(By.XPATH,"/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/a").click()

        driver.find_element(By.NAME, "firstName").send_keys("Yasmin")
        driver.find_element(By.NAME, "lastName").send_keys("Garcia")
        driver.find_element(By.NAME, "phone").send_keys("789456123")
        driver.find_element(By.NAME, "email").send_keys("yasriga@hotmail.com")
        driver.find_element(By.NAME, "address1").send_keys("78 Main street")
        driver.find_element(By.NAME, "City").send_keys("Toronto")
        driver.find_element(By.NAME, "State").send_keys("Ontario")
        driver.find_element(By.NAME, "PostalCode").send_keys("M4C5G8")
        driver.find_element(By.NAME, "Country").send_keys("Canada")
        driver.find_element(By.NAME, "UserName").send_keys(["yasriga"])
        driver.find_element(By.NAME, "password").send_keys(["789456"])
        driver.find_element(By.NAME, "confirmPassword").send_keys(["789456"])

        # Step 3: Click on the "Submit" button

        success_message = driver.find_element(By.XPATH, "//*[@id='email'']")
        assert "Your user name is yasriga" in success_message.text, "Registration failed or username not displayed"
        pytest.File("Registration failed or confirmation message not found.")