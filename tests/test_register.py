"""
Test Cases untuk Modul Register
Menggunakan Selenium WebDriver dan Page Object Model
"""
import pytest
import time


class TestRegister:
    """Test suite untuk modul register"""
    
    def test_register_with_valid_data(self, driver, register_page, index_page, clean_db):
        """TC-REG-001: Register dengan data valid"""
        # Arrange
        register_page.open()
        
        # Act
        register_page.register(
            name="Test User",
            email="testuser@example.com",
            username="testuser123",
            password="Test@1234",
            repassword="Test@1234"
        )
        time.sleep(2)
        
        # Assert
        assert index_page.is_logged_in(), "User should be redirected to index page after registration"
        assert "testuser123" in index_page.get_username_display(), "Username should be displayed"
    
    def test_register_with_empty_name(self, driver, register_page, clean_db):
        """TC-REG-002: Register dengan field name kosong (Bug Test)"""
        # Arrange
        register_page.open()
        
        # Act
        register_page.register(
            name="",
            email="emptyname@example.com",
            username="emptyname",
            password="Test@1234",
            repassword="Test@1234"
        )
        time.sleep(2)
        
        # Assert
        error_msg = register_page.get_error_message()
        assert error_msg is not None, "Error message should be displayed"
        assert "Data tidak boleh kosong" in error_msg, "Should show empty data message"
    
    def test_register_with_password_mismatch(self, driver, register_page, clean_db):
        """TC-REG-003: Register dengan password tidak match"""
        # Arrange
        register_page.open()
        
        # Act
        register_page.register(
            name="Test User",
            email="mismatch@example.com",
            username="mismatchpass",
            password="Test@1234",
            repassword="Test@5678"
        )
        time.sleep(2)
        
        # Assert
        error_msg = register_page.get_password_error()
        assert error_msg is not None, "Error message should be displayed"
        assert "Password tidak sama" in error_msg, "Should show password mismatch message"
    
    def test_register_with_existing_username(self, driver, register_page, clean_db):
        """TC-REG-004: Register dengan username yang sudah ada"""
        # Arrange
        register_page.open()
        
        # Act
        register_page.register(
            name="Test User",
            email="duplicate@example.com",
            username="irul",  # Username yang sudah ada
            password="Test@1234",
            repassword="Test@1234"
        )
        time.sleep(2)
        
        # Assert
        error_msg = register_page.get_error_message()
        assert error_msg is not None, "Error message should be displayed"
        assert "Username sudah terdaftar" in error_msg, "Should show duplicate username message"
    
    def test_register_with_empty_email(self, driver, register_page, clean_db):
        """TC-REG-005: Register dengan field email kosong"""
        # Arrange
        register_page.open()
        
        # Act
        register_page.register(
            name="Test User",
            email="",
            username="noemail",
            password="Test@1234",
            repassword="Test@1234"
        )
        time.sleep(2)
        
        # Assert
        error_msg = register_page.get_error_message()
        assert error_msg is not None, "Error message should be displayed"
        assert "Data tidak boleh kosong" in error_msg, "Should show empty data message"
    
    def test_register_with_all_empty_fields(self, driver, register_page, clean_db):
        """TC-REG-006: Register dengan semua field kosong"""
        # Arrange
        register_page.open()
        
        # Act
        register_page.register(
            name="",
            email="",
            username="",
            password="",
            repassword=""
        )
        time.sleep(2)
        
        # Assert
        error_msg = register_page.get_error_message()
        assert error_msg is not None, "Error message should be displayed"
        assert "Data tidak boleh kosong" in error_msg, "Should show empty data message"
    
    def test_register_with_empty_password(self, driver, register_page, clean_db):
        """TC-REG-007: Register dengan password kosong"""
        # Arrange
        register_page.open()
        
        # Act
        register_page.register(
            name="Test User",
            email="nopass@example.com",
            username="nopass",
            password="",
            repassword=""
        )
        time.sleep(2)
        
        # Assert
        error_msg = register_page.get_error_message()
        assert error_msg is not None, "Error message should be displayed"
        assert "Data tidak boleh kosong" in error_msg, "Should show empty data message"
    
    def test_navigate_to_login_page(self, driver, register_page, login_page):
        """Test navigasi dari register ke login page"""
        # Arrange
        register_page.open()
        
        # Act
        register_page.click_login_link()
        time.sleep(1)
        
        # Assert
        assert login_page.is_on_login_page(), "Should navigate to login page"


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
