"""
Test Configuration dan Fixtures
"""
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Conditional import for webdriver-manager (not needed in CI)
if not os.getenv('CI'):
    from webdriver_manager.chrome import ChromeDriverManager

# Conditional import for database stub (not needed in CI)
if not os.getenv('CI'):
    from tests.database_stub import DatabaseStub


# Test Configuration
BASE_URL = os.getenv('BASE_URL', 'http://localhost:8000')
HEADLESS = os.getenv('HEADLESS', 'false').lower() == 'true'


@pytest.fixture(scope="session")
def db_stub():
    """Database stub fixture untuk session"""
    # Skip database stub di CI/CD karena menggunakan MySQL service
    if os.getenv('CI'):
        yield None
        return
    
    # Import here to avoid import errors in CI
    from tests.database_stub import DatabaseStub
    
    stub = DatabaseStub()
    stub.setup_test_database()
    stub.seed_default_users()
    yield stub
    stub.close()
    stub.close()


@pytest.fixture(scope="function")
def clean_db(db_stub):
    """Clean database sebelum setiap test"""
    # Skip di CI/CD karena database sudah di-setup oleh workflow
    if os.getenv('CI'):
        yield None
        return
        
    db_stub.clear_all_users()
    db_stub.seed_default_users()
    yield db_stub


@pytest.fixture(scope="function")
def driver():
    """Selenium WebDriver fixture"""
    chrome_options = Options()
    
    if HEADLESS:
        chrome_options.add_argument("--headless=new")
    
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    
    # Untuk CI/CD, gunakan Chrome yang sudah terinstall
    if os.getenv('CI'):
        driver = webdriver.Chrome(options=chrome_options)
    else:
        # Local development, gunakan webdriver-manager
        from webdriver_manager.chrome import ChromeDriverManager
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
    
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(30)
    
    yield driver
    
    try:
        driver.quit()
    except:
        pass


@pytest.fixture(scope="function")
def login_page(driver):
    """Login page fixture"""
    from tests.login_page import LoginPage
    return LoginPage(driver, BASE_URL)


@pytest.fixture(scope="function")
def register_page(driver):
    """Register page fixture"""
    from tests.register_page import RegisterPage
    return RegisterPage(driver, BASE_URL)


@pytest.fixture(scope="function")
def index_page(driver):
    """Index page fixture"""
    from tests.index_page import IndexPage
    return IndexPage(driver, BASE_URL)
