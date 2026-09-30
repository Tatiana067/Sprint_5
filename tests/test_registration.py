from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from url import REGISTER_URL
from locators import Register_Locators, Login_Locators
from user_data import generate_random_credentials

class TestRegistration:
    def test_registration(self,register_new_user, driver):

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Login_Locators.LOGIN_BUTTON))

        button_text = driver.find_element(*Login_Locators.LOGIN_BUTTON).text
        assert button_text == 'Войти'

    def test_registration_short_password_failed(self, driver):
        new_user = generate_random_credentials('Татьяна')
        driver.get(REGISTER_URL)

        driver.find_element(*Register_Locators.NAME_FIELD).send_keys(new_user.name)
        driver.find_element(*Register_Locators.EMAIL_FIELD).send_keys(new_user.email)
        driver.find_element(*Register_Locators.PASSWORD_FIELD).send_keys('12345')

        driver.find_element(*Register_Locators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Register_Locators.PASSWORD_ERROR))

        error_text = driver.find_element(*Register_Locators.PASSWORD_ERROR).text
        assert error_text == 'Некорректный пароль'
