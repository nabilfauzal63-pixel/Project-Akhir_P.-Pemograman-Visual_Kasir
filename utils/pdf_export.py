from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime

def export_transaksi_pdf(data):
    file_name = f"transaksi_{data[0]}.pdf"
    c = canvas.Canvas(file_name, pagesize=A4)

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, 800, "STRUK TRANSAKSI")

    c.setFont("Helvetica", 11)
    y = 760
    labels = [
        ("ID Transaksi", data[0]),
        ("ID Pesanan", data[1]),
        ("Total", f"Rp {data[2]}"),
        ("Metode", data[3]),
        ("Tanggal", data[4]),
    ]

    for label, value in labels:
        c.drawString(50, y, f"{label}: {value}")
        y -= 20

    c.drawString(50, y - 20, "Terima kasih 🙏")
    c.save()
