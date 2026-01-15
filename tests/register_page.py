"""
Register Page Object Model
"""
from selenium.webdriver.common.by import By
from tests.base_page import BasePage


class RegisterPage(BasePage):
    """Page Object untuk halaman register"""
    
    # Locators
    NAME_INPUT = (By.ID, "name")
    EMAIL_INPUT = (By.ID, "InputEmail")
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "InputPassword")
    REPASSWORD_INPUT = (By.ID, "InputRePassword")
    SUBMIT_BUTTON = (By.NAME, "submit")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-danger")
    PASSWORD_ERROR = (By.CSS_SELECTOR, ".text-danger")
    LOGIN_LINK = (By.LINK_TEXT, "Login")
    
    def __init__(self, driver, base_url="http://localhost/quiz-pengupil"):
        super().__init__(driver, base_url)
        self.url = f"{base_url}/register.php"
    
    def open(self):
        """Buka halaman register"""
        self.driver.get(self.url)
        return self
    
    def register(self, name, email, username, password, repassword):
        """Perform register action"""
        self.input_text(self.NAME_INPUT, name)
        self.input_text(self.EMAIL_INPUT, email)
        self.input_text(self.USERNAME_INPUT, username)
        self.input_text(self.PASSWORD_INPUT, password)
        self.input_text(self.REPASSWORD_INPUT, repassword)
        self.click(self.SUBMIT_BUTTON)
    
    def get_error_message(self):
        """Get error message text"""
        try:
            return self.get_text(self.ERROR_MESSAGE)
        except:
            return None
    
    def get_password_error(self):
        """Get password validation error"""
        try:
            return self.get_text(self.PASSWORD_ERROR)
        except:
            return None
    
    def click_login_link(self):
        """Click link ke halaman login"""
        self.click(self.LOGIN_LINK)
    
    def is_on_register_page(self):
        """Check apakah berada di halaman register"""
        return "register.php" in self.get_current_url()
