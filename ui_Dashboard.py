# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboard21.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCharts import QChartView
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDateEdit,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QStatusBar, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import icon

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(872, 759)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget_6 = QWidget(self.centralwidget)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(20, 0))
        self.widget_6.setStyleSheet(u"background-color: rgb(85, 255, 0);")
        self.btnMenu = QPushButton(self.widget_6)
        self.btnMenu.setObjectName(u"btnMenu")
        self.btnMenu.setGeometry(QRect(0, 340, 20, 16))
        self.btnMenu.setStyleSheet(u"border:none;\n"
"")
        icon = QIcon()
        icon.addFile(u":/newPrefix/Icon/menu2-removebg-preview.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnMenu.setIcon(icon)
        self.btnMenu.setCheckable(True)

        self.gridLayout.addWidget(self.widget_6, 0, 2, 1, 1)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(200, 16777215))
        self.widget_2.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(85, 255, 0);\n"
"}\n"
"\n"
"QPushButton {\n"
"	text-align: left;\n"
"	 height:30px;\n"
"	border:none;\n"
"	padding-left:10px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color:white;\n"
"	color:green;\n"
"	font-weight:bold;\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.iconSayur_2 = QLabel(self.widget_2)
        self.iconSayur_2.setObjectName(u"iconSayur_2")
        self.iconSayur_2.setMinimumSize(QSize(40, 40))
        self.iconSayur_2.setMaximumSize(QSize(40, 40))
        self.iconSayur_2.setStyleSheet(u"")
        self.iconSayur_2.setPixmap(QPixmap(u":/newPrefix/Icon/sayur-removebg-preview.png"))
        self.iconSayur_2.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.iconSayur_2)

        self.lblToko = QLabel(self.widget_2)
        self.lblToko.setObjectName(u"lblToko")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.lblToko.setFont(font)

        self.horizontalLayout_3.addWidget(self.lblToko)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btnDashboard_2 = QPushButton(self.widget_2)
        self.btnDashboard_2.setObjectName(u"btnDashboard_2")
        self.btnDashboard_2.setStyleSheet(u"color: rgb(0, 0, 0);")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/Icon/dashboard_16596683.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnDashboard_2.setIcon(icon1)
        self.btnDashboard_2.setCheckable(True)
        self.btnDashboard_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.btnDashboard_2)

        self.btnProduk_2 = QPushButton(self.widget_2)
        self.btnProduk_2.setObjectName(u"btnProduk_2")
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/Icon/produk-removebg-preview.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnProduk_2.setIcon(icon2)
        self.btnProduk_2.setCheckable(True)
        self.btnProduk_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.btnProduk_2)

        self.btnStok_2 = QPushButton(self.widget_2)
        self.btnStok_2.setObjectName(u"btnStok_2")
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/Icon/product_13368825.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnStok_2.setIcon(icon3)
        self.btnStok_2.setCheckable(True)
        self.btnStok_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.btnStok_2)

        self.btnPemesanan_2 = QPushButton(self.widget_2)
        self.btnPemesanan_2.setObjectName(u"btnPemesanan_2")
        icon4 = QIcon()
        icon4.addFile(u":/newPrefix/Icon/Pemesanan.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnPemesanan_2.setIcon(icon4)
        self.btnPemesanan_2.setCheckable(True)
        self.btnPemesanan_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.btnPemesanan_2)

        self.btnPenjualan_2 = QPushButton(self.widget_2)
        self.btnPenjualan_2.setObjectName(u"btnPenjualan_2")
        icon5 = QIcon()
        icon5.addFile(u":/newPrefix/Icon/Laporan-removebg-preview.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnPenjualan_2.setIcon(icon5)
        self.btnPenjualan_2.setCheckable(True)
        self.btnPenjualan_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.btnPenjualan_2)

        self.btnTransaksi_2 = QPushButton(self.widget_2)
        self.btnTransaksi_2.setObjectName(u"btnTransaksi_2")
        icon6 = QIcon()
        icon6.addFile(u":/newPrefix/Icon/transaksi2-removebg-preview.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnTransaksi_2.setIcon(icon6)
        self.btnTransaksi_2.setCheckable(True)
        self.btnTransaksi_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.btnTransaksi_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 332, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.btnKeluar_2 = QPushButton(self.widget_2)
        self.btnKeluar_2.setObjectName(u"btnKeluar_2")
        self.btnKeluar_2.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u":/newPrefix/Icon/keluar-removebg-preview.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnKeluar_2.setIcon(icon7)
        self.btnKeluar_2.setCheckable(True)

        self.verticalLayout_4.addWidget(self.btnKeluar_2)


        self.gridLayout.addWidget(self.widget_2, 0, 1, 1, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(70, 16777215))
        self.widget.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(85, 255, 0);\n"
"}\n"
"\n"
"QPushButton {\n"
"	height:30px;\n"
"	border:none;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color:white;\n"
"	color:green;\n"
"	font-weight:Bold;\n"
"}")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btnDashboard_1 = QPushButton(self.widget)
        self.btnDashboard_1.setObjectName(u"btnDashboard_1")
        self.btnDashboard_1.setIcon(icon1)
        self.btnDashboard_1.setCheckable(True)
        self.btnDashboard_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btnDashboard_1)

        self.btnProduk_1 = QPushButton(self.widget)
        self.btnProduk_1.setObjectName(u"btnProduk_1")
        self.btnProduk_1.setIcon(icon2)
        self.btnProduk_1.setCheckable(True)
        self.btnProduk_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btnProduk_1)

        self.btnPemesanan_1 = QPushButton(self.widget)
        self.btnPemesanan_1.setObjectName(u"btnPemesanan_1")
        self.btnPemesanan_1.setIcon(icon3)
        self.btnPemesanan_1.setCheckable(True)
        self.btnPemesanan_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btnPemesanan_1)

        self.btnStok_1 = QPushButton(self.widget)
        self.btnStok_1.setObjectName(u"btnStok_1")
        self.btnStok_1.setIcon(icon4)
        self.btnStok_1.setCheckable(True)
        self.btnStok_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btnStok_1)

        self.btnPenjualan_1 = QPushButton(self.widget)
        self.btnPenjualan_1.setObjectName(u"btnPenjualan_1")
        self.btnPenjualan_1.setIcon(icon5)
        self.btnPenjualan_1.setCheckable(True)
        self.btnPenjualan_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btnPenjualan_1)

        self.btnTransaksi_1 = QPushButton(self.widget)
        self.btnTransaksi_1.setObjectName(u"btnTransaksi_1")
        self.btnTransaksi_1.setIcon(icon6)
        self.btnTransaksi_1.setCheckable(True)
        self.btnTransaksi_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btnTransaksi_1)


        self.gridLayout_2.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.btnKeluar_1 = QPushButton(self.widget)
        self.btnKeluar_1.setObjectName(u"btnKeluar_1")
        self.btnKeluar_1.setStyleSheet(u"")
        self.btnKeluar_1.setIcon(icon7)
        self.btnKeluar_1.setCheckable(True)

        self.gridLayout_2.addWidget(self.btnKeluar_1, 3, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.iconSayur_1 = QLabel(self.widget)
        self.iconSayur_1.setObjectName(u"iconSayur_1")
        self.iconSayur_1.setMinimumSize(QSize(40, 40))
        self.iconSayur_1.setMaximumSize(QSize(40, 40))
        self.iconSayur_1.setStyleSheet(u"")
        self.iconSayur_1.setPixmap(QPixmap(u":/newPrefix/Icon/sayur-removebg-preview.png"))
        self.iconSayur_1.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.iconSayur_1)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 332, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"background-color: rgb(85, 255, 0);")
        self.verticalLayout_3 = QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.stackedWidget = QStackedWidget(self.widget_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"    background-color: #f0f2f5; \n"
"")
        self.Dashboard = QWidget()
        self.Dashboard.setObjectName(u"Dashboard")
        self.verticalLayout_5 = QVBoxLayout(self.Dashboard)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_3 = QFrame(self.Dashboard)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(350, 200))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.IconUtama = QLabel(self.frame_3)
        self.IconUtama.setObjectName(u"IconUtama")
        self.IconUtama.setStyleSheet(u"")
        self.IconUtama.setPixmap(QPixmap(u":/newPrefix/Icon/sayur.png"))
        self.IconUtama.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.IconUtama)


        self.verticalLayout_5.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.Dashboard)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(200, 50))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.widget_4 = QWidget(self.frame_2)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(350, 50))
        self.horizontalLayout = QHBoxLayout(self.widget_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.PencarianDashboard = QLineEdit(self.widget_4)
        self.PencarianDashboard.setObjectName(u"PencarianDashboard")
        self.PencarianDashboard.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.PencarianDashboard)

        self.btnPencariandashboard = QPushButton(self.widget_4)
        self.btnPencariandashboard.setObjectName(u"btnPencariandashboard")
        self.btnPencariandashboard.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon8 = QIcon()
        icon8.addFile(u":/newPrefix/Icon/search-removebg-preview.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnPencariandashboard.setIcon(icon8)

        self.horizontalLayout_2.addWidget(self.btnPencariandashboard)


        self.horizontalLayout.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_6.addWidget(self.widget_4)


        self.verticalLayout_5.addWidget(self.frame_2)

        self.frame = QFrame(self.Dashboard)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(350, 400))
        self.frame.setStyleSheet(u"/* --- GAYA UMUM UNTUK SEMUA CARD --- */\n"
"QFrame {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #e0e0e0;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"/* 1. TOTAL PEMESANAN (Warna Hijau - Fresh/Order Baru) */\n"
"QFrame#cardPemesanan {\n"
"    border-left: 5px solid #27ae60;\n"
"}\n"
"QFrame#cardPemesanan:hover {\n"
"    background-color: #f1f9f4;\n"
"    border: 1px solid #27ae60;\n"
"}\n"
"\n"
"/* 2. TOTAL TRANSAKSI (Warna Biru - Keuangan/Trust) */\n"
"QFrame#cardTransaksi {\n"
"    border-left: 5px solid #2980b9;\n"
"}\n"
"QFrame#cardTransaksi:hover {\n"
"    background-color: #f1f7fa;\n"
"    border: 1px solid #2980b9;\n"
"}\n"
"\n"
"/* 3. TOTAL PRODUK (Warna Oranye - Variasi/Aset) */\n"
"QFrame#cardProduk {\n"
"    border-left: 5px solid #f39c12;\n"
"}\n"
"QFrame#cardProduk:hover {\n"
"    background-color: #fff9f1;\n"
"    border: 1px solid #f39c12;\n"
"}\n"
"\n"
"/* 4. TOTAL STOK (Warna Merah/Maroon - Urgensi/Gudang) */\n"
"QFrame#cardStok {\n"
"    border-left: 5px solid #e74c3c;\n"
"}"
                        "\n"
"QFrame#cardStok:hover {\n"
"    background-color: #fdf2f1;\n"
"    border: 1px solid #e74c3c;\n"
"}\n"
"\n"
"/* --- STYLING TEKS DI DALAM CARD --- */\n"
"QLabel {\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"/* Judul Kategori (Gunakan objectName: lbl_judul) */\n"
"QLabel#lbl_judul {\n"
"    color: #7f8c8d;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"    text-transform: uppercase;\n"
"}\n"
"\n"
"/* Angka Statistik (Gunakan objectName: lbl_angka) */\n"
"QLabel#lbl_angka {\n"
"    color: #2c3e50;\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_8 = QGridLayout(self.frame)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.cardPemesanan = QFrame(self.frame)
        self.cardPemesanan.setObjectName(u"cardPemesanan")
        self.cardPemesanan.setStyleSheet(u"")
        self.cardPemesanan.setFrameShape(QFrame.Shape.StyledPanel)
        self.cardPemesanan.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.cardPemesanan)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.jdlTotalPemesanan = QLabel(self.cardPemesanan)
        self.jdlTotalPemesanan.setObjectName(u"jdlTotalPemesanan")
        self.jdlTotalPemesanan.setMinimumSize(QSize(30, 15))
        self.jdlTotalPemesanan.setMaximumSize(QSize(16777215, 17))
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        self.jdlTotalPemesanan.setFont(font1)
        self.jdlTotalPemesanan.setStyleSheet(u"color: #111827;")
        self.jdlTotalPemesanan.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.jdlTotalPemesanan, 0, 0, 1, 2)

        self.label_4 = QLabel(self.cardPemesanan)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(30, 27))
        self.label_4.setMaximumSize(QSize(50, 50))
        self.label_4.setPixmap(QPixmap(u":/newPrefix/Icon/keranjang-removebg-preview.png"))
        self.label_4.setScaledContents(True)

        self.gridLayout_4.addWidget(self.label_4, 1, 0, 1, 1)

        self.lblTotalPesanan = QLabel(self.cardPemesanan)
        self.lblTotalPesanan.setObjectName(u"lblTotalPesanan")
        font2 = QFont()
        font2.setBold(True)
        self.lblTotalPesanan.setFont(font2)
        self.lblTotalPesanan.setStyleSheet(u"QLabel {\n"
"    font-size: 28px;\n"
"    font-weight: bold;\n"
"	margin-left:5px;\n"
"}")

        self.gridLayout_4.addWidget(self.lblTotalPesanan, 1, 1, 1, 1)


        self.gridLayout_8.addWidget(self.cardPemesanan, 0, 0, 1, 1)

        self.cardTransaksi = QFrame(self.frame)
        self.cardTransaksi.setObjectName(u"cardTransaksi")
        self.cardTransaksi.setFrameShape(QFrame.Shape.StyledPanel)
        self.cardTransaksi.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.cardTransaksi)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.jdlTotalTransaksi = QLabel(self.cardTransaksi)
        self.jdlTotalTransaksi.setObjectName(u"jdlTotalTransaksi")
        self.jdlTotalTransaksi.setMaximumSize(QSize(16777215, 17))
        self.jdlTotalTransaksi.setFont(font1)
        self.jdlTotalTransaksi.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.jdlTotalTransaksi, 0, 0, 1, 2)

        self.label_2 = QLabel(self.cardTransaksi)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(30, 27))
        self.label_2.setMaximumSize(QSize(50, 50))
        self.label_2.setPixmap(QPixmap(u":/newPrefix/Icon/coin-removebg-preview.png"))
        self.label_2.setScaledContents(True)

        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)

        self.lblTotalTransaksi = QLabel(self.cardTransaksi)
        self.lblTotalTransaksi.setObjectName(u"lblTotalTransaksi")
        self.lblTotalTransaksi.setFont(font2)
        self.lblTotalTransaksi.setStyleSheet(u"QLabel {\n"
"    font-size: 28px;\n"
"    font-weight: bold;\n"
"	margin-left:5px;\n"
"}")

        self.gridLayout_3.addWidget(self.lblTotalTransaksi, 1, 1, 1, 1)


        self.gridLayout_8.addWidget(self.cardTransaksi, 0, 1, 1, 1)

        self.cardProduk = QFrame(self.frame)
        self.cardProduk.setObjectName(u"cardProduk")
        self.cardProduk.setFrameShape(QFrame.Shape.StyledPanel)
        self.cardProduk.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.cardProduk)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.jdlTotalProduk = QLabel(self.cardProduk)
        self.jdlTotalProduk.setObjectName(u"jdlTotalProduk")
        self.jdlTotalProduk.setMaximumSize(QSize(16777215, 17))
        self.jdlTotalProduk.setFont(font1)
        self.jdlTotalProduk.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.jdlTotalProduk, 0, 0, 1, 2)

        self.label_6 = QLabel(self.cardProduk)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(30, 27))
        self.label_6.setMaximumSize(QSize(50, 50))
        self.label_6.setPixmap(QPixmap(u":/newPrefix/Icon/buah-removebg-preview.png"))
        self.label_6.setScaledContents(True)

        self.gridLayout_5.addWidget(self.label_6, 1, 0, 1, 1)

        self.lblTotalProduk = QLabel(self.cardProduk)
        self.lblTotalProduk.setObjectName(u"lblTotalProduk")
        self.lblTotalProduk.setFont(font2)
        self.lblTotalProduk.setStyleSheet(u"QLabel {\n"
"    font-size: 28px;\n"
"    font-weight: bold;\n"
"	margin-left:5px;\n"
"}")

        self.gridLayout_5.addWidget(self.lblTotalProduk, 1, 1, 1, 1)


        self.gridLayout_8.addWidget(self.cardProduk, 1, 0, 1, 1)

        self.cardStok = QFrame(self.frame)
        self.cardStok.setObjectName(u"cardStok")
        self.cardStok.setFrameShape(QFrame.Shape.StyledPanel)
        self.cardStok.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_7 = QGridLayout(self.cardStok)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.jdlTotalStok = QLabel(self.cardStok)
        self.jdlTotalStok.setObjectName(u"jdlTotalStok")
        self.jdlTotalStok.setMaximumSize(QSize(16777215, 17))
        self.jdlTotalStok.setFont(font1)
        self.jdlTotalStok.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_7.addWidget(self.jdlTotalStok, 0, 0, 1, 2)

        self.label_10 = QLabel(self.cardStok)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(30, 27))
        self.label_10.setMaximumSize(QSize(50, 50))
        self.label_10.setPixmap(QPixmap(u":/newPrefix/Icon/stok_buah_2-removebg-preview.png"))
        self.label_10.setScaledContents(True)

        self.gridLayout_7.addWidget(self.label_10, 1, 0, 1, 1)

        self.lblTotalStok = QLabel(self.cardStok)
        self.lblTotalStok.setObjectName(u"lblTotalStok")
        self.lblTotalStok.setFont(font2)
        self.lblTotalStok.setStyleSheet(u"QLabel {\n"
"    font-size: 28px;\n"
"    font-weight: bold;\n"
"	margin-left:5px;\n"
"}")

        self.gridLayout_7.addWidget(self.lblTotalStok, 1, 1, 1, 1)


        self.gridLayout_8.addWidget(self.cardStok, 1, 1, 1, 1)


        self.verticalLayout_5.addWidget(self.frame)

        self.stackedWidget.addWidget(self.Dashboard)
        self.Pemesanan = QWidget()
        self.Pemesanan.setObjectName(u"Pemesanan")
        self.verticalLayout_29 = QVBoxLayout(self.Pemesanan)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.frame_24 = QFrame(self.Pemesanan)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_24.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_24)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_25 = QFrame(self.frame_24)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_25.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_25)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.Judul_pesanan = QLabel(self.frame_25)
        self.Judul_pesanan.setObjectName(u"Judul_pesanan")
        font3 = QFont()
        font3.setPointSize(20)
        self.Judul_pesanan.setFont(font3)
        self.Judul_pesanan.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.Judul_pesanan.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_28.addWidget(self.Judul_pesanan)

        self.subjudul_pesanan = QLabel(self.frame_25)
        self.subjudul_pesanan.setObjectName(u"subjudul_pesanan")
        font4 = QFont()
        font4.setPointSize(11)
        self.subjudul_pesanan.setFont(font4)
        self.subjudul_pesanan.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.subjudul_pesanan.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_28.addWidget(self.subjudul_pesanan)


        self.verticalLayout_11.addWidget(self.frame_25)


        self.verticalLayout_29.addWidget(self.frame_24)

        self.widget_10 = QWidget(self.Pemesanan)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setMinimumSize(QSize(350, 0))
        self.widget_10.setStyleSheet(u"QPushButton:Checked {\n"
"	background-color: white; \n"
"	font-weight: bold;\n"
"}")
        self.horizontalLayout_21 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.inputNamaPelanggan = QLineEdit(self.widget_10)
        self.inputNamaPelanggan.setObjectName(u"inputNamaPelanggan")
        self.inputNamaPelanggan.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_22.addWidget(self.inputNamaPelanggan)

        self.btnPencarianPesanan = QPushButton(self.widget_10)
        self.btnPencarianPesanan.setObjectName(u"btnPencarianPesanan")
        self.btnPencarianPesanan.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.btnPencarianPesanan.setIcon(icon8)

        self.horizontalLayout_22.addWidget(self.btnPencarianPesanan)


        self.horizontalLayout_21.addLayout(self.horizontalLayout_22)

        self.btnTambahPesanan = QPushButton(self.widget_10)
        self.btnTambahPesanan.setObjectName(u"btnTambahPesanan")
        self.btnTambahPesanan.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(0, 85, 255);\n"
