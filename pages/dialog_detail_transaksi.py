from PySide6.QtWidgets import QDialog, QLabel, QVBoxLayout, QPushButton

class DetailTransaksiDialog(QDialog):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Detail Transaksi")
        self.setFixedWidth(300)

        layout = QVBoxLayout(self)

        labels = [
            f"ID Transaksi : {data[0]}",
            f"ID Pesanan   : {data[1]}",
            f"Total        : Rp {data[2]}",
            f"Metode       : {data[3]}",
            f"Tanggal      : {data[4]}"
        ]

        for text in labels:
            lbl = QLabel(text)
            layout.addWidget(lbl)

        btn_close = QPushButton("Tutup")
        btn_close.clicked.connect(self.accept)
        layout.addWidget(btn_close)
