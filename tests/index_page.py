"""
Index/Dashboard Page Object Model
"""
from selenium.webdriver.common.by import By
from tests.base_page import BasePage


class IndexPage(BasePage):
    """Page Object untuk halaman index/dashboard"""
    
    # Locators
    USERNAME_DISPLAY = (By.ID, "username-display")
    SUCCESS_MESSAGE = (By.ID, "login-success-message")
    LOGOUT_BUTTON = (By.ID, "logout-button")
    
    def __init__(self, driver, base_url="http://localhost/quiz-pengupil"):
        super().__init__(driver, base_url)
        self.url = f"{base_url}/index.php"
    
    def is_logged_in(self):
        """Check apakah user sudah login (berada di index page)"""
        return "index.php" in self.get_current_url()
    
    def get_username_display(self):
        """Get username yang ditampilkan"""
        try:
            return self.get_text(self.USERNAME_DISPLAY)
        except:
            return None
    
    def get_success_message(self):
        """Get success message"""
        try:
            return self.get_text(self.SUCCESS_MESSAGE)
        except:
            return None
    
    def logout(self):
        """Click logout button"""
        self.click(self.LOGOUT_BUTTON)