"	color:white;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: White;\n"
"	color: black;\n"
"	font-weight: bold;\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/newPrefix/Icon/tambah3-removebg-preview.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnTambahPesanan.setIcon(icon9)

        self.horizontalLayout_21.addWidget(self.btnTambahPesanan)


        self.verticalLayout_29.addWidget(self.widget_10)

        self.frame_23 = QFrame(self.Pemesanan)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_23)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.TablePesanan = QTableWidget(self.frame_23)
        if (self.TablePesanan.columnCount() < 7):
            self.TablePesanan.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.TablePesanan.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.TablePesanan.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.TablePesanan.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.TablePesanan.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.TablePesanan.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.TablePesanan.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.TablePesanan.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        if (self.TablePesanan.rowCount() < 3):
            self.TablePesanan.setRowCount(3)
        self.TablePesanan.setObjectName(u"TablePesanan")
        self.TablePesanan.setStyleSheet(u"/* Warna dasar tabel */\n"
"QTableWidget {\n"
"    background-color: #ffffff;\n"
"    alternate-background-color: #f9f9f9; /* Warna baris selang-seling */\n"
"    gridline-color: #dcdcdc;\n"
"    color: #333333;\n"
"    selection-background-color: #27ae60; /* Warna hijau saat baris diklik */\n"
"    selection-color: white;\n"
"}\n"
"\n"
"/* Warna Header (Kolom Atas) */\n"
"QHeaderView::section {\n"
"    background-color: #27ae60; /* Hijau sesuai tema Toko Sayur Anda */\n"
"    color: white;\n"
"    padding: 5px;\n"
"    font-weight: bold;\n"
"    border: 1px solid #2ecc71;\n"
"}\n"
"\n"
"/* Menghilangkan border kaku di sekeliling tabel */\n"
"QTableWidget {\n"
"    border: 1px solid #ced4da;\n"
"    border-radius: 5px;\n"
"}")
        self.TablePesanan.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.TablePesanan.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.TablePesanan.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.TablePesanan.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_27.addWidget(self.TablePesanan)


        self.verticalLayout_29.addWidget(self.frame_23)

        self.stackedWidget.addWidget(self.Pemesanan)
        self.Stok = QWidget()
        self.Stok.setObjectName(u"Stok")
        self.verticalLayout_21 = QVBoxLayout(self.Stok)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.frame_28 = QFrame(self.Stok)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_28.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_28)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.frame_29 = QFrame(self.frame_28)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_29.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_29)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.Judul_produk = QLabel(self.frame_29)
        self.Judul_produk.setObjectName(u"Judul_produk")
        self.Judul_produk.setFont(font3)
        self.Judul_produk.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.Judul_produk.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_31.addWidget(self.Judul_produk)

        self.subjudul_produk = QLabel(self.frame_29)
        self.subjudul_produk.setObjectName(u"subjudul_produk")
        self.subjudul_produk.setFont(font4)
        self.subjudul_produk.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.subjudul_produk.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_31.addWidget(self.subjudul_produk)


        self.verticalLayout_22.addWidget(self.frame_29)


        self.verticalLayout_21.addWidget(self.frame_28)

        self.frame_18 = QFrame(self.Stok)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_18)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.widget_8 = QWidget(self.frame_18)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMinimumSize(QSize(350, 0))
        self.widget_8.setStyleSheet(u"QPushButton:Checked {\n"
"	background-color: white; \n"
"	font-weight: bold;\n"
"}")
        self.horizontalLayout_16 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.inputSearchStok = QLineEdit(self.widget_8)
        self.inputSearchStok.setObjectName(u"inputSearchStok")
        self.inputSearchStok.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_17.addWidget(self.inputSearchStok)

        self.btnPencarianStok = QPushButton(self.widget_8)
        self.btnPencarianStok.setObjectName(u"btnPencarianStok")
        self.btnPencarianStok.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.btnPencarianStok.setIcon(icon8)

        self.horizontalLayout_17.addWidget(self.btnPencarianStok)


        self.horizontalLayout_16.addLayout(self.horizontalLayout_17)

        self.btnTambahStok = QPushButton(self.widget_8)
        self.btnTambahStok.setObjectName(u"btnTambahStok")
        self.btnTambahStok.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(0, 85, 255);\n"
