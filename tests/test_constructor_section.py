from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Main_Locators
from url import MAIN_URL

class TestConstructorSection:
    
    def test_select_sauces_tab(self, driver):
        driver.get(MAIN_URL)
        wait = WebDriverWait(driver, 5)
        
        tab = wait.until(EC.element_to_be_clickable(Main_Locators.SAUCES_TAB))
        tab.click()

        assert "current" in tab.get_attribute("class")

    def test_select_filling_tab(self, driver):
        driver.get(MAIN_URL)
        wait = WebDriverWait(driver, 5)
        
        tab = wait.until(EC.element_to_be_clickable(Main_Locators.FILLING_TAB))
        tab.click()

        assert "current" in tab.get_attribute("class")

    def test_select_bun_tab(self, driver):
        driver.get(MAIN_URL)
        wait = WebDriverWait(driver, 5)

        wait.until(EC.element_to_be_clickable(Main_Locators.SAUCES_TAB)).click()
        
        tab = wait.until(EC.element_to_be_clickable(Main_Locators.BUN_TAB))
        tab.click()

        assert "current" in tab.get_attribute("class")
        