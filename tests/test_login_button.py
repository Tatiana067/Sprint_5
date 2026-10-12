from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from url import MAIN_URL, REGISTER_URL
from locators import Login_Locators, Main_Locators, Register_Locators, Forgot_Password_Locators
from user_data import get_static_credentials

class TestLogin: 
    def test_log_in_to_account_button(self, driver): 
        static_user = get_static_credentials() 
        driver.get(MAIN_URL) 
        driver.find_element(*Main_Locators.LOG_BUTTON_ACCOUNT).click() 

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Login_Locators.EMAIL_FIELD)) 

        driver.find_element(*Login_Locators.EMAIL_FIELD).send_keys(static_user.email) 
        driver.find_element(*Login_Locators.PASSWORD_FIELD).send_keys(static_user.password) 
        driver.find_element(*Login_Locators.LOGIN_BUTTON).click() 
        
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Main_Locators.PLACE_AN_ORDER_BUTTON)) 

        assert driver.find_element(*Main_Locators.PLACE_AN_ORDER_BUTTON).is_displayed()

    def test_login_personal_account_button(self, driver): 
        static_user = get_static_credentials() 
        driver.get(MAIN_URL) 
        driver.find_element(*Main_Locators.PERSONAL_ACCOUNT_BUTTON).click() 

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Login_Locators.EMAIL_FIELD)) 

        driver.find_element(*Login_Locators.EMAIL_FIELD).send_keys(static_user.email) 
        driver.find_element(*Login_Locators.PASSWORD_FIELD).send_keys(static_user.password) 
        driver.find_element(*Login_Locators.LOGIN_BUTTON).click() 
        
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Main_Locators.PLACE_AN_ORDER_BUTTON)) 

        assert driver.find_element(*Main_Locators.PLACE_AN_ORDER_BUTTON).is_displayed()

    def test_login_via_registration_form_link_success(self, driver): 
        static_user = get_static_credentials() 
        driver.get(REGISTER_URL) 
        driver.find_element(*Register_Locators.TEXT_LOGIN).click() 

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Login_Locators.EMAIL_FIELD)) 

        driver.find_element(*Login_Locators.EMAIL_FIELD).send_keys(static_user.email) 
        driver.find_element(*Login_Locators.PASSWORD_FIELD).send_keys(static_user.password) 
        driver.find_element(*Login_Locators.LOGIN_BUTTON).click() 
        
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Main_Locators.PLACE_AN_ORDER_BUTTON)) 

        assert driver.find_element(*Main_Locators.PLACE_AN_ORDER_BUTTON).is_displayed()

    def test_login_via_forgot_password_form_link_success(self, driver): 
        static_user = get_static_credentials() 
        driver.get(MAIN_URL) 
        driver.find_element(*Main_Locators.LOG_BUTTON_ACCOUNT).click() 

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Login_Locators.TEXT_RESET_PASSWORD)) 

        driver.find_element(*Login_Locators.TEXT_RESET_PASSWORD).click() 
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Forgot_Password_Locators.LOGIN_LINK)) 

        driver.find_element(*Forgot_Password_Locators.LOGIN_LINK).click() 
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Login_Locators.EMAIL_FIELD)) 

        driver.find_element(*Login_Locators.EMAIL_FIELD).send_keys(static_user.email) 
        driver.find_element(*Login_Locators.PASSWORD_FIELD).send_keys(static_user.password) 
        driver.find_element(*Login_Locators.LOGIN_BUTTON).click() 
        
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Main_Locators.PLACE_AN_ORDER_BUTTON)) 
        
        assert driver.find_element(*Main_Locators.PLACE_AN_ORDER_BUTTON).is_displayed()
