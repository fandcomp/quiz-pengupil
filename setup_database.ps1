# Setup Database Script untuk PowerShell
# Script ini akan membuat database quiz_pengupil

Write-Host "=== Quiz Pengupil - Database Setup ===" -ForegroundColor Cyan
Write-Host ""

# Konfigurasi database
$DB_NAME = "quiz_pengupil"
$DB_USER = "root"

# Minta password
$DB_PASSWORD = Read-Host -Prompt "Masukkan password MySQL untuk user 'root'" -AsSecureString
$DB_PASSWORD_PLAIN = [Runtime.InteropServices.Marshal]::PtrToStringAuto(
    [Runtime.InteropServices.Marshal]::SecureStringToBSTR($DB_PASSWORD)
)

Write-Host ""
Write-Host "Mengecek koneksi MySQL..." -ForegroundColor Yellow

# Test koneksi
$testConnection = "SELECT 1" | mysql -u $DB_USER -p"$DB_PASSWORD_PLAIN" 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "Error: Tidak dapat terhubung ke MySQL!" -ForegroundColor Red
    Write-Host "Pastikan MySQL service berjalan dan password benar." -ForegroundColor Red
    exit 1
}

Write-Host "Koneksi berhasil!" -ForegroundColor Green
Write-Host ""

# Setup database
Write-Host "Membuat database dan tabel..." -ForegroundColor Yellow

$sqlFile = Join-Path $PSScriptRoot "db\setup_database.sql"

if (Test-Path $sqlFile) {
    Get-Content $sqlFile | mysql -u $DB_USER -p"$DB_PASSWORD_PLAIN"
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host ""
        Write-Host "========================================" -ForegroundColor Green
        Write-Host "Database berhasil dibuat!" -ForegroundColor Green
        Write-Host "========================================" -ForegroundColor Green
        Write-Host ""
        Write-Host "Database: $DB_NAME" -ForegroundColor Cyan
        Write-Host "Default Users:" -ForegroundColor Cyan
        Write-Host "  1. Username: irul     Password: 123456" -ForegroundColor White
        Write-Host "  2. Username: ahmad    Password: 123456" -ForegroundColor White
        Write-Host ""
        Write-Host "Next Steps:" -ForegroundColor Yellow
        Write-Host "  1. Jalankan: php -S localhost:8000" -ForegroundColor White
        Write-Host "  2. Buka browser: http://localhost:8000/login.php" -ForegroundColor White
        Write-Host "  3. Atau run tests: python tests/run_tests.py" -ForegroundColor White
        Write-Host ""
    } else {
        Write-Host "Error saat membuat database!" -ForegroundColor Red
        exit 1
    }
} else {
    Write-Host "Error: File $sqlFile tidak ditemukan!" -ForegroundColor Red
    exit 1
}
