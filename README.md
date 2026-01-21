# PassMan

A password manager project focused on secure local storage, encryption, and
cross-platform portability.

## Overview
PassMan is a password manager originally designed as a browser extension.
Credentials are stored locally in an encrypted file using **AES-256**, with
encryption keys derived from a master password via a **Key Derivation Function (Argon2)**.
The data format is JSON-based and intentionally standardized to allow
interoperability across different environments.

This project was developed to explore practical cryptography, secure storage,
and the differences between cryptographic APIs in Python and browser-based
JavaScript environments.

---

## Current Status
🚧 **Browser extension:** partially implemented  
✅ **Fully functional Python proof of concept**  
🧪 **JavaScript extension can decrypt files created by the Python PoC**

The core cryptographic workflow (key derivation, encryption, decryption, and file
parsing) is fully implemented and demonstrated in the Python PoC.  
The browser extension prototype focuses on validating cross-language
compatibility by successfully decrypting and reading encrypted password files
created by the Python implementation.

---

## Proof of Concept (Python CLI)
The `/POC` directory contains a working command-line password manager that:
- Derives encryption keys from a master password using **Argon2**
- Encrypts and decrypts credential data using **AES-256**
- Stores credentials securely in a local encrypted file
- Uses JSON as a standardized, portable storage format

This implementation serves as the reference model for the browser extension’s
encryption and storage logic.

---

## Browser Extension Prototype (JavaScript)
The browser extension is implemented using JavaScript and HTML and leverages the
**Web Crypto API (`window.crypto.subtle`)**, which requires asynchronous
cryptographic operations.

Current functionality includes:
- Argon2-based key derivation in JavaScript
- Decryption and parsing of encrypted password files created by the Python PoC
- Early UI and workflow experimentation

Implementing the same cryptographic design in JavaScript highlighted the
differences between synchronous crypto APIs (Python) and async-only browser
cryptography, as well as the constraints imposed by sandboxed environments.

---

## Cryptography Design
- **Key Derivation:** Argon2 (password → encryption key)
- **Encryption:** AES-256 symmetric encryption
- **Storage:** Local encrypted file (JSON-based schema)
- **Threat model:** Protect stored credentials at rest using strong KDFs and
  encryption, without relying on external services

---

## Tech Stack
- **Python**
  - PyCryptodome (AES encryption, padding)
  - Argon2 password hashing / KDF
  - Local encrypted file storage
- **JavaScript / HTML**
  - Browser extension prototype
  - Web Crypto API (`crypto.subtle`)
  - Asynchronous cryptographic workflows
- JSON for portable data storage

---

## What I Learned
- Implementing secure password-based encryption using **KDFs (Argon2)**
- Correct use of AES encryption and padding
- Designing a portable, encrypted file format
- Adapting cryptographic logic across programming languages
- Working with asynchronous cryptographic APIs in browser environments
- Understanding practical tradeoffs between CLI tools and browser-based security models

---

## Future Improvements
- Complete browser extension UI and workflow
- Integrate full encryption and write support into the extension
- Improve UX around password creation and management
- Add password generation and search functionality
- Security hardening and threat-model review

---

## Notes
This project is intended for educational purposes and experimentation with
practical cryptography. It is not intended for production use.
