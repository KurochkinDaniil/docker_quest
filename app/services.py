import os.path

from cryptography.fernet import Fernet


def generate_key(filename: str = 'crypto.key'):
    key = Fernet.generate_key()
    with open(filename, 'wb') as key_file:
        key_file.write(key)


def load_key(filename: str = 'crypto.key'):
    return open(filename, 'rb').read()


def encrypt(filename, key):
    f = Fernet(key)
    with open(filename, 'rb+') as file:
        data = file.read()
    encrypted_data = f.encrypt(data)
    with open(filename, 'wb') as file:
        file.write(encrypted_data)


def decrypt(filename, key):
    f = Fernet(key)
    with open(filename, 'rb+') as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filename, 'wb') as file:
        file.write(decrypted_data)
    return decrypted_data


def validate_answer(answer: str):
    if answer.upper() in ['WATSON', 'УОТСОН', 'ВАТСОН', 'WATTSON']:
        return True
    return False


if __name__ == '__main__':
    generate_key()
    encrypt('app/files/answer.txt', load_key())
