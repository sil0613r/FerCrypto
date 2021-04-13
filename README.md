# FerCrypto
Encrypt and decrypt files using the cryptography library

## Usage
### To encrypt files run encrypt.py, insert the path to file, select how often the key will be changed (0 - once, n > 0 where n is the input - seconds between generating new key)
### To decrypt files run decrypt.py, insert the encrypted file path and the key path

## More info about generating new keys
### If you choose the option that generates keys, encrypt_background.py will start and a batch file will be created in the startup folder. When you open your pc encrypt_ask_background.py will run and ask you if you want to run encrypt_background.py (y - encrypt_background.py will run, n - the batch file will be deleted)

## Notes
### -the changing keys option works only on windows
### -all the scripts must be in the same folder (you can change the scripts location but you need to modify the code from the scripts and from variables.json)
### -works 100% with .png .jpg .txt .docx .pdf .mp3 .mp4
