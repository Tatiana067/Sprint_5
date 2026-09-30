from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from url import MAIN_URL
from locators import Register_Locators, Login_Locators, Main_Locators, Login_Account_Locators
from user_data import get_static_credentials

class TestFromAccount:

    def test_from_personal_account_constructor(self, driver):
        static_user = get_static_credentials()
        driver.get(MAIN_URL)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Main_Locators.PERSONAL_ACCOUNT_BUTTON))
        driver.find_element(*Main_Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Login_Locators.EMAIL_FIELD))
        driver.find_element(*Login_Locators.EMAIL_FIELD).send_keys(static_user.email)
        driver.find_element(*Login_Locators.PASSWORD_FIELD).send_keys(static_user.password)
        driver.find_element(*Login_Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Main_Locators.PERSONAL_ACCOUNT_BUTTON))
        driver.find_element(*Main_Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Login_Account_Locators.DESIGNER))
        driver.find_element(*Login_Account_Locators.DESIGNER).click()
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(Main_Locators.PLACE_AN_ORDER_BUTTON, 'Оформить заказ'))
        assert driver.current_url == MAIN_URL

    def test_navigation_from_account_to_logo_success(self, driver):
        static_user = get_static_credentials()
        driver.get(MAIN_URL)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Main_Locators.PERSONAL_ACCOUNT_BUTTON))
        driver.find_element(*Main_Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Login_Locators.EMAIL_FIELD))
        driver.find_element(*Login_Locators.EMAIL_FIELD).send_keys(static_user.email)
        driver.find_element(*Login_Locators.PASSWORD_FIELD).send_keys(static_user.password)
        driver.find_element(*Login_Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Main_Locators.PERSONAL_ACCOUNT_BUTTON))
        driver.find_element(*Main_Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Login_Account_Locators.LOGO))
        driver.find_element(*Login_Account_Locators.LOGO).click()
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(Main_Locators.PLACE_AN_ORDER_BUTTON, 'Оформить заказ'))
        assert driver.current_url == MAIN_URL