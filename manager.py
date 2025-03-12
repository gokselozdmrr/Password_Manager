import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit, QLabel, \
    QFormLayout, QRadioButton
from encryption import encrypt, decrypt
from database import insert_password, get_password
from utils import generate_strong_password
import pyotp  # It provides 2FA support
import pyperclip # It provides copying transaction

def generate2FA():
    # It generates a 2FA secret key and produces valid code
    secret = pyotp.random_base32()  # Generate a random secret
    totp = pyotp.TOTP(secret)  # Generates TOTP object
    return secret, totp.now() # Returns the secret and the generated code


def save_password(service, username, password, encryption_key):
    # It saves the password to the database as encrypted form
    encrypted_password = encrypt(password, encryption_key)  # Encrypts the password
    insert_password(service, username, encrypted_password)  # Save encrypted password to the database


def show_password(service, encryption_key):
    # It shows the password that belongs to related service
    result = get_password(service)
    if result:
        username, encrypted_password = result
        decrypted_password = decrypt(encrypted_password, encryption_key)
        return decrypted_password
    else:
        return "Service not found!!!"


def initUI():
    # It initiates the UI with PyQt6
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setWindowTitle("Password Manager")
    window.setGeometry(100, 100, 400, 350)

    layout = QVBoxLayout()

    # User Input Fields
    service_input = QLineEdit()
    username_input = QLineEdit()
    password_input = QLineEdit()
    password_input.setEchoMode(QLineEdit.EchoMode.Password)  # Password was unvisible

    form_layout = QFormLayout()
    form_layout.addRow("Service: ", service_input)
    form_layout.addRow("Username: ", username_input)
    form_layout.addRow("Password: ", password_input)

    # Radio buttons for selecting password generation method
    radio_custom = QRadioButton("Custom Password")
    radio_custom.setChecked(True)  # Default option is "Custom Password"
    radio_random = QRadioButton("Generate Random Password")

    # Add radio buttons to the form
    form_layout.addRow(radio_custom)
    form_layout.addRow(radio_random)

    def on_save():
        # Determine which password to use based on radio button selection
        if radio_random.isChecked():
            password = generate_strong_password()
        else:
            password = password_input.text()

        save_password(service_input.text(), username_input.text(), password, b"thisisaverystrongkey32bytesecure")
        password_input.setText(password)

    def on_copy():
        pyperclip.copy(password_input.text())

    def on_generate_2fa():
        secret, code = generate2FA()
        twofa_secret_label.setText(f"Secret: {secret}")
        twofa_code_label.setText(f"Code: {code}")

    save_button = QPushButton("Save")
    save_button.clicked.connect(on_save)

    show_button = QPushButton("Show Password")
    show_button.clicked.connect(
        lambda: password_input.setText(show_password(service_input.text(), b"thisisaverystrongkey32bytesecure")))

    copy_button = QPushButton("Copy Password")
    copy_button.clicked.connect(on_copy)

    generate_2fa_button = QPushButton("Generate 2FA Code")
    generate_2fa_button.clicked.connect(on_generate_2fa)

    twofa_secret_label = QLabel()
    twofa_code_label = QLabel()

    layout.addLayout(form_layout)
    layout.addWidget(save_button)
    layout.addWidget(show_button)
    layout.addWidget(copy_button)
    layout.addWidget(generate_2fa_button)
    layout.addWidget(twofa_secret_label)
    layout.addWidget(twofa_code_label)

    container = QWidget()
    container.setLayout(layout)
    window.setCentralWidget(container)

    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    initUI()