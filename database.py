import sqlite3
import os

os.makedirs("data", exist_ok=True)

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("data/app.db")
        self.cursor = self.conn.cursor()
        self.create_tables()
        self.create_default_user()  # ⬅️ PENTING

    def create_tables(self):
        # =========================
        # PRODUK
        # =========================
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS produk (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT,
            harga INTEGER,
            stok INTEGER,
            stok_min INTEGER DEFAULT 5
        )
        """)

        # =========================
        # PESANAN
        # =========================
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS pesanan (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama_pelanggan TEXT,
            tanggal TEXT,
            total INTEGER,
            metode TEXT,
            status TEXT
        )
        """)

        # =========================
        # DETAIL PESANAN
        # =========================
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS pesanan_detail (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pesanan_id INTEGER,
            nama_produk TEXT,
            harga INTEGER,
            qty INTEGER,
            subtotal INTEGER
        )
        """)

        # =========================
        # TRANSAKSI
        # =========================
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS transaksi (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pesanan_id INTEGER,
            total INTEGER,
            metode TEXT,
            tanggal TEXT
        )
        """)

        # =========================
        # USER (LOGIN)
        # =========================
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
        """)

        self.conn.commit()

    # =========================
    # AUTO CREATE ADMIN
    # =========================
    def create_default_user(self):
        self.cursor.execute("SELECT COUNT(*) FROM user")
        count = self.cursor.fetchone()[0]

        if count == 0:
            self.cursor.execute("""
                INSERT INTO user (username, password)
                VALUES ('admin', '123')
            """)
            self.conn.commit()
            print("✔ User default admin/admin berhasil dibuat")

# =========================
# INSTANCE DATABASE
# =========================
db = Database()
