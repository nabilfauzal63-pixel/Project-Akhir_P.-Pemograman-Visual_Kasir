from PySide6.QtPrintSupport import QPrinter
from PySide6.QtGui import QPainter, QFont

def print_receipt(data):
    printer = QPrinter()
    printer.setPrinterName("POS-Printer")  # ganti sesuai printer

    painter = QPainter(printer)
    painter.setFont(QFont("Courier", 10))

    y = 100
    lines = [
        "STRUK TRANSAKSI",
        f"ID Transaksi : {data[0]}",
        f"ID Pesanan   : {data[1]}",
        f"Total        : Rp {data[2]}",
        f"Metode       : {data[3]}",
        f"Tanggal      : {data[4]}",
        "",
        "Terima kasih"
    ]

    for line in lines:
        painter.drawText(100, y, line)
        y += 20

    painter.end()
