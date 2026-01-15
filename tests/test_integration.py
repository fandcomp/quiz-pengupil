"""
Integration Test Cases
Test integrasi antara modul login dan register
"""
import pytest
import time


class TestIntegration:
    """Test suite untuk integration testing"""
    
    def test_register_then_login(self, driver, register_page, login_page, index_page, clean_db):
        """TC-INT-001: Register kemudian Login"""
        # Step 1: Register user baru
        register_page.open()
        register_page.register(
            name="Integration Test User",
            email="integration@test.com",
            username="integrationuser",
            password="Test@1234",
            repassword="Test@1234"
        )
        time.sleep(2)
        
        # Verify registration successful
        assert index_page.is_logged_in(), "Should be logged in after registration"
        
        # Step 2: Logout
        index_page.logout()
        time.sleep(2)
        
        # Step 3: Login dengan kredensial yang baru dibuat
        login_page.open()
        login_page.login("integrationuser", "Test@1234")
        time.sleep(2)
        
        # Assert
        assert index_page.is_logged_in(), "Should be able to login with new credentials"
        assert "integrationuser" in index_page.get_username_display(), "Username should match"
    
    def test_multiple_registration_attempts_same_username(self, driver, register_page, clean_db):
        """Test multiple registration dengan username yang sama"""
        # First registration
        register_page.open()
        register_page.register(
            name="First User",
            email="first@test.com",
            username="sameuser",
            password="Test@1234",
            repassword="Test@1234"
        )
        time.sleep(2)
        
        # Try to register again with same username
        register_page.open()
        register_page.register(
            name="Second User",
            email="second@test.com",
            username="sameuser",
            password="Test@5678",
            repassword="Test@5678"
        )
        time.sleep(2)
        
        # Assert
        error_msg = register_page.get_error_message()
        assert error_msg is not None, "Error message should be displayed"
        assert "Username sudah terdaftar" in error_msg, "Should prevent duplicate registration"
    
    def test_login_logout_login_cycle(self, driver, login_page, index_page, clean_db):
        """Test siklus login -> logout -> login"""
        # Login pertama
        login_page.open()
        login_page.login("irul", "123456")
        time.sleep(2)
        assert index_page.is_logged_in(), "Should be logged in"
        
        # Logout
        index_page.logout()
        time.sleep(2)
        assert login_page.is_on_login_page(), "Should be redirected to login page"
        
        # Login lagi
        login_page.login("irul", "123456")
        time.sleep(2)
        assert index_page.is_logged_in(), "Should be able to login again"


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
