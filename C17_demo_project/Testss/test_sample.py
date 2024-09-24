import time

from selenium.webdriver.common.by import By


class Test01:

    def test_method1(self,driver):
        driver.get("https://www.google.com/")
        expected_label_text = "Google offered in: Français"
        actual_label_text = driver.find_element(By.ID, "SIvCob").text

        assert expected_label_text == actual_label_text, f"Error occurred! Actual label text is {actual_label_text}. Expected label text is {expected_label_text}"

    def test_method2(self,driver):
        driver.get("https://yahoo.com")
        assert driver.current_url.__contains__("yahoo"), "Error occured!"