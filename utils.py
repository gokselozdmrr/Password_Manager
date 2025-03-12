import random
import string


def generate_strong_password(length=16):
    """It generates a strong password"""
    all_characters = string.ascii_letters + string.digits + string.punctuation  # It uses letter,number and punctuation

    return ''.join(random.choice(all_characters) for _ in range(length))  # Generates a random and strong password, then this password returns


def validate_password(password):
    """It checks the security of the password"""
    if len(password) < 8:
        return False

    if not any(char.isdigit() for char in password):  # It validates number
        return False

    if not any(char.isalpha() for char in password):  # It validates alphabet
        return False

    return True