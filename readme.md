# Quiz Pengupil - Automated Testing Suite

[![Selenium Test Suite CI/CD](https://github.com/fandcomp/quiz-pengupil/actions/workflows/selenium-tests.yml/badge.svg)](https://github.com/fandcomp/quiz-pengupil/actions/workflows/selenium-tests.yml)

Proyek ini merupakan aplikasi quiz dengan sistem autentikasi (login & register) yang dilengkapi dengan automated testing menggunakan Selenium WebDriver.

## 📋 Fitur

- **Modul Login**: Autentikasi user dengan validasi
- **Modul Register**: Pendaftaran user baru dengan validasi
- **Automated Testing**: Test suite lengkap menggunakan Selenium
- **CI/CD Pipeline**: GitHub Actions untuk automated testing
- **Database Stub**: Mock database untuk testing isolation
- **Page Object Model**: Design pattern untuk maintainable test code

## 🧪 Test Cases

Proyek ini mencakup test cases komprehensif untuk:

### Modul Login (8 test cases)
- ✅ Login dengan kredensial valid
- ✅ Login dengan password salah
- ✅ Login dengan username tidak terdaftar
- ✅ Login dengan field kosong
- ✅ Login dengan username kosong
- ✅ Login dengan password kosong
- ✅ SQL Injection prevention test
- ✅ Navigasi ke halaman register

### Modul Register (8 test cases)
- ✅ Register dengan data valid
- ✅ Register dengan field name kosong (Bug Test)
- ✅ Register dengan password mismatch
- ✅ Register dengan username duplikat
- ✅ Register dengan email kosong
- ✅ Register dengan semua field kosong
- ✅ Register dengan password kosong
- ✅ Navigasi ke halaman login

### Integration Tests (3 test cases)
- ✅ Register kemudian login
- ✅ Multiple registration dengan username sama
- ✅ Login-logout-login cycle

**Total: 19 Test Cases**

Lihat dokumentasi lengkap di [TEST_CASES.md](TEST_CASES.md)

## 🚀 Setup dan Instalasi

### Prerequisites

- PHP 7.4 atau lebih tinggi
- MySQL/MariaDB
- Python 3.8+
- Chrome Browser (untuk Selenium)

### Instalasi

1. **Clone repository**
   ```bash
   git clone https://github.com/fandcomp/quiz-pengupil.git
   cd quiz-pengupil
   ```

2. **Setup Database**
   
   **Untuk PowerShell:**
   ```powershell
   .\setup_database.ps1
   ```
   
   **Untuk CMD:**
   ```cmd
   setup_database.bat
   ```
   
   **Atau manual via MySQL:**
   ```sql
   mysql -u root -p
   CREATE DATABASE quiz_pengupil;
   USE quiz_pengupil;
   SOURCE db/quiz_pengupil.sql;
   ```

3. **Konfigurasi Database**
   
   Edit `koneksi.php` sesuai dengan konfigurasi database Anda:
   ```php
   $host     = 'localhost';
   $user     = 'root'; 
   $password = 'your_password';                  
   $db       = 'quiz_pengupil';
   ```

4. **Install Python Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Jalankan Web Server**
   ```bash
   php -S localhost:8000
   ```

## 🧪 Menjalankan Tests

### Menjalankan Semua Tests
```bash
python tests/run_tests.py
```

### Menjalankan Test Spesifik
```bash
# Login tests only
python tests/run_tests.py login

# Register tests only
python tests/run_tests.py register

# Integration tests only
python tests/run_tests.py integration
```

### Menggunakan pytest langsung
```bash
# Semua tests
pytest tests/ -v

# Specific test file
pytest tests/test_login.py -v

# Specific test case
pytest tests/test_login.py::TestLogin::test_login_with_valid_credentials -v
```

### Generate Test Report
```bash
pytest tests/ -v --html=test-reports/report.html --self-contained-html
```

## 🔄 CI/CD Pipeline

Proyek ini menggunakan GitHub Actions untuk automated testing. Setiap push atau pull request akan trigger:

1. Setup environment (PHP, Python, MySQL)
2. Install dependencies
3. Start PHP server
4. Setup test database
5. Run Selenium test suite
6. Generate dan upload test reports
7. Publish test results

Lihat konfigurasi lengkap di [`.github/workflows/selenium-tests.yml`](.github/workflows/selenium-tests.yml)

## 📁 Struktur Proyek

```
quiz-pengupil/
├── .github/
│   └── workflows/
│       └── selenium-tests.yml    # GitHub Actions workflow
├── db/
│   └── quiz_pengupil.sql         # Database schema
├── tests/
│   ├── __init__.py
│   ├── base_page.py              # Base Page Object Model
│   ├── login_page.py             # Login Page Object
│   ├── register_page.py          # Register Page Object
│   ├── index_page.py             # Index/Dashboard Page Object
│   ├── database_stub.py          # Database stub untuk testing
│   ├── conftest.py               # Pytest fixtures dan configuration
│   ├── test_login.py             # Login test cases
│   ├── test_register.py          # Register test cases
│   ├── test_integration.py       # Integration test cases
│   └── run_tests.py              # Test runner script
├── koneksi.php                   # Database connection
├── login.php                     # Login page
├── register.php                  # Register page
├── index.php                     # Dashboard/landing page
├── logout.php                    # Logout handler
├── style.css                     # Styles
├── requirements.txt              # Python dependencies
├── .gitignore                    # Git ignore file
├── TEST_CASES.md                 # Test cases documentation
└── README.md                     # This file
```

## 🛠️ Technologies Used

### Backend
- PHP 7.4+
- MySQL/MariaDB
- Session Management

### Testing
- **Selenium WebDriver**: Browser automation
- **pytest**: Test framework
- **Page Object Model**: Design pattern
- **Database Stub**: Test isolation
- **webdriver-manager**: Automatic driver management

### CI/CD
- **GitHub Actions**: Automated testing pipeline
- **pytest-html**: HTML test reports
- **JUnit XML**: Test result format

## 📊 Test Coverage

Test suite mencakup:
- ✅ Positive test cases (happy path)
- ✅ Negative test cases (error handling)
- ✅ Boundary value testing
- ✅ Security testing (SQL injection)
- ✅ Integration testing
- ✅ Form validation testing
- ✅ Session management testing

## 🐛 Known Issues

1. **Field Name Kosong di Database**: Sesuai dengan catatan, field `name` pada tabel `users` sengaja tidak diisi (kosong) untuk keperluan testing. Ini merupakan bug yang dicatat dan diuji dalam test case TC-REG-002.

## 👥 Kontributor

- **fandcomp** - [GitHub Profile](https://github.com/fandcomp)

## 📝 Lisensi

Proyek ini dibuat untuk keperluan pembelajaran - Pengujian Perangkat Lunak, Politeknik SSN.

## 🔗 Repository Link

**GitHub Repository**: [https://github.com/fandcomp/quiz-pengupil](https://github.com/fandcomp/quiz-pengupil)

## 📞 Kontak

Jika ada pertanyaan atau saran, silakan buka issue di repository ini.

---