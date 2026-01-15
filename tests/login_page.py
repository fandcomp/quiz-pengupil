"""
Login Page Object Model
"""
from selenium.webdriver.common.by import By
from tests.base_page import BasePage


class LoginPage(BasePage):
    """Page Object untuk halaman login"""
    
    # Locators
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "InputPassword")
    SUBMIT_BUTTON = (By.NAME, "submit")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-danger")
    REGISTER_LINK = (By.LINK_TEXT, "Register")
    
    def __init__(self, driver, base_url="http://localhost/quiz-pengupil"):
        super().__init__(driver, base_url)
        self.url = f"{base_url}/login.php"
    
    def open(self):
        """Buka halaman login"""
        self.driver.get(self.url)
        return self
    
    def login(self, username, password):
        """Perform login action"""
        self.input_text(self.USERNAME_INPUT, username)
        self.input_text(self.PASSWORD_INPUT, password)
        self.click(self.SUBMIT_BUTTON)
    
    def get_error_message(self):
        """Get error message text"""
        try:
            return self.get_text(self.ERROR_MESSAGE)
        except:
            return None
    
    def click_register_link(self):
        """Click link ke halaman register"""
        self.click(self.REGISTER_LINK)
    
    def is_on_login_page(self):
        """Check apakah berada di halaman login"""
        return "login.php" in self.get_current_url()
