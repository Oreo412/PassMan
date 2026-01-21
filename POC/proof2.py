import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Util.Padding import pad
from argon2 import PasswordHasher
import os
import base64

data = {}


def encryptFile(password, fileName, plaintext):
    ph = PasswordHasher(hash_len=32)
    hash = ph.hash(password)
    salt, key = argonToBinary(hash)
    cipher = AES.new(key,AES.MODE_GCM)
    encryptedText, tag = cipher.encrypt_and_digest(plaintext.encode("utf-8"))
    with open(fileName, 'wb')as c_file:
        c_file.write(salt)
        c_file.write(cipher.nonce)
        c_file.write(encryptedText)
        c_file.write(tag)

def decryptFile(password, fileName):
    ph = PasswordHasher(hash_len=32)
    with open(fileName, 'rb') as c_file:
        saltIn = c_file.read(16)
        nonce = c_file.read(16)
        cipher = c_file.read()
        ciphertext = cipher[:len(cipher)-16]
        tag = cipher[len(cipher)-16:]

    hash = ph.hash(password, salt= saltIn )
    _, key = argonToBinary(hash)

    cipher = AES.new(key, AES.MODE_GCM, nonce)



    plaintext = cipher.decrypt_and_verify(ciphertext, tag).decode()

    return plaintext

def addSite():
    global data
    website = input("Input Website URL: ")
    username = input("Input Username: ")
    password = input("Input Password: ")
    data[website] = {
        "username": username,
        "password": password
    }

def loadJson():
    global data
    fileName = input("Input file name: ")
    key = input("Input password to unlock: ")
    jsonText = decryptFile(key, fileName)
    data = json.loads(jsonText)

def findPassword():
    global data
    inputSite = ""
    while True:
        print("Select one of the following sites: ")
        sites = data.keys()
        for site in sites:
            print(site)
        inputSite = input()
        if inputSite in sites:
            break
        print("Please check your spelling")
    return data[inputSite]["username"], data[inputSite]["password"]

def argonToBinary(output):
    splitHash = output.split('$')
    salt = splitHash[4]
    hash = splitHash[5]
    padded_salt = salt + '=' * (len(salt) % 4)
    padded_hash = hash + '=' * (len(hash) % 4)

    binary_salt = base64.b64decode(padded_salt)
    binary_hash = base64.b64decode(padded_hash)
    return binary_salt, binary_hash

openFile = 'w'

while True:
    openFile = input("Would you like to open existing passwords? y/n: ")[0].lower()
    if openFile in ['y', 'n']:
        break
    print("Please type y or n")

if(openFile == 'y'):
    loadJson()

nextTask = 'w'

while True:
    openFile = input("Would you like to: \n Find Password (f) \n Add Password (a) \n Save file (s) \n Load New Password File (l) \n Exit (e) \n")[0].lower()
    if openFile == 'e':
        break
    elif openFile == 'f':
        username, password = findPassword()
        print("Username: " + username)
        print("Password: " + password)
    elif openFile == 'a':
        addSite()
    elif openFile == 's':
        
        password = input("Input Password: ")
            
        fileName = input("Please input file name: ")
        encryptFile(password, fileName, json.dumps(data, indent=4))
    elif openFile == 'l':
        loadJson()
    else:
        print("Please input one of the given characters")

