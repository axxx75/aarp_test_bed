# src/database.py
import os
import psycopg2

class Database:
    def __init__(self):
        self.host = os.environ.get("DB_HOST", "localhost")
        self.port = int(os.environ.get("DB_PORT", 5432))
        self.user = os.environ.get("DB_USER", "test_user")
        self.password = os.environ.get("DB_PASSWORD", "") # Replaced hardcoded password with environment variable
        self.conn = None

    def connect(self):
        if self.conn:
            return self.conn
        self.conn = psycopg2.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            dbname=os.environ.get("DB_NAME", "test_db")
        )
        return self.conn

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None

