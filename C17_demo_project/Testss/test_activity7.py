import time
from selenium.webdriver.common.by import By

class Test1:
    def test_1(self,driver,register_userdata):
        driver.get(" https://demo.guru99.com/test/newtours/index.php")
        driver.find_element(By.XPATH,"/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/a").click()

        user_name_locator = driver.find_element(By.CSS_SELECTOR, "#email")
        user_name_locator.send_keys(register_userdata[0])
        password=driver.find_element(By.NAME,"password")
        password.send_keys(register_userdata[1])
        confirm_password=driver.find_element(By.NAME,"confirmPassword")
        confirm_password.send_keys(register_userdata[1])
        submit=driver.find_element(By.XPATH,'//input[@name="submit"]')
        submit.click()
        time.sleep(3)

    def test_2(self, driver,register_userdata):
        # click on signin  button
        signin_link = driver.find_element(By.XPATH, '//a[@href="login.php"]')
        signin_link.click()
        user_name_signin = driver.find_element(By.NAME, "userName")
        user_name_signin.send_keys(register_userdata[0])
        password_signin = driver.find_element(By.NAME, "password")
        password_signin.send_keys(register_userdata[1])
        submit_signin = driver.find_element(By.NAME, "submit")
        submit_signin.click()
        time.sleep(5)

    def test_method3(self, driver):
        # click on signoff button
        sign_off = driver.find_element(By.XPATH, "//td[@class='mouseOut']/a[@href='index.php']")
        sign_off.click()
