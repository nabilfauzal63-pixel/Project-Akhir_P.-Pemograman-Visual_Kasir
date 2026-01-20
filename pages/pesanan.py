from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from PySide6.QtPrintSupport import QPrinter, QPrintDialog
from PySide6.QtGui import QTextDocument
from database import db
from pages.dialog_tambah_pesanan import DialogTambahPesanan
from pages.dialog_detail_pesanan import DetailPesananDialog
from pages.dialog_edit_pesanan import DialogEditPesanan
from utils.table_action import TableActionBuilder
from pages.dialog_preview_struk import PreviewStrukDialog

class PesananPage:
    def __init__(self, ui):
        self.ui = ui
        self.table = ui.TablePesanan

        self.ui.btnTambahPesanan.clicked.connect(self.tambah_pesanan)
        self.load_data()

    # ======================
    # LOAD DATA
    # ======================
    def load_data(self):
        self.table.setRowCount(0)

        db.cursor.execute("""
            SELECT id, tanggal, nama_pelanggan, total, metode, status
            FROM pesanan
            ORDER BY id DESC
        """)

        for data in db.cursor.fetchall():
            row = self.table.rowCount()
            self.table.insertRow(row)

            for col, val in enumerate(data):
                self.table.setItem(row, col, QTableWidgetItem(str(val)))

            self.add_action_buttons(row, data)

    # ======================
    # TAMBAH PESANAN
    # ======================
    def tambah_pesanan(self):
        dialog = DialogTambahPesanan()

        if dialog.exec():
            data = dialog.get_data()

            db.cursor.execute("""
                INSERT INTO pesanan (nama_pelanggan, tanggal, total, status)
                VALUES (?, ?, ?, 'draft')
            """, (
                data["nama"],
                data["tanggal"],
                data["total"]
            ))

            pesanan_id = db.cursor.lastrowid

            for item in data["items"]:
                db.cursor.execute("""
                    INSERT INTO pesanan_detail
                    (pesanan_id, nama_produk, harga, qty, subtotal)
                    VALUES (?, ?, ?, ?, ?)
                """, (
                    pesanan_id,
                    item["nama"],
                    item["harga"],
                    item["qty"],
                    item["subtotal"]
                ))

            db.conn.commit()
            self.load_data()

    # ======================
    # DETAIL PESANAN
    # ======================
    def buka_detail_pesanan(self, pesanan_id):
        dialog = DetailPesananDialog(pesanan_id, self.ui.centralwidget)
        dialog.exec()

    # ======================
    # BAYAR + KURANGI STOK
    # ======================
    def bayar(self, pesanan_id, metode):
        # Ambil detail pesanan
        db.cursor.execute("""
            SELECT nama_produk, qty
            FROM pesanan_detail
            WHERE pesanan_id=?
        """, (pesanan_id,))
        items = db.cursor.fetchall()

        # Kurangi stok
        for nama_produk, qty in items:
            db.cursor.execute("""
                UPDATE produk
                SET stok = stok - ?
                WHERE nama=?
            """, (qty, nama_produk))

        # Update pesanan
        db.cursor.execute("""
            UPDATE pesanan
            SET status='selesai', metode=?
            WHERE id=?
        """, (metode, pesanan_id))

        # Simpan transaksi
        db.cursor.execute("""
            INSERT INTO transaksi (pesanan_id, total, metode, tanggal)
            SELECT id, total, ?, date('now')
            FROM pesanan WHERE id=?
        """, (metode, pesanan_id))

        db.conn.commit()

        self.load_data()
        self.ui.main.stok.load_data()
        self.ui.main.riwayat.load_data()
        self.ui.main.laporan.load_data()

    # ======================
    # EDIT PESANAN
    # ======================
    def edit_pesanan(self, pesanan_id):
        dialog = DialogEditPesanan(pesanan_id)
        if dialog.exec():
            self.load_data()

    # ======================
    # HAPUS PESANAN
    # ======================
    def hapus_pesanan(self, pesanan_id):
        db.cursor.execute(
            "SELECT status FROM pesanan WHERE id=?", (pesanan_id,)
        )
        status = db.cursor.fetchone()[0]

        if status == "selesai":
            QMessageBox.warning(
                None, "Tidak Bisa",
                "Pesanan sudah selesai dan tidak bisa dihapus"
            )
            return

        if QMessageBox.question(
            None, "Hapus",
            "Yakin ingin menghapus pesanan ini?"
        ) == QMessageBox.Yes:

            db.cursor.execute(
                "DELETE FROM pesanan_detail WHERE pesanan_id=?",
                (pesanan_id,)
            )
            db.cursor.execute(
                "DELETE FROM pesanan WHERE id=?",
                (pesanan_id,)
            )

            db.conn.commit()
            self.load_data()

    # ======================
    # CETAK STRUK (FIX ERROR QPRINTER)
    # ======================
    def cetak_struk(self, pesanan_id):
        db.cursor.execute("""
            SELECT nama_pelanggan, tanggal, total, metode
            FROM pesanan WHERE id=?
        """, (pesanan_id,))
        pesanan = db.cursor.fetchone()

        if not pesanan:
            QMessageBox.warning(None, "Error", "Pesanan tidak ditemukan")
            return

        db.cursor.execute("""
            SELECT nama_produk, harga, qty, subtotal
            FROM pesanan_detail WHERE pesanan_id=?
        """, (pesanan_id,))
        items = db.cursor.fetchall()

        html = """
        <h3 style='text-align:center'>TOKO KASIR</h3>
        <hr>
        """
        html += f"Tanggal : {pesanan[1]}<br>"
        html += f"Pelanggan : {pesanan[0]}<br><br>"

        html += "<table width='100%'>"
        for nama, harga, qty, subtotal in items:
            html += f"""
            <tr>
                <td>{nama}</td>
                <td align='right'>{qty} x {harga}</td>
                <td align='right'>{subtotal}</td>
            </tr>
            """
        html += "</table><hr>"
        html += f"<b>TOTAL : Rp {pesanan[2]:,}</b><br>"
        html += f"Metode : {pesanan[3]}<br>"
        html += "<p style='text-align:center'>Terima Kasih</p>"

        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self.ui.centralwidget)

        if dialog.exec():
            doc = QTextDocument()
            doc.setHtml(html)
            doc.print(printer)

    def preview_struk(self, pesanan_id):
        dialog = PreviewStrukDialog(pesanan_id, self.ui.centralwidget)
        dialog.exec()

    # ======================
    # TOMBOL AKSI
    # ======================
    def add_action_buttons(self, row, data):
        pesanan_id = data[0]
        status = data[5]

        builder = TableActionBuilder(self.table, row, 6)

        builder.add_button(
            "Detail",
            lambda _, pid=pesanan_id: self.buka_detail_pesanan(pid)
        )

        if status == "draft":
            builder.add_button(
                "Edit",
                lambda _, pid=pesanan_id: self.edit_pesanan(pid)
            )
            builder.add_button(
                "Hapus",
                lambda _, pid=pesanan_id: self.hapus_pesanan(pid)
            )
            builder.add_button(
                "Cash",
                lambda _, pid=pesanan_id: self.bayar(pid, "Cash")
            )
            builder.add_button(
                "Transfer",
                lambda _, pid=pesanan_id: self.bayar(pid, "Transfer")
            )

        if status == "selesai":
            builder.add_button(
                "Cetak",
                lambda _, pid=pesanan_id: PreviewStrukDialog(
                    pid,
                    self.ui.centralwidget
            ).exec()
        )

        builder.build()
