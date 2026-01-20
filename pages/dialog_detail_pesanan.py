from PySide6.QtWidgets import QDialog, QTableWidgetItem
from dialog_detail_pesanan_ui import Ui_Dialog
from database import db


class DetailPesananDialog(QDialog):
    def __init__(self, pesanan_id, parent=None):
        super().__init__(parent)

        self.pesanan_id = pesanan_id
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.setWindowTitle(f"Detail Pesanan #{pesanan_id}")
        self.ui.pushButton.clicked.connect(self.close)

        self.load_data()

    def load_data(self):
        self.ui.tableDetailPesanan.setRowCount(0)

        db.cursor.execute("""
            SELECT nama_produk, harga, qty, subtotal
            FROM pesanan_detail
            WHERE pesanan_id=?
        """, (self.pesanan_id,))

        for row_data in db.cursor.fetchall():
            row = self.ui.tableDetailPesanan.rowCount()
            self.ui.tableDetailPesanan.insertRow(row)

            for col, val in enumerate(row_data):
                self.ui.tableDetailPesanan.setItem(
                    row, col, QTableWidgetItem(str(val))
                )
