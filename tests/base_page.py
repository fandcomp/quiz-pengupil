"""
Base Page Object Model untuk Selenium Tests
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    """Base class untuk semua page objects"""
    
    def __init__(self, driver, base_url="http://localhost/quiz-pengupil"):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, 10)
    
    def find_element(self, locator):
        """Find element dengan explicit wait"""
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def find_elements(self, locator):
        """Find multiple elements"""
        return self.wait.until(EC.presence_of_all_elements_located(locator))
    
    def click(self, locator):
        """Click element dengan wait"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    def input_text(self, locator, text):
        """Input text ke element"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator):
        """Get text dari element"""
        return self.find_element(locator).text
    
    def is_element_present(self, locator):
        """Check apakah element ada"""
        try:
            self.driver.find_element(*locator)
            return True
        except:
            return False
    
    def get_current_url(self):
        """Get current URL"""
        return self.driver.current_url
