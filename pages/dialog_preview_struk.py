from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QTextBrowser,
    QPushButton, QHBoxLayout
)
from PySide6.QtPrintSupport import QPrinter, QPrintDialog
from PySide6.QtGui import QTextDocument, QPageSize
from database import db


class PreviewStrukDialog(QDialog):
    def __init__(self, pesanan_id, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Preview Struk")
        self.resize(420, 520)

        self.pesanan_id = pesanan_id
        self.html_struk = ""

        # =========================
        # UI
        # =========================
        layout = QVBoxLayout(self)

        self.browser = QTextBrowser()
        layout.addWidget(self.browser)

        btnLayout = QHBoxLayout()
        self.btnCetak = QPushButton("🖨 Cetak")
        self.btnTutup = QPushButton("Tutup")

        self.btnCetak.clicked.connect(self.cetak)
        self.btnTutup.clicked.connect(self.close)

        btnLayout.addWidget(self.btnCetak)
        btnLayout.addWidget(self.btnTutup)

        layout.addLayout(btnLayout)

        self.load_data()

    # =========================
    # LOAD STRUK
    # =========================
    def load_data(self):
        db.cursor.execute("""
            SELECT nama_pelanggan, tanggal, total, metode
            FROM pesanan WHERE id=?
        """, (self.pesanan_id,))
        pesanan = db.cursor.fetchone()

        db.cursor.execute("""
            SELECT nama_produk, harga, qty, subtotal
            FROM pesanan_detail
            WHERE pesanan_id=?
        """, (self.pesanan_id,))
        items = db.cursor.fetchall()

        html = """
        <div style="font-family:Courier New; font-size:12px">
        <h3 style="text-align:center">TOKO SAYUR</h3>
        <div style="text-align:center">========================</div>
        """

        html += f"""
        <p>
        Tanggal : {pesanan[1]}<br>
        Pelanggan : {pesanan[0]}
        </p>
        <div>------------------------</div>
        """

        for nama, harga, qty, subtotal in items:
            html += f"""
            <div>
                {nama}<br>
                {qty} x {harga} = <b>{subtotal}</b>
            </div>
            """

        html += f"""
        <div>------------------------</div>
        <p>
        <b>TOTAL : Rp {pesanan[2]:,}</b><br>
        Metode : {pesanan[3]}
        </p>
        <div style="text-align:center">========================</div>
        <p style="text-align:center">Terima Kasih</p>
        </div>
        """

        self.html_struk = html
        self.browser.setHtml(html)

    # =========================
    # CETAK
    # =========================
    def cetak(self):
        printer = QPrinter(QPrinter.HighResolution)

        # ✅ QT6 CORRECT WAY
        printer.setPageSize(QPageSize(QPageSize.PageSizeId.A7))
        printer.setFullPage(True)

        dialog = QPrintDialog(printer, self)
        if dialog.exec():
            doc = QTextDocument()
            doc.setHtml(self.html_struk)
            doc.print(printer)
