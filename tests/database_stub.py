"""
Database Stub untuk Testing
Menyediakan mock database operations untuk testing tanpa mengubah database real
"""
import mysql.connector
from mysql.connector import Error
import hashlib


class DatabaseStub:
    """Database stub untuk isolasi testing"""
    
    def __init__(self, host='localhost', user='root', password='', database='quiz_pengupil_test'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
    
    def connect(self):
        """Membuat koneksi ke test database"""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            return True
        except Error as e:
            print(f"Error connecting to database: {e}")
            return False
    
    def setup_test_database(self):
        """Setup test database dan tabel"""
        try:
            # Connect tanpa database untuk create database
            conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password
            )
            cursor = conn.cursor()
            
            # Drop dan create database
            cursor.execute(f"DROP DATABASE IF EXISTS {self.database}")
            cursor.execute(f"CREATE DATABASE {self.database}")
            cursor.execute(f"USE {self.database}")
            
            # Create table users
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(70) NOT NULL,
                    username VARCHAR(50) NOT NULL,
                    email VARCHAR(50) NOT NULL,
                    password VARCHAR(255) NOT NULL
                )
            """)
            
            conn.commit()
            cursor.close()
            conn.close()
            
            # Reconnect ke test database
            self.connect()
            return True
            
        except Error as e:
            print(f"Error setting up test database: {e}")
            return False
    
    def insert_test_user(self, username, name, email, password):
        """Insert user untuk testing"""
        try:
            cursor = self.connection.cursor()
            # Hash password seperti di PHP dengan bcrypt
            # Note: Python bcrypt hash berbeda dengan PHP, jadi kita simpan plain untuk testing
            query = "INSERT INTO users (username, name, email, password) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (username, name, email, password))
            self.connection.commit()
            cursor.close()
            return True
        except Error as e:
            print(f"Error inserting test user: {e}")
            return False
    
    def delete_user(self, username):
        """Delete user by username"""
        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM users WHERE username = %s"
            cursor.execute(query, (username,))
            self.connection.commit()
            cursor.close()
            return True
        except Error as e:
            print(f"Error deleting user: {e}")
            return False
    
    def user_exists(self, username):
        """Check apakah user exists"""
        try:
            cursor = self.connection.cursor()
            query = "SELECT COUNT(*) FROM users WHERE username = %s"
            cursor.execute(query, (username,))
            result = cursor.fetchone()
            cursor.close()
            return result[0] > 0
        except Error as e:
            print(f"Error checking user: {e}")
            return False
    
    def clear_all_users(self):
        """Clear semua users dari test database"""
        try:
            cursor = self.connection.cursor()
            cursor.execute("TRUNCATE TABLE users")
            self.connection.commit()
            cursor.close()
            return True
        except Error as e:
            print(f"Error clearing users: {e}")
            return False
    
    def seed_default_users(self):
        """Seed database dengan default test users"""
        # Password: 123456 (hashed dengan PHP password_hash)
        default_users = [
            ('irul', '', 'irul@irul.com', '$2y$10$D9yc9Mt0t8niCNO9di8ejOUPib46suwHghqFnJKQJ3Z6uwRDxfw.'),
            ('ahmad', '', 'ahmad@ahmad.com', '$2y$10$OWez2au.UMnz3yedD0BqH.bsOC374XoV9VhMigepVzLyuq2jETHs2')
        ]
        
        for username, name, email, password in default_users:
            self.insert_test_user(username, name, email, password)
    
    def close(self):
        """Close database connection"""
        if self.connection and self.connection.is_connected():
            self.connection.close()
    
    def __enter__(self):
        """Context manager enter"""
        self.connect()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit"""
        self.close()