"	color:white;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: White;\n"
"	color: black;\n"
"	font-weight: bold;\n"
"}")
        self.btnTambahStok.setIcon(icon9)

        self.horizontalLayout_16.addWidget(self.btnTambahStok)

        self.comboBoxStok = QComboBox(self.widget_8)
        self.comboBoxStok.addItem("")
        self.comboBoxStok.addItem("")
        self.comboBoxStok.addItem("")
        self.comboBoxStok.addItem("")
        self.comboBoxStok.setObjectName(u"comboBoxStok")
        self.comboBoxStok.setMinimumSize(QSize(100, 0))
        self.comboBoxStok.setMaximumSize(QSize(30, 16777215))
        self.comboBoxStok.setStyleSheet(u"QComboBox {\n"
"	selection-background-color: rgb(0, 85, 255);\n"
"	background-color: white;\n"
"	border: 2px solid black;\n"
"}")
        self.comboBoxStok.setEditable(False)

        self.horizontalLayout_16.addWidget(self.comboBoxStok)


        self.verticalLayout_20.addWidget(self.widget_8, 0, Qt.AlignmentFlag.AlignBottom)

        self.TableStok = QTableWidget(self.frame_18)
        if (self.TableStok.columnCount() < 5):
            self.TableStok.setColumnCount(5)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.TableStok.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.TableStok.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.TableStok.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.TableStok.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.TableStok.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        if (self.TableStok.rowCount() < 3):
            self.TableStok.setRowCount(3)
        self.TableStok.setObjectName(u"TableStok")
        self.TableStok.setStyleSheet(u"/* Warna dasar tabel */\n"
"QTableWidget {\n"
"    background-color: #ffffff;\n"
"    alternate-background-color: #f9f9f9; /* Warna baris selang-seling */\n"
"    gridline-color: #dcdcdc;\n"
"    color: #333333;\n"
"    selection-background-color: #27ae60; /* Warna hijau saat baris diklik */\n"
"    selection-color: white;\n"
"}\n"
"\n"
"/* Warna Header (Kolom Atas) */\n"
"QHeaderView::section {\n"
"    background-color: #27ae60; /* Hijau sesuai tema Toko Sayur Anda */\n"
"    color: white;\n"
"    padding: 5px;\n"
"    font-weight: bold;\n"
"    border: 1px solid #2ecc71;\n"
"}\n"
"\n"
"/* Menghilangkan border kaku di sekeliling tabel */\n"
"QTableWidget {\n"
"    border: 1px solid #ced4da;\n"
"    border-radius: 5px;\n"
"}")
        self.TableStok.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.TableStok.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.TableStok.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.TableStok.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_20.addWidget(self.TableStok)


        self.verticalLayout_21.addWidget(self.frame_18)

        self.stackedWidget.addWidget(self.Stok)
        self.Penjualan = QWidget()
        self.Penjualan.setObjectName(u"Penjualan")
        self.verticalLayout_6 = QVBoxLayout(self.Penjualan)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_4 = QFrame(self.Penjualan)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_7)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.Judul_penjualan = QLabel(self.frame_7)
        self.Judul_penjualan.setObjectName(u"Judul_penjualan")
        self.Judul_penjualan.setFont(font3)
        self.Judul_penjualan.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.Judul_penjualan.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.Judul_penjualan)

        self.subjudul_penjualan = QLabel(self.frame_7)
        self.subjudul_penjualan.setObjectName(u"subjudul_penjualan")
        self.subjudul_penjualan.setFont(font4)
        self.subjudul_penjualan.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.subjudul_penjualan.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.subjudul_penjualan)


        self.verticalLayout_7.addWidget(self.frame_7)


        self.verticalLayout_6.addWidget(self.frame_4)

        self.frame_6 = QFrame(self.Penjualan)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"background-color:#f4f7f6;")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_9)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.LblDari = QLabel(self.frame_9)
        self.LblDari.setObjectName(u"LblDari")

        self.verticalLayout_8.addWidget(self.LblDari)

        self.dateFromLaporan = QDateEdit(self.frame_9)
        self.dateFromLaporan.setObjectName(u"dateFromLaporan")
        self.dateFromLaporan.setMinimumSize(QSize(10, 25))
        self.dateFromLaporan.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;")

        self.verticalLayout_8.addWidget(self.dateFromLaporan)


        self.verticalLayout_13.addLayout(self.verticalLayout_8)


        self.horizontalLayout_8.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_8)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_10)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.LblKe = QLabel(self.frame_10)
        self.LblKe.setObjectName(u"LblKe")

        self.verticalLayout_12.addWidget(self.LblKe)

        self.dateToLaporan = QDateEdit(self.frame_10)
        self.dateToLaporan.setObjectName(u"dateToLaporan")
        self.dateToLaporan.setMinimumSize(QSize(10, 25))
        self.dateToLaporan.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;")

        self.verticalLayout_12.addWidget(self.dateToLaporan)


        self.verticalLayout_14.addLayout(self.verticalLayout_12)


        self.horizontalLayout_8.addWidget(self.frame_10)

        self.frame_13 = QFrame(self.frame_8)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.cmbMetodeLaporan = QComboBox(self.frame_13)
        self.cmbMetodeLaporan.addItem("")
        self.cmbMetodeLaporan.addItem("")
        self.cmbMetodeLaporan.addItem("")
        self.cmbMetodeLaporan.setObjectName(u"cmbMetodeLaporan")
        self.cmbMetodeLaporan.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_12.addWidget(self.cmbMetodeLaporan)

        self.btnTampilkanLaporan = QPushButton(self.frame_13)
        self.btnTampilkanLaporan.setObjectName(u"btnTampilkanLaporan")

        self.horizontalLayout_12.addWidget(self.btnTampilkanLaporan)


        self.horizontalLayout_8.addWidget(self.frame_13)


        self.verticalLayout_9.addWidget(self.frame_8)

        self.frame_14 = QFrame(self.frame_6)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(350, 50))
        self.frame_14.setStyleSheet(u"QPushButton:Checked {\n"
"	background-color: white;\n"
"	font-weight: Bold;\n"
"}")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.btnViewTable = QPushButton(self.frame_14)
        self.btnViewTable.setObjectName(u"btnViewTable")
        self.btnViewTable.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.btnViewTable.setCheckable(True)
        self.btnViewTable.setAutoExclusive(True)

        self.horizontalLayout_9.addWidget(self.btnViewTable)

        self.btnViewChart = QPushButton(self.frame_14)
        self.btnViewChart.setObjectName(u"btnViewChart")
        self.btnViewChart.setStyleSheet(u"background-color: rgb(0, 255, 255);")
        self.btnViewChart.setCheckable(True)
        self.btnViewChart.setAutoExclusive(True)

        self.horizontalLayout_9.addWidget(self.btnViewChart)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.PencarianLaporan = QLineEdit(self.frame_14)
        self.PencarianLaporan.setObjectName(u"PencarianLaporan")
        self.PencarianLaporan.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;")

        self.horizontalLayout_7.addWidget(self.PencarianLaporan)

        self.btnPencarianLaporan = QPushButton(self.frame_14)
        self.btnPencarianLaporan.setObjectName(u"btnPencarianLaporan")
        self.btnPencarianLaporan.setMinimumSize(QSize(10, 10))
        self.btnPencarianLaporan.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.btnPencarianLaporan.setIcon(icon8)

        self.horizontalLayout_7.addWidget(self.btnPencarianLaporan)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_7)


        self.verticalLayout_9.addWidget(self.frame_14, 0, Qt.AlignmentFlag.AlignTop)

        self.frame_11 = QFrame(self.frame_6)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy)
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.stackedLaporan = QStackedWidget(self.frame_11)
        self.stackedLaporan.setObjectName(u"stackedLaporan")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_15 = QVBoxLayout(self.page)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.tableLaporanPenjualan = QTableWidget(self.page)
        if (self.tableLaporanPenjualan.columnCount() < 5):
            self.tableLaporanPenjualan.setColumnCount(5)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableLaporanPenjualan.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableLaporanPenjualan.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableLaporanPenjualan.setHorizontalHeaderItem(2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableLaporanPenjualan.setHorizontalHeaderItem(3, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableLaporanPenjualan.setHorizontalHeaderItem(4, __qtablewidgetitem16)
        if (self.tableLaporanPenjualan.rowCount() < 3):
            self.tableLaporanPenjualan.setRowCount(3)
        self.tableLaporanPenjualan.setObjectName(u"tableLaporanPenjualan")
        self.tableLaporanPenjualan.setStyleSheet(u"/* Warna dasar tabel */\n"
"QTableWidget {\n"
"    background-color: #ffffff;\n"
"    alternate-background-color: #f9f9f9; /* Warna baris selang-seling */\n"
"    gridline-color: #dcdcdc;\n"
"    color: #333333;\n"
"    selection-background-color: #27ae60; /* Warna hijau saat baris diklik */\n"
"    selection-color: white;\n"
"}\n"
"\n"
"/* Warna Header (Kolom Atas) */\n"
"QHeaderView::section {\n"
"    background-color: #27ae60; /* Hijau sesuai tema Toko Sayur Anda */\n"
"    color: white;\n"
"    padding: 5px;\n"
"    font-weight: bold;\n"
"    border: 1px solid #2ecc71;\n"
"}\n"
"\n"
"/* Menghilangkan border kaku di sekeliling tabel */\n"
"QTableWidget {\n"
"    border: 1px solid #ced4da;\n"
"    border-radius: 5px;\n"
"}")

        self.verticalLayout_15.addWidget(self.tableLaporanPenjualan)

        self.stackedLaporan.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_23 = QVBoxLayout(self.page_2)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.chartViewPenjualan = QChartView(self.page_2)
        self.chartViewPenjualan.setObjectName(u"chartViewPenjualan")

        self.verticalLayout_23.addWidget(self.chartViewPenjualan)

        self.stackedLaporan.addWidget(self.page_2)

        self.horizontalLayout_10.addWidget(self.stackedLaporan)


        self.verticalLayout_9.addWidget(self.frame_11)


        self.verticalLayout_6.addWidget(self.frame_6)

        self.frame_5 = QFrame(self.Penjualan)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_6.addWidget(self.frame_5)

        self.stackedWidget.addWidget(self.Penjualan)
        self.Transaksi = QWidget()
        self.Transaksi.setObjectName(u"Transaksi")
        self.verticalLayout_26 = QVBoxLayout(self.Transaksi)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.frame_21 = QFrame(self.Transaksi)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_21.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_21)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.frame_22 = QFrame(self.frame_21)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_22.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_22)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.Judul_Transaksi = QLabel(self.frame_22)
        self.Judul_Transaksi.setObjectName(u"Judul_Transaksi")
        self.Judul_Transaksi.setFont(font3)
        self.Judul_Transaksi.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.Judul_Transaksi.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_25.addWidget(self.Judul_Transaksi)

        self.subjudul_Transaksi = QLabel(self.frame_22)
        self.subjudul_Transaksi.setObjectName(u"subjudul_Transaksi")
        self.subjudul_Transaksi.setFont(font4)
        self.subjudul_Transaksi.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.subjudul_Transaksi.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_25.addWidget(self.subjudul_Transaksi)


        self.verticalLayout_24.addWidget(self.frame_22)


        self.verticalLayout_26.addWidget(self.frame_21)

        self.frame_20 = QFrame(self.Transaksi)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_20)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.widget_9 = QWidget(self.frame_20)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMinimumSize(QSize(350, 0))
        self.widget_9.setStyleSheet(u"QPushButton:Checked {\n"
"	background-color: white; \n"
"	font-weight: bold;\n"
"}")
        self.gridLayout_6 = QGridLayout(self.widget_9)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.btnFilterTransaksi = QPushButton(self.widget_9)
        self.btnFilterTransaksi.setObjectName(u"btnFilterTransaksi")

        self.horizontalLayout_11.addWidget(self.btnFilterTransaksi)

        self.btnResetFilterTransaksi = QPushButton(self.widget_9)
        self.btnResetFilterTransaksi.setObjectName(u"btnResetFilterTransaksi")

        self.horizontalLayout_11.addWidget(self.btnResetFilterTransaksi)


        self.gridLayout_6.addLayout(self.horizontalLayout_11, 0, 0, 1, 1)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.dateFromTransaksi = QDateEdit(self.widget_9)
        self.dateFromTransaksi.setObjectName(u"dateFromTransaksi")
        self.dateFromTransaksi.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;")

        self.horizontalLayout_18.addWidget(self.dateFromTransaksi)

        self.dateToTransaksi = QDateEdit(self.widget_9)
        self.dateToTransaksi.setObjectName(u"dateToTransaksi")
        self.dateToTransaksi.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;")

        self.horizontalLayout_18.addWidget(self.dateToTransaksi)

        self.cmbMetodeTransaksi = QComboBox(self.widget_9)
        self.cmbMetodeTransaksi.addItem("")
        self.cmbMetodeTransaksi.addItem("")
        self.cmbMetodeTransaksi.addItem("")
        self.cmbMetodeTransaksi.setObjectName(u"cmbMetodeTransaksi")
        self.cmbMetodeTransaksi.setMinimumSize(QSize(100, 0))
        self.cmbMetodeTransaksi.setMaximumSize(QSize(30, 16777215))
        self.cmbMetodeTransaksi.setStyleSheet(u"QComboBox {\n"
"	selection-background-color: rgb(0, 85, 255);\n"
"	background-color: white;\n"
"	border: 2px solid black;\n"
"}")
        self.cmbMetodeTransaksi.setEditable(False)

        self.horizontalLayout_18.addWidget(self.cmbMetodeTransaksi)


        self.gridLayout_6.addLayout(self.horizontalLayout_18, 0, 1, 2, 1)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.inputSearchTransaksi = QLineEdit(self.widget_9)
        self.inputSearchTransaksi.setObjectName(u"inputSearchTransaksi")
        self.inputSearchTransaksi.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;")

        self.horizontalLayout_19.addWidget(self.inputSearchTransaksi)

        self.btnPencarianTransaksi = QPushButton(self.widget_9)
        self.btnPencarianTransaksi.setObjectName(u"btnPencarianTransaksi")
        self.btnPencarianTransaksi.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.btnPencarianTransaksi.setIcon(icon8)

        self.horizontalLayout_19.addWidget(self.btnPencarianTransaksi)


        self.gridLayout_6.addLayout(self.horizontalLayout_19, 1, 0, 1, 1)


        self.verticalLayout_16.addWidget(self.widget_9)

        self.TableTransaksi = QTableWidget(self.frame_20)
        if (self.TableTransaksi.columnCount() < 6):
            self.TableTransaksi.setColumnCount(6)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.TableTransaksi.setHorizontalHeaderItem(0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.TableTransaksi.setHorizontalHeaderItem(1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.TableTransaksi.setHorizontalHeaderItem(2, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.TableTransaksi.setHorizontalHeaderItem(3, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.TableTransaksi.setHorizontalHeaderItem(4, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.TableTransaksi.setHorizontalHeaderItem(5, __qtablewidgetitem22)
        if (self.TableTransaksi.rowCount() < 3):
            self.TableTransaksi.setRowCount(3)
        self.TableTransaksi.setObjectName(u"TableTransaksi")
        self.TableTransaksi.setStyleSheet(u"/* Warna dasar tabel */\n"
"QTableWidget {\n"
"    background-color: #ffffff;\n"
"    alternate-background-color: #f9f9f9; /* Warna baris selang-seling */\n"
"    gridline-color: #dcdcdc;\n"
"    color: #333333;\n"
"    selection-background-color: #27ae60; /* Warna hijau saat baris diklik */\n"
"    selection-color: white;\n"
"}\n"
"\n"
"/* Warna Header (Kolom Atas) */\n"
"QHeaderView::section {\n"
"    background-color: #27ae60; /* Hijau sesuai tema Toko Sayur Anda */\n"
"    color: white;\n"
"    padding: 5px;\n"
"    font-weight: bold;\n"
"    border: 1px solid #2ecc71;\n"
"}\n"
"\n"
"/* Menghilangkan border kaku di sekeliling tabel */\n"
"QTableWidget {\n"
"    border: 1px solid #ced4da;\n"
"    border-radius: 5px;\n"
"}")
        self.TableTransaksi.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.TableTransaksi.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.TableTransaksi.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.TableTransaksi.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_16.addWidget(self.TableTransaksi)

        self.btnPDF = QPushButton(self.frame_20)
        self.btnPDF.setObjectName(u"btnPDF")
        self.btnPDF.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;")

        self.verticalLayout_16.addWidget(self.btnPDF)


        self.verticalLayout_26.addWidget(self.frame_20)

        self.stackedWidget.addWidget(self.Transaksi)
        self.Produk = QWidget()
        self.Produk.setObjectName(u"Produk")
        self.verticalLayout_18 = QVBoxLayout(self.Produk)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_26 = QFrame(self.Produk)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_26.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_26)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame_27 = QFrame(self.frame_26)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_27.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_27)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.Judul_Produk = QLabel(self.frame_27)
        self.Judul_Produk.setObjectName(u"Judul_Produk")
        self.Judul_Produk.setFont(font3)
        self.Judul_Produk.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.Judul_Produk.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_30.addWidget(self.Judul_Produk)

        self.subjudul_Produk = QLabel(self.frame_27)
        self.subjudul_Produk.setObjectName(u"subjudul_Produk")
        self.subjudul_Produk.setFont(font4)
        self.subjudul_Produk.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.subjudul_Produk.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_30.addWidget(self.subjudul_Produk)


        self.verticalLayout_17.addWidget(self.frame_27)


        self.verticalLayout_18.addWidget(self.frame_26)

        self.frame_17 = QFrame(self.Produk)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_17)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.widget_7 = QWidget(self.frame_17)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(350, 0))
        self.widget_7.setStyleSheet(u"QPushButton:Checked {\n"
"	background-color: white; \n"
"	font-weight: bold;\n"
"}")
        self.horizontalLayout_15 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.inputSearchProduk = QLineEdit(self.widget_7)
        self.inputSearchProduk.setObjectName(u"inputSearchProduk")
        self.inputSearchProduk.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_14.addWidget(self.inputSearchProduk)

        self.btnPencarianProduk = QPushButton(self.widget_7)
        self.btnPencarianProduk.setObjectName(u"btnPencarianProduk")
        self.btnPencarianProduk.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.btnPencarianProduk.setIcon(icon8)

        self.horizontalLayout_14.addWidget(self.btnPencarianProduk)


        self.horizontalLayout_15.addLayout(self.horizontalLayout_14)

        self.btnTambahProduk = QPushButton(self.widget_7)
        self.btnTambahProduk.setObjectName(u"btnTambahProduk")
        self.btnTambahProduk.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(0, 85, 255);\n"
"	color:white;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: White;\n"
"	color: black;\n"
"	font-weight: bold;\n"
"}")
        self.btnTambahProduk.setIcon(icon9)

        self.horizontalLayout_15.addWidget(self.btnTambahProduk)


        self.verticalLayout_19.addWidget(self.widget_7, 0, Qt.AlignmentFlag.AlignBottom)

        self.TableProduk = QTableWidget(self.frame_17)
        if (self.TableProduk.columnCount() < 6):
            self.TableProduk.setColumnCount(6)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.TableProduk.setHorizontalHeaderItem(0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.TableProduk.setHorizontalHeaderItem(1, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.TableProduk.setHorizontalHeaderItem(2, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.TableProduk.setHorizontalHeaderItem(3, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.TableProduk.setHorizontalHeaderItem(4, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.TableProduk.setHorizontalHeaderItem(5, __qtablewidgetitem28)
        if (self.TableProduk.rowCount() < 3):
            self.TableProduk.setRowCount(3)
        self.TableProduk.setObjectName(u"TableProduk")
        self.TableProduk.setStyleSheet(u"/* Warna dasar tabel */\n"
"QTableWidget {\n"
"    background-color: #ffffff;\n"
"    alternate-background-color: #f9f9f9; /* Warna baris selang-seling */\n"
"    gridline-color: #dcdcdc;\n"
"    color: #333333;\n"
"    selection-background-color: #27ae60; /* Warna hijau saat baris diklik */\n"
"    selection-color: white;\n"
"}\n"
"\n"
"/* Warna Header (Kolom Atas) */\n"
"QHeaderView::section {\n"
"    background-color: #27ae60; /* Hijau sesuai tema Toko Sayur Anda */\n"
"    color: white;\n"
"    padding: 5px;\n"
"    font-weight: bold;\n"
"    border: 1px solid #2ecc71;\n"
"}\n"
"\n"
"/* Menghilangkan border kaku di sekeliling tabel */\n"
"QTableWidget {\n"
"    border: 1px solid #ced4da;\n"
"    border-radius: 5px;\n"
"}")
        self.TableProduk.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.TableProduk.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.TableProduk.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_19.addWidget(self.TableProduk)


        self.verticalLayout_18.addWidget(self.frame_17)

        self.stackedWidget.addWidget(self.Produk)

        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.widget_3, 0, 4, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 872, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.btnMenu.toggled.connect(self.widget.setHidden)
        self.btnMenu.toggled.connect(self.widget_2.setVisible)
        self.btnTransaksi_1.toggled.connect(self.btnTransaksi_2.setChecked)
        self.btnPemesanan_1.toggled.connect(self.btnStok_2.setChecked)
        self.btnPenjualan_1.toggled.connect(self.btnPenjualan_2.setChecked)
        self.btnStok_1.toggled.connect(self.btnPemesanan_2.setChecked)
        self.btnProduk_1.toggled.connect(self.btnProduk_2.setChecked)
        self.btnDashboard_1.toggled.connect(self.btnDashboard_2.setChecked)
        self.btnDashboard_2.toggled.connect(self.btnDashboard_1.setChecked)
        self.btnProduk_2.toggled.connect(self.btnProduk_1.setChecked)
        self.btnPemesanan_2.toggled.connect(self.btnStok_1.setChecked)
        self.btnPenjualan_2.toggled.connect(self.btnPenjualan_1.setChecked)
        self.btnStok_2.toggled.connect(self.btnPemesanan_1.setChecked)
        self.btnTransaksi_2.toggled.connect(self.btnTransaksi_1.setChecked)
        self.btnKeluar_1.toggled.connect(MainWindow.close)
        self.btnKeluar_2.toggled.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedLaporan.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnMenu.setText("")
        self.iconSayur_2.setText("")
        self.lblToko.setText(QCoreApplication.translate("MainWindow", u"TOKO SAYUR", None))
        self.btnDashboard_2.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.btnProduk_2.setText(QCoreApplication.translate("MainWindow", u"Produk", None))
        self.btnStok_2.setText(QCoreApplication.translate("MainWindow", u"Stok", None))
        self.btnPemesanan_2.setText(QCoreApplication.translate("MainWindow", u"Pemesanan", None))
        self.btnPenjualan_2.setText(QCoreApplication.translate("MainWindow", u"Laporan penjualan", None))
        self.btnTransaksi_2.setText(QCoreApplication.translate("MainWindow", u"Riwayat Transaksi", None))
        self.btnKeluar_2.setText(QCoreApplication.translate("MainWindow", u"Keluar", None))
        self.btnDashboard_1.setText("")
        self.btnProduk_1.setText("")
        self.btnPemesanan_1.setText("")
        self.btnStok_1.setText("")
        self.btnPenjualan_1.setText("")
        self.btnTransaksi_1.setText("")
        self.btnKeluar_1.setText("")
        self.iconSayur_1.setText("")
        self.IconUtama.setText("")
        self.btnPencariandashboard.setText("")
        self.jdlTotalPemesanan.setText(QCoreApplication.translate("MainWindow", u"Total Pemesanan", None))
        self.label_4.setText("")
        self.lblTotalPesanan.setText(QCoreApplication.translate("MainWindow", u"152", None))
        self.jdlTotalTransaksi.setText(QCoreApplication.translate("MainWindow", u"Total Transaksi", None))
        self.label_2.setText("")
        self.lblTotalTransaksi.setText(QCoreApplication.translate("MainWindow", u"152", None))
        self.jdlTotalProduk.setText(QCoreApplication.translate("MainWindow", u"Total Produk", None))
        self.label_6.setText("")
        self.lblTotalProduk.setText(QCoreApplication.translate("MainWindow", u"152", None))
        self.jdlTotalStok.setText(QCoreApplication.translate("MainWindow", u"Total Stok", None))
        self.label_10.setText("")
        self.lblTotalStok.setText(QCoreApplication.translate("MainWindow", u"152", None))
        self.Judul_pesanan.setText(QCoreApplication.translate("MainWindow", u"DAFTAR PESANAN", None))
        self.subjudul_pesanan.setText(QCoreApplication.translate("MainWindow", u"Pesanan pelanggan yang masuk", None))
        self.btnPencarianPesanan.setText("")
        self.btnTambahPesanan.setText(QCoreApplication.translate("MainWindow", u"Tambah Pesanan", None))
        ___qtablewidgetitem = self.TablePesanan.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID Pesanan", None));
        ___qtablewidgetitem1 = self.TablePesanan.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Tanggal Pemesanan", None));
        ___qtablewidgetitem2 = self.TablePesanan.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Nama Pemesan", None));
        ___qtablewidgetitem3 = self.TablePesanan.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Total", None));
        ___qtablewidgetitem4 = self.TablePesanan.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Metode Pembayaran", None));
        ___qtablewidgetitem5 = self.TablePesanan.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem6 = self.TablePesanan.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Aksi", None));
        self.Judul_produk.setText(QCoreApplication.translate("MainWindow", u"STOK PRODUK", None))
        self.subjudul_produk.setText(QCoreApplication.translate("MainWindow", u"Monitoring dan Pengelolaan Produk", None))
        self.btnPencarianStok.setText("")
        self.btnTambahStok.setText(QCoreApplication.translate("MainWindow", u"Tambah Stok", None))
        self.comboBoxStok.setItemText(0, QCoreApplication.translate("MainWindow", u"-Status Stok-", None))
        self.comboBoxStok.setItemText(1, QCoreApplication.translate("MainWindow", u"Masih Ada", None))
        self.comboBoxStok.setItemText(2, QCoreApplication.translate("MainWindow", u"Menipis", None))
        self.comboBoxStok.setItemText(3, QCoreApplication.translate("MainWindow", u"Habis", None))

        ___qtablewidgetitem7 = self.TableStok.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Kode Produk", None));
        ___qtablewidgetitem8 = self.TableStok.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Nama Produk", None));
        ___qtablewidgetitem9 = self.TableStok.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Stok saat ini", None));
        ___qtablewidgetitem10 = self.TableStok.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Status Stok", None));
        ___qtablewidgetitem11 = self.TableStok.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Aksi", None));
        self.Judul_penjualan.setText(QCoreApplication.translate("MainWindow", u"LAPORAN PENJUALAN", None))
        self.subjudul_penjualan.setText(QCoreApplication.translate("MainWindow", u"Ringkasan transaksi dan performa penjualan", None))
        self.LblDari.setText(QCoreApplication.translate("MainWindow", u"Tanggal Dari", None))
        self.LblKe.setText(QCoreApplication.translate("MainWindow", u"Tanggal Ke", None))
        self.cmbMetodeLaporan.setItemText(0, QCoreApplication.translate("MainWindow", u"Semua", None))
        self.cmbMetodeLaporan.setItemText(1, QCoreApplication.translate("MainWindow", u"Cash", None))
        self.cmbMetodeLaporan.setItemText(2, QCoreApplication.translate("MainWindow", u"Transfer", None))

        self.btnTampilkanLaporan.setText(QCoreApplication.translate("MainWindow", u"Tampilkan", None))
        self.btnViewTable.setText(QCoreApplication.translate("MainWindow", u"Tabel", None))
        self.btnViewChart.setText(QCoreApplication.translate("MainWindow", u"Grafik", None))
        self.btnPencarianLaporan.setText("")
        ___qtablewidgetitem12 = self.tableLaporanPenjualan.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Tanggal", None));
        ___qtablewidgetitem13 = self.tableLaporanPenjualan.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Jumlah Transaksi", None));
        ___qtablewidgetitem14 = self.tableLaporanPenjualan.horizontalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Total Penjualan", None));
        ___qtablewidgetitem15 = self.tableLaporanPenjualan.horizontalHeaderItem(3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Cash", None));
        ___qtablewidgetitem16 = self.tableLaporanPenjualan.horizontalHeaderItem(4)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Transfer", None));
        self.Judul_Transaksi.setText(QCoreApplication.translate("MainWindow", u"RIWAYAT TRANSAKSI", None))
        self.subjudul_Transaksi.setText(QCoreApplication.translate("MainWindow", u"Daftar Transaksi Penjualan", None))
        self.btnFilterTransaksi.setText(QCoreApplication.translate("MainWindow", u"Tampilkan", None))
        self.btnResetFilterTransaksi.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.cmbMetodeTransaksi.setItemText(0, QCoreApplication.translate("MainWindow", u"Semua", None))
        self.cmbMetodeTransaksi.setItemText(1, QCoreApplication.translate("MainWindow", u"Cash", None))
        self.cmbMetodeTransaksi.setItemText(2, QCoreApplication.translate("MainWindow", u"Transfer", None))

        self.btnPencarianTransaksi.setText("")
        ___qtablewidgetitem17 = self.TableTransaksi.horizontalHeaderItem(0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"ID Transaksi", None));
        ___qtablewidgetitem18 = self.TableTransaksi.horizontalHeaderItem(1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"ID Pesanan", None));
        ___qtablewidgetitem19 = self.TableTransaksi.horizontalHeaderItem(2)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Tanggal Bayar", None));
        ___qtablewidgetitem20 = self.TableTransaksi.horizontalHeaderItem(3)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Total Bayar", None));
        ___qtablewidgetitem21 = self.TableTransaksi.horizontalHeaderItem(4)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Metode Pembayaran", None));
        ___qtablewidgetitem22 = self.TableTransaksi.horizontalHeaderItem(5)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Aksi", None));
        self.btnPDF.setText(QCoreApplication.translate("MainWindow", u"EXPOR PDF", None))
        self.Judul_Produk.setText(QCoreApplication.translate("MainWindow", u"PRODUK", None))
        self.subjudul_Produk.setText(QCoreApplication.translate("MainWindow", u"Kelola Data Produk Toko Sayur", None))
        self.btnPencarianProduk.setText("")
        self.btnTambahProduk.setText(QCoreApplication.translate("MainWindow", u"Tambah Produk", None))
        ___qtablewidgetitem23 = self.TableProduk.horizontalHeaderItem(0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"ID Produk", None));
        ___qtablewidgetitem24 = self.TableProduk.horizontalHeaderItem(1)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Kode Produk", None));
        ___qtablewidgetitem25 = self.TableProduk.horizontalHeaderItem(2)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Nama Produk", None));
        ___qtablewidgetitem26 = self.TableProduk.horizontalHeaderItem(3)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Harga Jual", None));
        ___qtablewidgetitem27 = self.TableProduk.horizontalHeaderItem(4)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Satuan", None));
        ___qtablewidgetitem28 = self.TableProduk.horizontalHeaderItem(5)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Aksi", None));
    # retranslateUi

