from PySide6.QtWidgets import (
    QDialog, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QMessageBox
)
from PySide6.QtCore import Qt
from database import db


class LoginDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Login Kasir")
        self.setFixedSize(350, 220)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)

        # ======================
        # WIDGET
        # ======================
        title = QLabel("🧾 Aplikasi Kasir")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            font-size:18px;
            font-weight:bold;
        """)

        self.inputUser = QLineEdit()
        self.inputUser.setPlaceholderText("Username")

        self.inputPass = QLineEdit()
        self.inputPass.setPlaceholderText("Password")
        self.inputPass.setEchoMode(QLineEdit.Password)

        btnLogin = QPushButton("LOGIN")
        btnLogin.setCursor(Qt.PointingHandCursor)
        btnLogin.setStyleSheet("""
            QPushButton {
                background:#2ecc71;
                color:white;
                font-weight:bold;
                padding:8px;
                border-radius:6px;
            }
            QPushButton:hover {
                background:#27ae60;
            }
        """)

        # ======================
        # LAYOUT
        # ======================
        layout = QVBoxLayout(self)
        layout.addWidget(title)
        layout.addSpacing(10)
        layout.addWidget(self.inputUser)
        layout.addWidget(self.inputPass)
        layout.addSpacing(10)
        layout.addWidget(btnLogin)

        # ======================
        # SIGNAL
        # ======================
        btnLogin.clicked.connect(self.login)

    # ======================
    # LOGIC LOGIN
    # ======================
    def login(self):
        username = self.inputUser.text().strip()
        password = self.inputPass.text().strip()

        if not username or not password:
            QMessageBox.warning(self, "Error", "Username dan password wajib diisi")
            return

        db.cursor.execute("""
            SELECT id FROM user
            WHERE username=? AND password=?
        """, (username, password))

        if db.cursor.fetchone():
            self.accept()
        else:
            QMessageBox.critical(
                self,
                "Login Gagal",
                "Username atau password salah"
            )
