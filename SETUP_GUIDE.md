# Setup Guide untuk Automated Testing

## Prerequisites

Pastikan Anda memiliki software berikut terinstall:

1. **PHP 7.4+**
   - Download dari https://www.php.net/downloads
   - Pastikan `php` tersedia di PATH

2. **MySQL/MariaDB**
   - Download MySQL dari https://dev.mysql.com/downloads/
   - Atau MariaDB dari https://mariadb.org/download/

3. **Python 3.8+**
   - Download dari https://www.python.org/downloads/
   - Pastikan "Add Python to PATH" dicentang saat instalasi

4. **Chrome Browser**
   - Download dari https://www.google.com/chrome/

5. **Git**
   - Download dari https://git-scm.com/downloads

## Langkah-langkah Setup

### 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/quiz-pengupil.git
cd quiz-pengupil
```

### 2. Setup Database

#### Opsi 1: Menggunakan Setup Script (Recommended)

**Untuk PowerShell (Windows):**
```powershell
.\setup_database.ps1
```

**Untuk CMD (Windows):**
```cmd
setup_database.bat
```

**Untuk Linux/Mac:**
```bash
mysql -u root -p < db/setup_database.sql
```

#### Opsi 2: Manual - MySQL Command Line

Buka MySQL command line atau MySQL Workbench:

```sql
CREATE DATABASE quiz_pengupil;
USE quiz_pengupil;
SOURCE db/quiz_pengupil.sql;

-- Verify
SHOW TABLES;
SELECT * FROM users;
```

#### Opsi 3: PowerShell (tanpa script)

```powershell
# Import database menggunakan Get-Content
Get-Content db\setup_database.sql | mysql -u root -p

# Atau menggunakan mysql dengan SOURCE
mysql -u root -p -e "SOURCE db/setup_database.sql"
```

**Note**: Di PowerShell, operator `<` tidak bekerja untuk redirect. Gunakan `Get-Content` atau script yang disediakan.

### 3. Konfigurasi Database Connection

Edit file `koneksi.php` sesuai dengan setup MySQL Anda:

```php
<?php
    $host     = 'localhost';
    $user     = 'root';          // Sesuaikan dengan user MySQL Anda
    $password = 'your_password';  // Sesuaikan dengan password MySQL Anda
    $db       = 'quiz_pengupil';

    $con = mysqli_connect($host, $user, $password, $db);
    if (!$con) { 
        die("Connection failed: " . mysqli_connect_error());    
    }
?>
```

### 4. Install Python Dependencies

```bash
pip install -r requirements.txt
```

Jika ada error, coba:
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Test Manual (Optional)

Jalankan PHP built-in server:

```bash
php -S localhost:8000
```

Buka browser dan akses:
- http://localhost:8000/login.php
- http://localhost:8000/register.php

### 6. Setup Test Database

Untuk testing, buat database terpisah:

**Menggunakan PowerShell:**
```powershell
# Buat file SQL temporary untuk test database
@"
CREATE DATABASE IF NOT EXISTS quiz_pengupil_test;
USE quiz_pengupil_test;
"@ | Out-File -FilePath temp_test_db.sql -Encoding utf8

Get-Content temp_test_db.sql, db\quiz_pengupil.sql | mysql -u root -p
Remove-Item temp_test_db.sql
```

**Atau manual via MySQL:**
```sql
CREATE DATABASE quiz_pengupil_test;
USE quiz_pengupil_test;
SOURCE db/quiz_pengupil.sql;
```

Update file `tests/conftest.py` jika perlu mengubah konfigurasi database test.

### 7. Run Tests

#### Opsi 1: Menggunakan test runner script

```bash
# Run semua tests
python tests/run_tests.py

# Run specific module
python tests/run_tests.py login
python tests/run_tests.py register
python tests/run_tests.py integration
```

#### Opsi 2: Menggunakan pytest langsung

```bash
# Run semua tests dengan verbose output
pytest tests/ -v

# Run specific test file
pytest tests/test_login.py -v

# Run specific test case
pytest tests/test_login.py::TestLogin::test_login_with_valid_credentials -v

# Generate HTML report
pytest tests/ -v --html=test-reports/report.html --self-contained-html
```

### 8. Troubleshooting

#### Error: "Connection failed"
- Pastikan MySQL service berjalan
- Cek username dan password di `koneksi.php`
- Cek database sudah dibuat

#### Error: "No module named 'selenium'"
```bash
pip install selenium
```

#### Error: "ChromeDriver not found"
```bash
pip install webdriver-manager
```
webdriver-manager akan otomatis download ChromeDriver yang sesuai.

#### Error: "Address already in use" (Port 8000)
Gunakan port lain:
```bash
php -S localhost:8080
```
Lalu update `BASE_URL` di `tests/conftest.py`

#### Tests gagal karena timing
Tambahkan `time.sleep()` di test cases atau tingkatkan implicit wait di `conftest.py`

## Menjalankan Tests di Headless Mode

Edit file `tests/conftest.py`:

```python
HEADLESS = True  # Set ke True untuk headless mode
```

Headless mode berguna untuk:
- Running tests di server tanpa GUI
- CI/CD pipeline
- Faster test execution

## Generate Test Reports

### HTML Report
```bash
pytest tests/ -v --html=test-reports/report.html --self-contained-html
```

Buka `test-reports/report.html` di browser untuk melihat hasil.

### JUnit XML Report (untuk CI/CD)
```bash
pytest tests/ -v --junitxml=test-reports/junit.xml
```

## Best Practices

1. **Selalu jalankan test dengan clean database**
   - Fixture `clean_db` akan otomatis membersihkan database sebelum setiap test

2. **Gunakan database terpisah untuk testing**
   - Jangan gunakan database production untuk testing

3. **Review test reports**
   - Cek HTML report untuk detail hasil test
   - Lihat screenshots jika test gagal

4. **Update test cases**
   - Tambah test cases untuk fitur baru
   - Update test cases jika ada perubahan requirement

## Next Steps

Setelah semua setup selesai:

1. Push code ke GitHub
2. Setup GitHub Actions (sudah dikonfigurasi di `.github/workflows/selenium-tests.yml`)
3. Monitor test execution di GitHub Actions tab

## Kontak

Jika ada masalah saat setup, silakan buka issue di repository atau hubungi kontributor.
