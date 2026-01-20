from PySide6.QtWidgets import (
    QDialog, QLineEdit, QPushButton,
    QFormLayout, QHBoxLayout, QVBoxLayout, QMessageBox
)
from database import db


class DialogEditPesanan(QDialog):
    def __init__(self, pesanan_id):
        super().__init__()
        self.pesanan_id = pesanan_id
        self.setWindowTitle("Edit Pesanan")
        self.setFixedSize(350, 300)

        # INPUT
        self.inputNama = QLineEdit()
        self.inputTanggal = QLineEdit()
        self.inputProduk = QLineEdit()
        self.inputHarga = QLineEdit()
        self.inputQty = QLineEdit()

        self.load_data()

        # BUTTON
        btnSimpan = QPushButton("Simpan")
        btnBatal = QPushButton("Batal")

        btnSimpan.clicked.connect(self.simpan)
        btnBatal.clicked.connect(self.reject)

        # LAYOUT
        form = QFormLayout()
        form.addRow("Nama Pelanggan", self.inputNama)
        form.addRow("Tanggal", self.inputTanggal)
        form.addRow("Produk", self.inputProduk)
        form.addRow("Harga", self.inputHarga)
        form.addRow("Qty", self.inputQty)

        btnLayout = QHBoxLayout()
        btnLayout.addWidget(btnSimpan)
        btnLayout.addWidget(btnBatal)

        layout = QVBoxLayout(self)
        layout.addLayout(form)
        layout.addLayout(btnLayout)

    def load_data(self):
        db.cursor.execute("""
            SELECT nama_pelanggan, tanggal
            FROM pesanan WHERE id=?
        """, (self.pesanan_id,))
        p = db.cursor.fetchone()

        db.cursor.execute("""
            SELECT nama_produk, harga, qty
            FROM pesanan_detail WHERE pesanan_id=?
        """, (self.pesanan_id,))
        d = db.cursor.fetchone()

        self.inputNama.setText(p[0])
        self.inputTanggal.setText(p[1])
        self.inputProduk.setText(d[0])
        self.inputHarga.setText(str(d[1]))
        self.inputQty.setText(str(d[2]))

    def simpan(self):
        try:
            harga = int(self.inputHarga.text())
            qty = int(self.inputQty.text())
        except ValueError:
            QMessageBox.warning(self, "Error", "Harga & Qty harus angka")
            return

        subtotal = harga * qty

        # UPDATE PESANAN
        db.cursor.execute("""
            UPDATE pesanan
            SET nama_pelanggan=?, tanggal=?, total=?
            WHERE id=?
        """, (
            self.inputNama.text(),
            self.inputTanggal.text(),
            subtotal,
            self.pesanan_id
        ))

        # UPDATE DETAIL
        db.cursor.execute("""
            UPDATE pesanan_detail
            SET nama_produk=?, harga=?, qty=?, subtotal=?
            WHERE pesanan_id=?
        """, (
            self.inputProduk.text(),
            harga,
            qty,
            subtotal,
            self.pesanan_id
        ))

        db.conn.commit()
        self.accept()
