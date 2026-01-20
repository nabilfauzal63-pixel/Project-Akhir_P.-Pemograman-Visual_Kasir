from PySide6.QtWidgets import (
    QTableWidgetItem, QAbstractItemView,
    QMessageBox, QInputDialog
)
from database import db
from utils.table_action import TableActionBuilder


class StokPage:
    def __init__(self, ui):
        self.ui = ui
        self.table = ui.TableStok

        self.setup_table()
        self.load_data()

        self.ui.inputSearchStok.textChanged.connect(
            lambda text: self.search_by_name(text, 1)
        )
        self.ui.inputSearchStok.setPlaceholderText("Cari nama produk...")

    # =========================
    # SETUP TABLE
    # =========================
    def setup_table(self):
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels([
            "ID", "Nama Produk", "Stok", "Stok Minimum", "Status", "Aksi"
        ])
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)

    # =========================
    # LOAD DATA
    # =========================
    def load_data(self):
        self.table.setRowCount(0)

        db.cursor.execute("""
            SELECT id, nama, stok, stok_min,
                CASE
                    WHEN stok <= 0 THEN 'Habis'
                    WHEN stok <= stok_min THEN 'Hampir Habis'
                    ELSE 'Aman'
                END AS status
            FROM produk
            ORDER BY nama
        """)

        rows = db.cursor.fetchall()

        for data in rows:
            row = self.table.rowCount()
            self.table.insertRow(row)

            for col, val in enumerate(data):
                self.table.setItem(row, col, QTableWidgetItem(str(val)))

            self.add_action_buttons(row, data)

        self.cek_stok_warning()

    # =========================
    # AKSI
    # =========================
    def add_action_buttons(self, row, data):
        TableActionBuilder(self.table, row, 5) \
            .add_button("+", lambda _, pid=data[0]: self.update_stok(pid, True), "Tambah Stok") \
            .add_button("-", lambda _, pid=data[0]: self.update_stok(pid, False), "Kurangi Stok") \
            .build()

    # =========================
    # UPDATE STOK
    # =========================
    def update_stok(self, produk_id, tambah=True):
        jumlah, ok = QInputDialog.getInt(
            None, "Update Stok", "Jumlah:", 1, 1
        )
        if not ok:
            return

        if tambah:
            db.cursor.execute(
                "UPDATE produk SET stok = stok + ? WHERE id=?",
                (jumlah, produk_id)
            )
        else:
            db.cursor.execute(
                "UPDATE produk SET stok = stok - ? WHERE id=?",
                (jumlah, produk_id)
            )

        db.conn.commit()
        self.load_data()

    # =========================
    # WARNING STOK
    # =========================
    def cek_stok_warning(self):
        db.cursor.execute("""
            SELECT nama, stok, stok_min
            FROM produk
            WHERE stok <= stok_min
        """)

        result = db.cursor.fetchall()
        if not result:
            return

        pesan = "⚠ Stok menipis / habis:\n\n"
        for nama, stok, stok_min in result:
            status = "HABIS" if stok <= 0 else "HAMPIR HABIS"
            pesan += f"- {nama} ({stok}) → {status}\n"

        QMessageBox.warning(
            None,
            "Peringatan Stok",
            pesan
        )

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
