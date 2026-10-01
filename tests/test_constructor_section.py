from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Main_Locators
from url import MAIN_URL

class TestConstructorSection:
    
    def test_constructor_section(self, driver):
        driver.get(MAIN_URL)
        wait = WebDriverWait(driver, 5)

        wait.until(EC.element_to_be_clickable(Main_Locators.SAUCES_TAB)).click()
        assert len(driver.find_elements(*Main_Locators.SAUCES_TEXT)) > 0

        wait.until(EC.element_to_be_clickable(Main_Locators.FILLING_TAB)).click()
        assert len(driver.find_elements(*Main_Locators.FILLING_TEXT)) > 0

        wait.until(EC.element_to_be_clickable(Main_Locators.BUN_TAB)).click()
        assert len(driver.find_elements(*Main_Locators.BUN_TEXT)) > 0
