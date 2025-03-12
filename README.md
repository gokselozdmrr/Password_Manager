# Password Manager with 2FA Support
This is a Password Manager application built with PyQt6 for the graphical user interface (GUI), providing the ability to securely store and retrieve passwords. The project also supports 2FA (Two-Factor Authentication) integration and generates strong passwords. The data is encrypted using AES-256 encryption for security.

## Features
Password Encryption: User passwords are securely encrypted using AES-256 encryption.
Password Storage: Allows saving, retrieving, and displaying passwords for different services.
2FA Generation: Supports Two-Factor Authentication (2FA) by generating time-based one-time passcodes (TOTP).
Password Generation: Provides the option to generate strong random passwords.
Copy to Clipboard: Allows copying passwords to the clipboard for easy pasting.
Dependencies
This project requires the following Python libraries:

**PyQt6**: For building the graphical user interface.
**pyotp**: For generating and validating time-based one-time passcodes (TOTP) for Two-Factor Authentication.
**pyperclip**: For copying passwords to the clipboard.
**Cryptography (PyCryptodome)**: For AES-256 encryption.
**sqlite3**: For the local database storage of passwords.
**random and string**: For generating strong random passwords.

To install the required dependencies, you can use **pip**:
"pip install pyqt6 pyotp pyperclip pycryptodome"

## Project Structure

password_manager/
│
├── manager.py                 # Main application file
├── encryption.py           # Encryption and decryption functions (AES-256)
├── database.py             # Database interaction (SQLite)
├── utils.py                # Utility functions (password generation and validation)
└── identifier.sqlite       # SQLite database for storing passwords

## How It Works

1. **Encrypting and Storing Passwords**
When saving a password, the application encrypts the password using AES-256 encryption before storing it in an SQLite database. The encryption key used for AES is a fixed 32-byte key (you can modify this for better security).

2. **Password Retrieval**
To retrieve a password, the application decrypts the stored password using the encryption key and displays it in the password field.

3. **Two-Factor Authentication (2FA)**
The 2FA functionality allows users to generate a TOTP (Time-Based One-Time Password) for additional security. This 2FA code is displayed along with the secret key, which can be used to generate valid 2FA codes in the future.

4. **Password Generation**
The application allows the user to either:
  -Manually input a password, or
  -Automatically generate a strong random password using a combination of letters, digits, and symbols.

5. **Clipboard Copying**
Users can easily copy the password to the clipboard for use in login forms or other applications.

## Usage

You can use any IDE or code editor to run the application. You need to run manager.py to run the application.

The application will open a window with the following features:

**Service**: The name of the service (e.g., Gmail, Facebook).
**Username**: The username associated with the service.
**Password**: The password for the service (either custom or generated).

## How to Use

**Saving a Password**:

Enter the service name, username, and password.
You can either enter a custom password or generate a random one.
Click "Save" to store the password in the database.

**Viewing a Password**:
Enter the service name and click "Show Password" to view the decrypted password.

**Copying a Password**:

After entering the password field, click "Copy Password" to copy the password to your clipboard.

**Generate 2FA Code**:

Click "Generate 2FA Code" to generate a new secret and the corresponding one-time passcode (TOTP).

## Security Considerations

**AES-256 Encryption**: The application uses AES-256 encryption to store passwords securely. The encryption key is hardcoded, but in production, you should use a more secure method for handling keys (e.g., environment variables, hardware security modules).

**Two-Factor Authentication (2FA)**: 2FA adds an additional layer of security to your services by requiring a time-sensitive code, in addition to the password.

## Database

Passwords are stored in an SQLite database named **identifier.sqlite**. This database contains the following table:

**Passwords Table**:
    **service**: The name of the service (e.g., Gmail, Facebook).
    **username**: The username associated with the service.
    **password**: The encrypted password for the service.

You can view or modify the stored data directly in the SQLite database file if needed.

# Password_Manager
