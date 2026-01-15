# Quick Start Guide - Bahasa Indonesia

## Setup Cepat untuk Windows (PowerShell)

### 1. Install Prerequisites
- ✅ PHP 7.4+ (Download: https://www.php.net/downloads)
- ✅ MySQL/MariaDB (Download: https://dev.mysql.com/downloads/)
- ✅ Python 3.8+ (Download: https://www.python.org/downloads/)
- ✅ Chrome Browser

### 2. Setup Database
Jalankan script otomatis:
```powershell
.\setup_database.ps1
```
Script ini akan:
- Membuat database `quiz_pengupil`
- Membuat tabel `users`
- Insert data test users (irul & ahmad)

### 3. Install Python Dependencies
```powershell
pip install -r requirements.txt
```

### 4. Jalankan Aplikasi
```powershell
php -S localhost:8000
```

Buka browser: http://localhost:8000/login.php

Login dengan:
- Username: `irul` / Password: `123456`
- Username: `ahmad` / Password: `123456`

### 5. Jalankan Tests (Optional)
Buka terminal baru:
```powershell
python tests/run_tests.py
```

## Troubleshooting PowerShell

### Error: "mysql not recognized"
Tambahkan MySQL ke PATH:
```powershell
$env:Path += ";C:\Program Files\MySQL\MySQL Server 8.0\bin"
```
Atau restart terminal setelah install MySQL.

### Error: "script cannot be loaded"
Enable script execution:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Error: "php not recognized"  
Tambahkan PHP ke PATH:
```powershell
$env:Path += ";C:\php"
```

### Import Database Manual (Jika Script Gagal)

**Opsi 1: Menggunakan Get-Content**
```powershell
Get-Content db\setup_database.sql | mysql -u root -p
```

**Opsi 2: Menggunakan MySQL Shell**
```powershell
mysql -u root -p
```
Lalu di MySQL prompt:
```sql
SOURCE db/setup_database.sql;
```

**Opsi 3: Copy-Paste SQL**
1. Buka file `db/setup_database.sql`
2. Copy semua isinya
3. Paste di MySQL Workbench atau phpMyAdmin
4. Execute

## File Penting

- `setup_database.ps1` - Setup database otomatis (PowerShell)
- `setup_database.bat` - Setup database otomatis (CMD)
- `db/setup_database.sql` - SQL script untuk database
- `tests/run_tests.py` - Menjalankan semua tests

## Command Berguna

```powershell
# Setup database
.\setup_database.ps1

# Jalankan web server
php -S localhost:8000

# Install dependencies
pip install -r requirements.txt

# Run all tests
python tests/run_tests.py

# Run specific tests
python tests/run_tests.py login
python tests/run_tests.py register

# Generate HTML report
pytest tests/ -v --html=test-reports/report.html --self-contained-html
```

## Struktur Database

**Database:** quiz_pengupil  
**Tabel:** users

| Field    | Type         | Description        |
|----------|--------------|-------------------|
| id       | INT(11)      | Primary Key       |
| name     | VARCHAR(70)  | Nama user (kosong untuk test) |
| username | VARCHAR(50)  | Username          |
| email    | VARCHAR(50)  | Email             |
| password | VARCHAR(255) | Password (hashed) |

**Default Users:**
- Username: `irul`, Password: `123456`, Email: `irul@irul.com`
- Username: `ahmad`, Password: `123456`, Email: `ahmad@ahmad.com`

## Testing

### Local Testing
```powershell
# Start server
php -S localhost:8000

# Run tests (terminal baru)
python tests/run_tests.py
```

### CI/CD Testing
Push ke GitHub - GitHub Actions akan otomatis menjalankan tests.

## Next Steps

1. ✅ Setup database (gunakan script)
2. ✅ Test login manual di browser
3. ✅ Install Python dependencies
4. ✅ Run automated tests
5. ✅ Push ke GitHub
6. ✅ Monitor GitHub Actions

## Bantuan Lebih Lanjut

Lihat file lengkap:
- `SETUP_GUIDE.md` - Setup detail
- `TEST_CASES.md` - Dokumentasi test cases
- `README.md` - Dokumentasi lengkap
