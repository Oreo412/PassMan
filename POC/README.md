# PassMan – Python Proof of Concept

This directory contains a fully functional command-line proof of concept for
the PassMan password manager. It demonstrates the core cryptographic workflow
used by the main project.

## What This Demonstrates
- Password-based key derivation using **Argon2**
- AES-256 encryption and decryption of credential data
- Secure local file storage
- JSON-based portable data format

This implementation serves as the reference model for the browser extension.

## Requirements
- Python 3.9+
- pycryptodome
- argon2-cffi

Install dependencies:
```bash
pip install pycryptodome argon2-cffi
```
Running the PoC
From the POC directory:
```bash
python proof2.py
```
The CLI is interactive and will prompt you to:

  Create or open an encrypted password file
  
  Add, find, and manage credentials
  
  Save encrypted data to disk

Included is an example password file. To access this password answer y when asked if you'd like to open a file, input the file name "example", then input the password "examplemasterpassword"

After opening the example file, you can see example entries and add your own entries into the example file. Don't forget to save before exiting the CLI!
  
Notes
All cryptographic operations are performed locally

The encrypted files created here are compatible with the JavaScript browser
extension prototype

This tool is intended for educational and experimental purposes
