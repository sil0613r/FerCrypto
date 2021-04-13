from cryptography.fernet import Fernet

file = input('Enter the file location: ')
key_location = input('Enter the key location: ')


def decrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = f.decrypt(encrypted_data)

    with open(filename, "wb") as file:
        file.write(decrypted_data)


def load_key():
    return open(key_location, "rb").read()


key = load_key()

decrypt(file, key)
