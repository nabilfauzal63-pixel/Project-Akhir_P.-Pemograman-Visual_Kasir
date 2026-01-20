# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_detail_pesanan.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QFrame,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(751, 591)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lblJudul = QLabel(self.frame)
        self.lblJudul.setObjectName(u"lblJudul")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.lblJudul.setFont(font)

        self.verticalLayout_2.addWidget(self.lblJudul)

        self.tableDetailPesanan = QTableWidget(self.frame)
        if (self.tableDetailPesanan.columnCount() < 4):
            self.tableDetailPesanan.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableDetailPesanan.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableDetailPesanan.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableDetailPesanan.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableDetailPesanan.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableDetailPesanan.setObjectName(u"tableDetailPesanan")
        self.tableDetailPesanan.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableDetailPesanan.setAlternatingRowColors(True)
        self.tableDetailPesanan.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableDetailPesanan.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableDetailPesanan.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_2.addWidget(self.tableDetailPesanan)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_2.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lblJudul.setText(QCoreApplication.translate("Dialog", u"Detail Pesanan", None))
        ___qtablewidgetitem = self.tableDetailPesanan.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Produk", None));
        ___qtablewidgetitem1 = self.tableDetailPesanan.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Harga", None));
        ___qtablewidgetitem2 = self.tableDetailPesanan.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"Qty", None));
        ___qtablewidgetitem3 = self.tableDetailPesanan.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"Subtotal", None));
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"TUTUP", None))
    # retranslateUi

