from PySide6.QtWidgets import QTableWidgetItem
from PySide6.QtCharts import (
    QChart, QChartView, QBarSeries, QBarSet, QValueAxis, QBarCategoryAxis
)
from PySide6.QtWidgets import QAbstractItemView
from PySide6.QtCore import Qt
from database import db
from datetime import datetime

class LaporanPage:
    def __init__(self, ui):
        self.ui = ui
        self.table = ui.tableLaporanPenjualan
        self.chart_view = ui.chartViewPenjualan

        self.setup_table()
        self.setup_ui()
        self.load_laporan()

    # ================= SETUP =================

    def setup_ui(self):
        self.ui.cmbMetodeLaporan.addItems(["Semua", "Cash", "Transfer"])

        self.ui.btnTampilkanLaporan.clicked.connect(self.load_laporan)
        self.ui.btnViewTable.clicked.connect(
            lambda: self.ui.stackedLaporan.setCurrentIndex(0)
        )
        self.ui.btnViewChart.clicked.connect(
            lambda: self.ui.stackedLaporan.setCurrentIndex(1)
        )

    def setup_table(self):
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels([
            "Tanggal", "Jumlah Transaksi",
            "Total Penjualan", "Cash", "Transfer"
        ])
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)

    # ================= DATA =================

    def load_laporan(self):
        date_from = self.ui.dateFromLaporan.date().toString("yyyy-MM-dd")
        date_to = self.ui.dateToLaporan.date().toString("yyyy-MM-dd")
        metode = self.ui.cmbMetodeLaporan.currentText()

        query = """
        SELECT
            tanggal,
            COUNT(*) as jumlah,
            SUM(total) as total,
            SUM(CASE WHEN metode='Cash' THEN total ELSE 0 END) as cash,
            SUM(CASE WHEN metode='Transfer' THEN total ELSE 0 END) as transfer
        FROM transaksi
        WHERE tanggal BETWEEN ? AND ?
        """
        params = [date_from, date_to]

        if metode != "Semua":
            query += " AND metode=?"
            params.append(metode)

        query += " GROUP BY tanggal ORDER BY tanggal"

        result = db.cursor.execute(query, params).fetchall()

        self.fill_table(result)
        self.fill_chart(result)

    # ================= TABLE =================

    def fill_table(self, data):
        self.table.setRowCount(0)

        for row_idx, row in enumerate(data):
            self.table.insertRow(row_idx)
            for col, val in enumerate(row):
                self.table.setItem(
                    row_idx, col,
                    QTableWidgetItem(str(val))
                )

    # ================= CHART =================

    def fill_chart(self, data):
        chart = QChart()
        chart.setTitle("Grafik Penjualan")

        series = QBarSeries()
        set_total = QBarSet("Total Penjualan")

        categories = []

        for row in data:
            categories.append(row[0])
            set_total.append(row[2] or 0)

        series.append(set_total)
        chart.addSeries(series)

        axis_x = QBarCategoryAxis()
        axis_x.append(categories)
        chart.addAxis(axis_x, Qt.AlignBottom)
        series.attachAxis(axis_x)

        axis_y = QValueAxis()
        chart.addAxis(axis_y, Qt.AlignLeft)
        series.attachAxis(axis_y)

        self.chart_view.setChart(chart)
