# src/database.py
import psycopg2

class Database:
    def __init__(self):
        # Security finding: password hardcoded
        self.host = "localhost"
        self.port = 5432
        self.user = "test_user"
        self.password = "P@ssw0rd_hardcoded"  # <-- hardcoded credential (intended)
        self.conn = None

    def connect(self):
        if self.conn:
            return self.conn
        self.conn = psycopg2.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            dbname="test_db"
        )
        return self.conn

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None

