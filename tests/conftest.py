"""
Test Configuration dan Fixtures
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from tests.database_stub import DatabaseStub


# Test Configuration
BASE_URL = "http://localhost/quiz-pengupil"
HEADLESS = False  # Set True untuk CI/CD


@pytest.fixture(scope="session")
def db_stub():
    """Database stub fixture untuk session"""
    stub = DatabaseStub()
    stub.setup_test_database()
    stub.seed_default_users()
    yield stub
    stub.close()


@pytest.fixture(scope="function")
def clean_db(db_stub):
    """Clean database sebelum setiap test"""
    db_stub.clear_all_users()
    db_stub.seed_default_users()
    yield db_stub


@pytest.fixture(scope="function")
def driver():
    """Selenium WebDriver fixture"""
    chrome_options = Options()
    
    if HEADLESS:
        chrome_options.add_argument("--headless")
    
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    
    # Gunakan webdriver-manager untuk auto-download chromedriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(10)
    
    yield driver
    
    driver.quit()


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
