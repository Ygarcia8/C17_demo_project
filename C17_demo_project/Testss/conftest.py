import pytest
from selenium import webdriver

@pytest.fixture
def user_data(s):
    return {
    "username": "yasriga",
    "password": "789456"
    }
@pytest.fixture()
def register_userdata():
    username="yasriga"
    password="789456"
    return [username, password]

@pytest.fixture(scope="class")
def driver():
    print("********************************Intializing Chrome Driver**************************************")
    driver=webdriver.Chrome()
    return driver


