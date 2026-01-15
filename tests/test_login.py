"""
Test Cases untuk Modul Login
Menggunakan Selenium WebDriver dan Page Object Model
"""
import pytest
import time


class TestLogin:
    """Test suite untuk modul login"""
    
    def test_login_with_valid_credentials(self, driver, login_page, index_page, clean_db):
        """TC-LOG-001: Login dengan kredensial valid"""
        # Arrange
        login_page.open()
        
        # Act
        login_page.login("irul", "123456")
        time.sleep(2)
        
        # Assert
        assert index_page.is_logged_in(), "User should be redirected to index page"
        assert "irul" in index_page.get_username_display(), "Username should be displayed"
    
    def test_login_with_wrong_password(self, driver, login_page, clean_db):
        """TC-LOG-002: Login dengan password salah"""
        # Arrange
        login_page.open()
        
        # Act
        login_page.login("irul", "wrongpassword")
        time.sleep(2)
        
        # Assert
        assert login_page.is_on_login_page(), "Should stay on login page"
    
    def test_login_with_nonexistent_username(self, driver, login_page, clean_db):
        """TC-LOG-003: Login dengan username tidak terdaftar"""
        # Arrange
        login_page.open()
        
        # Act
        login_page.login("usernotexist", "anypassword")
        time.sleep(2)
        
        # Assert
        error_msg = login_page.get_error_message()
        assert error_msg is not None, "Error message should be displayed"
        assert "Register User Gagal" in error_msg, "Should show register failed message"
    
    def test_login_with_empty_fields(self, driver, login_page, clean_db):
        """TC-LOG-004: Login dengan field kosong"""
        # Arrange
        login_page.open()
        
        # Act
        login_page.login("", "")
        time.sleep(2)
        
        # Assert
        error_msg = login_page.get_error_message()
        assert error_msg is not None, "Error message should be displayed"
        assert "Data tidak boleh kosong" in error_msg, "Should show empty data message"
    
    def test_login_with_empty_username(self, driver, login_page, clean_db):
        """TC-LOG-005: Login dengan username kosong"""
        # Arrange
        login_page.open()
        
        # Act
        login_page.login("", "anypassword")
        time.sleep(2)
        
        # Assert
        error_msg = login_page.get_error_message()
        assert error_msg is not None, "Error message should be displayed"
        assert "Data tidak boleh kosong" in error_msg, "Should show empty data message"
    
    def test_login_with_empty_password(self, driver, login_page, clean_db):
        """TC-LOG-006: Login dengan password kosong"""
        # Arrange
        login_page.open()
        
        # Act
        login_page.login("irul", "")
        time.sleep(2)
        
        # Assert
        error_msg = login_page.get_error_message()
        assert error_msg is not None, "Error message should be displayed"
        assert "Data tidak boleh kosong" in error_msg, "Should show empty data message"
    
    def test_login_sql_injection_attempt(self, driver, login_page, clean_db):
        """TC-LOG-007: Login dengan SQL Injection attempt"""
        # Arrange
        login_page.open()
        
        # Act
        login_page.login("admin' OR '1'='1", "anything")
        time.sleep(2)
        
        # Assert
        # Should not be able to login with SQL injection
        assert login_page.is_on_login_page() or login_page.get_error_message() is not None, \
            "SQL injection should be prevented"
    
    def test_navigate_to_register_page(self, driver, login_page, register_page):
        """Test navigasi dari login ke register page"""
        # Arrange
        login_page.open()
        
        # Act
        login_page.click_register_link()
        time.sleep(1)
        
        # Assert
        assert register_page.is_on_register_page(), "Should navigate to register page"


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
