from cryptography.fernet import Fernet
import shutil
import json
import os
import getpass
import pathlib

user_name = getpass.getuser()

file = input("Enter the file location: ")
encrypt_interval = input("How often should the file be encrypted (0 for one time; minutes): ")
encrypt_interval = int(encrypt_interval)
file_ext = pathlib.Path(file).suffix
file_ext = str(file_ext)
encrypt_location = os.path.dirname(os.path.realpath(__file__))

shutil.copy2(file, 'original_file%s' % file_ext)

json_variables = {
    'encrypt_interval': encrypt_interval,
    'encrypted_file_location': file,
    'original_file_location': 'original_file%s' % file_ext,
    'key_location': 'key.key',
    'encrypt_ask_location': '%s\\encrypt_ask_background.py' % encrypt_location
}

with open('variables.json', 'w') as json_file:
    json.dump(json_variables, json_file)


def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    return open("key.key", "rb").read()


def encrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()

    encrypted_data = f.encrypt(file_data)

    with open(filename, "wb") as file:
        file.write(encrypted_data)


def encrypt_and_create_key():
    write_key()
    key = load_key()
    encrypt(file, key)


json_file_variables = open("variables.json")
variables = json.load(json_file_variables)

encrypt_ask_location = variables['encrypt_ask_location']

def add_to_startup():
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % user_name
    with open(bat_path + '\\' + "run_ask_encrypt_background.bat", "w+") as bat_file:
        bat_file.write(r'python3 %s' % encrypt_ask_location)


def check_encrypt_interval():
    if encrypt_interval == 0:
        encrypt_and_create_key()
    elif encrypt_interval > 0:
        encrypt_and_create_key()
        add_to_startup()
        os.system('python3 encrypt_background.py')
    else:
        print('error')


check_encrypt_interval()
