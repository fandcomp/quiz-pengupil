# Test Cases untuk Modul Login dan Register

## Test Cases Modul Register

### TC-REG-001: Register dengan data valid
**Tujuan**: Memverifikasi bahwa user dapat mendaftar dengan data yang valid  
**Input**:
- Name: "Test User"
- Email: "testuser@example.com"
- Username: "testuser123"
- Password: "Test@1234"
- Re-Password: "Test@1234"

**Expected Output**: User berhasil terdaftar dan diarahkan ke halaman index.php

**Priority**: High

---

### TC-REG-002: Register dengan field name kosong (Bug Test)
**Tujuan**: Memverifikasi sistem dapat menangani field name yang kosong  
**Input**:
- Name: "" (kosong)
- Email: "emptyname@example.com"
- Username: "emptyname"
- Password: "Test@1234"
- Re-Password: "Test@1234"

**Expected Output**: Sistem menolak registrasi dengan pesan "Data tidak boleh kosong !!"

**Priority**: High  
**Note**: Sesuai catatan, field name di database sengaja dibiarkan kosong untuk testing

---

### TC-REG-003: Register dengan password tidak match
**Tujuan**: Memvalidasi bahwa sistem memeriksa kecocokan password  
**Input**:
- Name: "Test User"
- Email: "mismatch@example.com"
- Username: "mismatchpass"
- Password: "Test@1234"
- Re-Password: "Test@5678"

**Expected Output**: Pesan error "Password tidak sama !!"

**Priority**: High

---

### TC-REG-004: Register dengan username yang sudah ada
**Tujuan**: Memverifikasi validasi username duplikat  
**Input**:
- Name: "Test User"
- Email: "duplicate@example.com"
- Username: "irul" (sudah ada di database)
- Password: "Test@1234"
- Re-Password: "Test@1234"

**Expected Output**: Pesan error "Username sudah terdaftar !!"

**Priority**: High

---

### TC-REG-005: Register dengan field email kosong
**Tujuan**: Memvalidasi required field email  
**Input**:
- Name: "Test User"
- Email: "" (kosong)
- Username: "noemail"
- Password: "Test@1234"
- Re-Password: "Test@1234"

**Expected Output**: Pesan error "Data tidak boleh kosong !!"

**Priority**: Medium

---

### TC-REG-006: Register dengan semua field kosong
**Tujuan**: Memvalidasi form dengan semua field kosong  
**Input**: Semua field kosong

**Expected Output**: Pesan error "Data tidak boleh kosong !!"

**Priority**: Medium

---

### TC-REG-007: Register dengan password kosong
**Tujuan**: Memvalidasi required field password  
**Input**:
- Name: "Test User"
- Email: "nopass@example.com"
- Username: "nopass"
- Password: "" (kosong)
- Re-Password: "" (kosong)

**Expected Output**: Pesan error "Data tidak boleh kosong !!"

**Priority**: Medium

---

## Test Cases Modul Login

### TC-LOG-001: Login dengan kredensial valid
**Tujuan**: Memverifikasi login dengan username dan password yang benar  
**Input**:
- Username: "irul"
- Password: "123456" (sesuai database)

**Expected Output**: User berhasil login dan diarahkan ke halaman index.php

**Priority**: High

---

### TC-LOG-002: Login dengan password salah
**Tujuan**: Memverifikasi penanganan password yang salah  
**Input**:
- Username: "irul"
- Password: "wrongpassword"

**Expected Output**: Tidak ada redirect, tetap di halaman login (password tidak cocok)

**Priority**: High

---

### TC-LOG-003: Login dengan username tidak terdaftar
**Tujuan**: Memverifikasi penanganan username yang tidak ada  
**Input**:
- Username: "usernotexist"
- Password: "anypassword"

**Expected Output**: Pesan error "Register User Gagal !!"

**Priority**: High

---

### TC-LOG-004: Login dengan field kosong
**Tujuan**: Memvalidasi required fields pada login  
**Input**:
- Username: "" (kosong)
- Password: "" (kosong)

**Expected Output**: Pesan error "Data tidak boleh kosong !!"

**Priority**: Medium

---

### TC-LOG-005: Login dengan username kosong
**Tujuan**: Memvalidasi required field username  
**Input**:
- Username: "" (kosong)
- Password: "anypassword"

**Expected Output**: Pesan error "Data tidak boleh kosong !!"

**Priority**: Medium

---

### TC-LOG-006: Login dengan password kosong
**Tujuan**: Memvalidasi required field password  
**Input**:
- Username: "irul"
- Password: "" (kosong)

**Expected Output**: Pesan error "Data tidak boleh kosong !!"

**Priority**: Medium

---

### TC-LOG-007: Login dengan SQL Injection attempt
**Tujuan**: Memverifikasi keamanan terhadap SQL Injection  
**Input**:
- Username: "admin' OR '1'='1"
- Password: "anything"

**Expected Output**: Login ditolak, tidak ada SQL injection berhasil

**Priority**: High

---

## Test Cases Integration

### TC-INT-001: Register kemudian Login
**Tujuan**: Memverifikasi integrasi antara modul register dan login  
**Steps**:
1. Register user baru dengan data valid
2. Logout (jika ada halaman logout)
3. Login dengan kredensial user yang baru dibuat

**Expected Output**: User dapat register dan login dengan sukses

**Priority**: High

---

### TC-INT-002: Register dengan name kosong kemudian cek database
**Tujuan**: Memverifikasi bahwa data dengan name kosong dapat tersimpan di database (sesuai catatan)  
**Steps**:
1. Bypass validasi frontend
2. Submit register dengan name="" tetapi field lain terisi
3. Cek database apakah record tersimpan dengan name kosong

**Expected Output**: Sesuai dengan bug yang dicatat, name field di database kosong

**Priority**: Medium

---

## Strategi Testing

### Stub/Driver yang Diperlukan:

1. **Database Stub**: Mock database untuk testing tanpa mengubah data real
2. **Session Driver**: Untuk mengatur dan memverifikasi session management
3. **Email Stub**: Jika ada fungsi email verification di masa depan

### Automation Strategy:

- Gunakan Selenium WebDriver untuk UI testing
- Setup dan teardown database sebelum/sesudah setiap test
- Implementasi Page Object Model untuk maintainability
- Gunakan pytest fixtures untuk setup/teardown

### CI/CD Integration:

- Jalankan test suite pada setiap push
- Test database menggunakan MySQL/MariaDB di Docker container
- Generate test reports
- Block merge jika test gagal
