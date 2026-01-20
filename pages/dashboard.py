from database import db

class DashboardPage:
    def __init__(self, ui):
        self.ui = ui
        self.refresh()

    def refresh(self):
        self.load_total_pesanan()
        self.load_total_transaksi()
        self.load_total_produk()
        self.load_total_stok()

    # ================= LOAD DATA =================

    def load_total_pesanan(self):
        result = db.cursor.execute("""
            SELECT COUNT(*) FROM pesanan
            WHERE status != 'batal'
        """).fetchone()
        self.ui.lblTotalPesanan.setText(str(result[0] or 0))

    def load_total_transaksi(self):
        result = db.cursor.execute(
            "SELECT COUNT(*) FROM transaksi"
        ).fetchone()
        self.ui.lblTotalTransaksi.setText(str(result[0] or 0))

    def load_total_produk(self):
        result = db.cursor.execute(
            "SELECT COUNT(*) FROM produk"
        ).fetchone()
        self.ui.lblTotalProduk.setText(str(result[0] or 0))

    def load_total_stok(self):
        result = db.cursor.execute(
            "SELECT SUM(stok) FROM produk"
        ).fetchone()
        self.ui.lblTotalStok.setText(str(result[0] or 0))
