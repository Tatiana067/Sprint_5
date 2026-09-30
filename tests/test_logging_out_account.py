from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from url import PERSONAL_ACCOUNT_URL
from locators import Login_Account_Locators, Login_Locators

class TestLogout:
    def test_logging_out_account(self, driver):
        driver.get(PERSONAL_ACCOUNT_URL)
        driver.find_element(*Login_Account_Locators.LOGOUT_BUTTON).click()
        
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Login_Locators.LOGIN_BUTTON))
   
        actual_button_text = driver.find_element(*Login_Locators.LOGIN_BUTTON).text
        assert actual_button_text == 'Войти'
        