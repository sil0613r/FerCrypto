import time
from cryptography.fernet import Fernet
import json


json_file = open("variables.json")
variables = json.load(json_file)


original_file_location = variables['original_file_location']
encrypted_file_location = variables['encrypted_file_location']
key_location = variables['key_location']
encrypt_interval = variables['encrypt_interval']
encrypt_interval = float(encrypt_interval)

time.sleep(1)


while True:

    def load_key():
        return open(key_location, "rb").read()

    key = load_key()

    def encrypt(filename_original, filename):
        f = Fernet(key)
        with open(filename_original, "rb") as file:
            file_data = file.read()

        encrypted_data = f.encrypt(file_data)

        with open(filename, "wb") as file:
            file.write(encrypted_data)

    encrypt(original_file_location, encrypted_file_location)

    print('Key changed')

    time.sleep(encrypt_interval)
