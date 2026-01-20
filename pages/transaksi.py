from PySide6.QtWidgets import (
    QPushButton, QTableWidgetItem, QWidget, QHBoxLayout, QMessageBox
)
from PySide6.QtWidgets import QAbstractItemView
from database import db
from utils.pdf_export import export_transaksi_pdf
from PySide6.QtCore import QDate
from pages.dialog_detail_transaksi import DetailTransaksiDialog
from utils.receipt_print import print_receipt

class TransaksiPage:
    def __init__(self, ui):
        self.ui = ui
        self.table = ui.TableTransaksi

        self.setup_table()
        self.load_data()

        self.ui.btnFilterTransaksi.clicked.connect(self.apply_filter)
        self.ui.btnResetFilterTransaksi.clicked.connect(self.reset_filter)
        self.ui.inputSearchTransaksi.textChanged.connect(
            lambda text: self.search_by_name(text, 1)
        )
        self.ui.inputSearchTransaksi.setPlaceholderText("Cari nama...")


        self.ui.cmbMetodeTransaksi.addItems(["Semua", "Cash", "Transfer"])


    def setup_table(self):
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels([
            "ID Transaksi", "ID Pesanan", "Total", "Metode", "Tanggal", "Aksi"
        ])
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)

    def load_data(self):
        self.table.setRowCount(0)

        query = "SELECT * FROM transaksi ORDER BY tanggal DESC"
        for row in db.cursor.execute(query):
            row_pos = self.table.rowCount()
            self.table.insertRow(row_pos)

            for col, val in enumerate(row):
                self.table.setItem(row_pos, col, QTableWidgetItem(str(val)))

            self.add_action_buttons(row_pos, row)

    def add_action_buttons(self, row, data):
        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)

        btn_print = QPushButton("Print")
        btn_pdf = QPushButton("PDF")

        btn_detail = QPushButton("Detail")
        btn_detail.clicked.connect(
            lambda _, d=data: self.show_detail(d)
        )
        layout.insertWidget(0, btn_detail)

        btn_print.clicked.connect(lambda _, d=data: self.print_struk(d))
        btn_pdf.clicked.connect(lambda _, d=data: self.export_pdf(d))

        layout.addWidget(btn_print)
        layout.addWidget(btn_pdf)

        self.table.setCellWidget(row, 5, widget)

    def show_detail(self, data):
        dialog = DetailTransaksiDialog(data, self.ui.centralwidget)
        dialog.exec()


    def print_struk(self, data):
        print_receipt(data)
        QMessageBox.information(
            None, "Print", "Struk berhasil dikirim ke printer"
        )

    def export_pdf(self, data):
        export_transaksi_pdf(data)
        QMessageBox.information(
            None, "PDF", "Transaksi berhasil diexport ke PDF"
        )

    def apply_filter(self):
        date_from = self.ui.dateFromTransaksi.date().toString("yyyy-MM-dd")
        date_to = self.ui.dateToTransaksi.date().toString("yyyy-MM-dd")
        metode = self.ui.cmbMetodeTransaksi.currentText()

        query = """
            SELECT * FROM transaksi
            WHERE tanggal BETWEEN ? AND ?
            """
        params = [date_from, date_to]

        if metode != "Semua":
            query += " AND metode=?"
            params.append(metode)

        self.load_data(query, params)

    def reset_filter(self):
        self.ui.dateFromTransaksi.setDate(QDate.currentDate())
        self.ui.dateToTransaksi.setDate(QDate.currentDate())
        self.ui.cmbMetodeTransaksi.setCurrentIndex(0)
        self.load_data()

    def load_data(self, query=None, params=None):
        self.table.setRowCount(0)

        if not query:
            query = "SELECT * FROM transaksi ORDER BY tanggal DESC"
            params = []

        for row in db.cursor.execute(query, params):
            row_pos = self.table.rowCount()
            self.table.insertRow(row_pos)

            for col, val in enumerate(row):
                self.table.setItem(row_pos, col, QTableWidgetItem(str(val)))

            self.add_action_buttons(row_pos, row)

    def search_by_name(self, text, col):
        text = text.lower()
        for row in range(self.table.rowCount()):
            item = self.table.item(row, col)
            self.table.setRowHidden(
                row,
                text not in item.text().lower()
            )
        
        self.ui.main.dashboard.refresh()





