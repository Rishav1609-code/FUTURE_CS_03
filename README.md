# 🔐 Secure File Sharing System

## 📌 Overview

A lightweight secure file sharing web application built as part of a Cybersecurity internship project. The system encrypts files using **AES** before storage or transfer, enforces secure key handling, and provides a simple Flask-based web UI for uploading and downloading encrypted files.

---

## ✨ Features

* **AES file encryption** for confidentiality and integrity
* **Automatic encryption/decryption** on upload and download
* **Secure key handling** — keys are generated securely and not stored in plain text
* **Flask web interface** for intuitive file operations
* **Documentation** that details the encryption design and key lifecycle

---

## 🏗️ Project Structure

```
FUTURE_CS_03/
├── app.py                    # Flask application entrypoint
├── requirements.txt          # Python dependencies
├── /docx                     # Encryption methods & key handling explained
├── /templates                # HTML templates
├── /screenshots              # UI & codes screenshots
├── /video                    # Walkthrough/demo video
│── /dencrypted               # Stores all decrypted files
│── /encrypted                # Stores all encrypted files
│── /uploads_files            # Stores all uploaded files before processing
└── README.md                 # Project documentation
```

---

## ⚙️ Tech Stack

* Python 3
* Flask (web framework)
* Cryptography library (AES) for encryption
* HTML / CSS / JavaScript for the frontend
* Git & GitHub for version control

---

## 🚀 Installation

1. Clone the repository:

```bash
git clone <repo-url>
cd FUTURE_CS_03
```

2. Create and activate a virtual environment:

* Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

* Windows

```powershell
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
python app.py
```

5. Open the app in your browser at `http://127.0.0.1:5000`.

---

## 📂 Usage

* Use the **Upload** page to select and upload a file — it will be encrypted and stored.
* Use the **Download** page to retrieve and decrypt a stored file (requires the correct key/credentials).
* See `Security_Overview.docx` for details on key generation, storage, and the encryption workflow.

---

## 🛡️ Security Notes

* Files are encrypted with AES; keys are generated securely and are never stored in plaintext.
* Always run the app behind TLS (HTTPS) in production.
* Add proper authentication and authorization before deploying publicly.
* Review `Security_Overview.docx` for the threat model and recommended hardening steps.

---

## 📽️ Deliverables

* Well-documented source code (GitHub repo)
* Walkthrough/demo video showing the encryption/decryption flow
* Security overview document covering encryption and key management
* Project screenshots for quick reference

---

## 📬 Author
**Rishav Raj** – Cyber Security Intern @ Future Interns

---
👉 Star ⭐ this repository if you found it helpful!

