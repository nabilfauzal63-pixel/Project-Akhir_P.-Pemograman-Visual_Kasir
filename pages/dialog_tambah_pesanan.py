from PySide6.QtWidgets import (
    QDialog, QLabel, QLineEdit, QPushButton,
    QFormLayout, QHBoxLayout, QVBoxLayout, QMessageBox
)
from PySide6.QtCore import QDate


class DialogTambahPesanan(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tambah Pesanan")
        self.setFixedSize(350, 300)

        # ======================
        # INPUT
        # ======================
        self.inputNama = QLineEdit()
        self.inputTanggal = QLineEdit(
            QDate.currentDate().toString("yyyy-MM-dd")
        )
        self.inputProduk = QLineEdit()
        self.inputHarga = QLineEdit()
        self.inputQty = QLineEdit()

        # ======================
        # BUTTON
        # ======================
        btnSimpan = QPushButton("Simpan")
        btnBatal = QPushButton("Batal")

        btnSimpan.clicked.connect(self.validasi)
        btnBatal.clicked.connect(self.reject)

        # ======================
        # LAYOUT
        # ======================
        form = QFormLayout()
        form.addRow("Nama Pelanggan", self.inputNama)
        form.addRow("Tanggal", self.inputTanggal)
        form.addRow("Nama Produk", self.inputProduk)
        form.addRow("Harga", self.inputHarga)
        form.addRow("Qty", self.inputQty)

        btnLayout = QHBoxLayout()
        btnLayout.addWidget(btnSimpan)
        btnLayout.addWidget(btnBatal)

        layout = QVBoxLayout(self)
        layout.addLayout(form)
        layout.addLayout(btnLayout)

    # ======================
    # VALIDASI INPUT
    # ======================
    def validasi(self):
        if not self.inputNama.text():
            QMessageBox.warning(self, "Error", "Nama pelanggan wajib diisi")
            return

        if not self.inputProduk.text():
            QMessageBox.warning(self, "Error", "Nama produk wajib diisi")
            return

        try:
            int(self.inputHarga.text())
            int(self.inputQty.text())
        except ValueError:
            QMessageBox.warning(self, "Error", "Harga dan Qty harus angka")
            return

        self.accept()

    # ======================
    # AMBIL DATA
    # ======================
    def get_data(self):
        harga = int(self.inputHarga.text())
        qty = int(self.inputQty.text())

        return {
            "nama": self.inputNama.text(),
            "tanggal": self.inputTanggal.text(),
            "items": [
                {
                    "nama": self.inputProduk.text(),
                    "harga": harga,
                    "qty": qty,
                    "subtotal": harga * qty
                }
            ],
            "total": harga * qty
        }
