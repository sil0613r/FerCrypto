import os
import getpass

user_name = getpass.getuser()
start_background = input('Continue encrypting the file? (y/n) ')
bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % user_name
dir_path = os.path.dirname(os.path.realpath(__file__))

encrypt_background_path = str()

if start_background == 'y':
    os.chdir(dir_path)
    file_name = 'encrypt_background.py'
    os.system('cmd /k "python3 %s"' % file_name)
elif start_background == 'n':
    os.remove(bat_path + '\\' + "run_ask_encrypt_background.bat")
else:
    print('invalid option')
