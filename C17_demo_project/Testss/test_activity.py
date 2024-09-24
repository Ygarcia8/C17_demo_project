# test_google_label.py

from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

def test_text_label():
    print("Sample Test case Started!!!!")
    # Chrome Driver
    driver = webdriver.Chrome()
    # Maximize the windows size
    driver.maximize_window()
    driver.get('https://www.google.com/')
    #finding the element by xpath
    book_demo=driver.find_element(By.XPATH,'//*[@id="SIvCob"]')
    text_book_demo=book_demo.text
    print("Extracted Text:",text_book_demo)
    #assertion
    assert 'Ofrecido por Google en: English Français' == text_book_demo
    driver.close()