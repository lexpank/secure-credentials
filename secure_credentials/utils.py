from cryptography.fernet import Fernet

def generate_encryption_key() -> str:
    """ Generate random key for encryption """
    key = Fernet.generate_key()
    return key.decode("utf-8")


def encrypt_data(key: str, data: str) -> str:
    """ Encrypt data using key """
    f = Fernet(key)
    return f.encrypt(data.encode("utf-8")).decode("utf-8")

def decrypt_data(key: str, data: str) -> str:
    """ Decrypt data using key """
    f = Fernet(key)
    return f.decrypt(data.encode("utf-8")).decode("utf-8")