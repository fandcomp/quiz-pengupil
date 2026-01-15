"""
Test runner script - menjalankan semua test cases
"""
import pytest
import sys


def run_all_tests():
    """Run all test suites"""
    args = [
        "tests/",
        "-v",
        "--tb=short",
        "--html=test-reports/report.html",
        "--self-contained-html",
        "--junitxml=test-reports/junit.xml",
        "-s"
    ]
    
    return pytest.main(args)


def run_login_tests():
    """Run only login tests"""
    return pytest.main(["tests/test_login.py", "-v", "-s"])


def run_register_tests():
    """Run only register tests"""
    return pytest.main(["tests/test_register.py", "-v", "-s"])


def run_integration_tests():
    """Run only integration tests"""
    return pytest.main(["tests/test_integration.py", "-v", "-s"])


if __name__ == "__main__":
    if len(sys.argv) > 1:
        test_type = sys.argv[1]
        
        if test_type == "login":
            sys.exit(run_login_tests())
        elif test_type == "register":
            sys.exit(run_register_tests())
        elif test_type == "integration":
            sys.exit(run_integration_tests())
        else:
            print(f"Unknown test type: {test_type}")
            print("Available options: login, register, integration, or run without arguments for all tests")
            sys.exit(1)
    else:
        sys.exit(run_all_tests())
