-- Setup Database untuk Quiz Pengupil
-- Jalankan script ini untuk membuat database dan tabel

-- Buat database jika belum ada
CREATE DATABASE IF NOT EXISTS quiz_pengupil;

-- Gunakan database
USE quiz_pengupil;

-- Buat tabel users
CREATE TABLE IF NOT EXISTS `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(70) NOT NULL,
  `username` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Insert data default untuk testing
-- Password untuk kedua user adalah: 123456
INSERT INTO `users` (`id`, `name`, `username`, `email`, `password`) VALUES
	(1, '', 'irul', 'irul@irul.com', '$2y$10$D9yc9Mt0t8niCNO9di8ejOUPib46suwHghqFnJKQJ3Z6uwRDxfw.'),
	(2, '', 'ahmad', 'ahmad@ahmad.com', '$2y$10$OWez2au.UMnz3yedD0BqH.bsOC374XoV9VhMigepVzLyuq2jETHs2');

-- Tampilkan hasil
SELECT 'Database quiz_pengupil berhasil dibuat!' as Status;
SELECT * FROM users;
