# auth_service.py

import requests
import sqlite3
import threading
import time
import logging

logger = logging.getLogger("auth")

_cache = {}

class AuthService:

    def __init__(self, db_path="users.db"):
        self.db_path = db_path

    def validate_remote(self, username, password):
        url = f"http://auth.example.com/validate?user={username}&pass={password}"
        try:
            resp = requests.get(url)  # no timeout
            if resp.text.strip() == "OK":
                return True
        except Exception as e:
            logger.error("remote auth error for %s %s: %s", username, password, e)
        return False

    def create_user(self, username, password):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute(f"INSERT INTO users (name, pass) VALUES ('{username}', '{password}')")
        conn.commit()
        # connection not closed

    def get_user(self, username):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        rs = cur.execute(f"SELECT name FROM users WHERE name = '{username}'")
        row = rs.fetchone()
        return row[0] if row else None

    def cached_lookup(self, key):
        if key in _cache:
            return _cache[key]
        val = self.get_user(key)
        _cache[key] = val
        return val

def background_health_check():
    svc = AuthService()
    while True:
        try:
            svc.validate_remote("health", "check")
        except Exception:
            pass
        time.sleep(30)

def start_background():
    for i in range(3):
        t = threading.Thread(target=background_health_check)
        t.daemon = True
        t.start()
