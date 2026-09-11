import os
import sqlite3
from pathlib import Path

DATA_DIR = os.getenv("DATA_DIR", "data")
DB_PATH = Path(DATA_DIR) / "secnote.db"

def get_connection():
    Path(DATA_DIR).mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    # incidents
    cur.execute("""
        CREATE TABLE IF NOT EXISTS incidents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            severity TEXT NOT NULL,
            status TEXT NOT NULL,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        );
    """)
    # tags
    cur.execute("""
        CREATE TABLE IF NOT EXISTS tags (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        );
    """)
    # incident_tags
    cur.execute("""
        CREATE TABLE IF NOT EXISTS incident_tags (
            incident_id INTEGER NOT NULL,
            tag_id INTEGER NOT NULL,
            FOREIGN KEY (incident_id) REFERENCES incidents(id),
            FOREIGN KEY (tag_id) REFERENCES tags(id)
        );
    """)
    # weak_passwords
    cur.execute("""
        CREATE TABLE IF NOT EXISTS weak_passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            password TEXT NOT NULL,
            source TEXT
        );
    """)
    # password_rules
    cur.execute("""
        CREATE TABLE IF NOT EXISTS password_rules (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            min_length INTEGER,
            require_upper INTEGER,
            require_lower INTEGER,
            require_digit INTEGER,
            require_symbol INTEGER
        );
    """)
    conn.commit()
    conn.close()