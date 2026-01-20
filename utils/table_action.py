from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton
from PySide6.QtCore import Qt


class TableActionBuilder:
    def __init__(self, table, row, column):
        """
        table   : QTableWidget
        row     : row index
        column  : column index (kolom Aksi)
        """
        self.table = table
        self.row = row
        self.column = column

        self.widget = QWidget()
        self.layout = QHBoxLayout(self.widget)
        self.layout.setContentsMargins(2, 2, 2, 2)
        self.layout.setSpacing(4)
        self.layout.setAlignment(Qt.AlignCenter)

    def add_button(self, text, callback, tooltip=None, style=None):
        btn = QPushButton(text)
        btn.setCursor(Qt.PointingHandCursor)

        if tooltip:
            btn.setToolTip(tooltip)

        if style:
            btn.setStyleSheet(style)

        btn.clicked.connect(callback)
        self.layout.addWidget(btn)
        return self

    def build(self):
        self.table.setCellWidget(self.row, self.column, self.widget)
