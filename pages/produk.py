from PySide6.QtWidgets import (
    QTableWidgetItem, QMessageBox, QInputDialog
)
from PySide6.QtWidgets import QAbstractItemView
from database import db
from utils.table_action import TableActionBuilder


class ProdukPage:
    def __init__(self, ui):
        self.ui = ui
        self.table = ui.TableProduk

        self.setup_table()
        self.load_data()

        self.ui.btnTambahProduk.clicked.connect(self.tambah_produk)
        self.ui.inputSearchProduk.textChanged.connect(
            lambda text: self.search_by_name(text, 1)
        )
        self.ui.inputSearchProduk.setPlaceholderText("Cari nama produk...")

    # =========================
    # SETUP TABLE
    # =========================
    def setup_table(self):
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels([
            "ID", "Nama Produk", "Harga", "Stok", "Status", "Aksi"
        ])
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)

    # =========================
    # LOAD DATA
    # =========================
    def load_data(self):
        self.table.setRowCount(0)

        db.cursor.execute("""
            SELECT 
                id, 
                nama, 
                harga, 
                stok,
                CASE
                    WHEN stok <= 0 THEN 'Habis'
                    ELSE 'Aman'
                END as status
            FROM produk
            ORDER BY nama
        """)

        for data in db.cursor.fetchall():
            row = self.table.rowCount()
            self.table.insertRow(row)

            for col, val in enumerate(data):
                self.table.setItem(row, col, QTableWidgetItem(str(val)))

            self.add_action_buttons(row, data)

    # =========================
    # TAMBAH PRODUK
    # =========================
    def tambah_produk(self):
        nama, ok = QInputDialog.getText(
            None, "Tambah Produk", "Nama Produk:"
        )
        if not ok or not nama:
            return

        harga, ok = QInputDialog.getInt(
            None, "Tambah Produk", "Harga:", 10000, 0
        )
        if not ok:
            return

        stok, ok = QInputDialog.getInt(
            None, "Tambah Produk", "Stok Awal:", 1, 0
        )
        if not ok:
            return

        db.cursor.execute("""
            INSERT INTO produk (nama, harga, stok)
            VALUES (?, ?, ?)
        """, (nama, harga, stok))

        db.conn.commit()
        self.load_data()
        self.ui.main.stok.load_data()

    # =========================
    # EDIT PRODUK
    # =========================
    def edit_produk(self, data):
        harga_baru, ok = QInputDialog.getInt(
            None, "Edit Harga",
            "Harga Baru:", int(data[2]), 0
        )

        if ok:
            db.cursor.execute(
                "UPDATE produk SET harga=? WHERE id=?",
                (harga_baru, data[0])
            )
            db.conn.commit()
            self.load_data()
            self.ui.main.stok.load_data()

    # =========================
    # HAPUS PRODUK
    # =========================
    def hapus_produk(self, produk_id):
        reply = QMessageBox.question(
            None,
            "Hapus Produk",
            "Yakin ingin menghapus produk ini?",
            QMessageBox.Yes | QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            db.cursor.execute(
                "DELETE FROM produk WHERE id=?",
                (produk_id,)
            )
            db.conn.commit()
            self.load_data()
            self.ui.main.stok.load_data()

    # =========================
    # AKSI BUTTON
    # =========================
    def add_action_buttons(self, row, data):
        TableActionBuilder(self.table, row, 5) \
            .add_button("Edit", lambda _, d=data: self.edit_produk(d)) \
            .add_button("Hapus", lambda _, pid=data[0]: self.hapus_produk(pid)) \
            .build()

    # =========================
    # SEARCH
    # =========================
    def search_by_name(self, text, col):
        text = text.lower()
        for row in range(self.table.rowCount()):
            item = self.table.item(row, col)
            self.table.setRowHidden(
                row,
                text not in item.text().lower()
            )
