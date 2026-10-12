import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Login_Locators, Register_Locators
from url import REGISTER_URL
from user_data import generate_random_credentials

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def register_page(driver):
    driver.get(REGISTER_URL)
    return driver

@pytest.fixture
def register_new_user(register_page):
    user_data = generate_random_credentials('Татьяна')
    driver = register_page 
    driver.find_element(*Register_Locators.NAME_FIELD).send_keys(user_data.name)
    driver.find_element(*Register_Locators.EMAIL_FIELD).send_keys(user_data.email)
    driver.find_element(*Register_Locators.PASSWORD_FIELD).send_keys(user_data.password)
    driver.find_element(*Register_Locators.REGISTER_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((Login_Locators.LOGIN_BUTTON)))
    return user_data
