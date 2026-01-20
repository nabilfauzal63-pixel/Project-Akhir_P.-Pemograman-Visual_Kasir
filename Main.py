import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_Dashboard import Ui_MainWindow

from pages.dashboard import DashboardPage
from pages.produk import ProdukPage
from pages.stok import StokPage
from pages.pesanan import PesananPage
from pages.transaksi import TransaksiPage
from pages.laporan import LaporanPage
from pages.dashboard import DashboardPage
from PySide6.QtWidgets import QApplication, QDialog
from pages.dialog_login import LoginDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.main = self

        # Pages
        self.dashboard = DashboardPage(self.ui)
        self.produk = ProdukPage(self.ui)
        self.stok = StokPage(self.ui)
        self.pesanan = PesananPage(self.ui)
        self.transaksi = TransaksiPage(self.ui)
        self.laporan = LaporanPage(self.ui)

        self.setup_navigation()

    def setup_navigation(self):
        self.ui.btnDashboard_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Dashboard))
        self.ui.btnProduk_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Produk))
        self.ui.btnStok_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Stok))
        self.ui.btnPemesanan_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Pemesanan))
        self.ui.btnTransaksi_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Transaksi))
        self.ui.btnPenjualan_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Penjualan))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    login = LoginDialog()
    if login.exec() != QDialog.Accepted:
        sys.exit()

    window = MainWindow()
    window.show()

    sys.exit(app.exec())

