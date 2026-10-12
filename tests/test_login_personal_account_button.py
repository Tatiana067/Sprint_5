from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from url import MAIN_URL
from locators import Login_Locators, Main_Locators
from user_data import get_static_credentials

class TestLogin:

    def test_login_personal_account_button(self, driver):
        static_user = get_static_credentials()
        driver.get(MAIN_URL)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Main_Locators.PERSONAL_ACCOUNT_BUTTON))
        driver.find_element(*Main_Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Login_Locators.EMAIL_FIELD))
        driver.find_element(*Login_Locators.EMAIL_FIELD).send_keys(static_user.email)
        driver.find_element(*Login_Locators.PASSWORD_FIELD).send_keys(static_user.password)
        
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Login_Locators.LOGIN_BUTTON))
        driver.find_element(*Login_Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(Main_Locators.PLACE_AN_ORDER_BUTTON, 'Оформить заказ'))
        actual_button_text = driver.find_element(*Main_Locators.PLACE_AN_ORDER_BUTTON).text
        assert actual_button_text == 'Оформить заказ'
        