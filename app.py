from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
from wtforms.validators import InputRequired
import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

# Flask config
app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'

# Folders
UPLOAD_FOLDER = "static/encrypted"
DECRYPTED_FOLDER = "static/decrypted"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(DECRYPTED_FOLDER, exist_ok=True)

# AES key (must be 16, 24, or 32 bytes)
AES_KEY = get_random_bytes(16)

class UploadFileForm(FlaskForm):
    file = FileField("Choose File", validators=[InputRequired()])
    submit = SubmitField("Upload & Encrypt")

# --- Helper functions ---
def encrypt_file(file_data):
    cipher = AES.new(AES_KEY, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(file_data)
    return cipher.nonce, tag, ciphertext

def decrypt_file(nonce, tag, ciphertext):
    cipher = AES.new(AES_KEY, AES.MODE_EAX, nonce=nonce)
    return cipher.decrypt_and_verify(ciphertext, tag)

# --- Routes ---
@app.route("/", methods=["GET", "POST"])
def home():
    form = UploadFileForm()
    message = None

    if form.validate_on_submit():
        file = form.file.data
        filename = secure_filename(file.filename)
        file_data = file.read()

        # Encrypt file
        nonce, tag, ciphertext = encrypt_file(file_data)

        # Save encrypted file as base64 (nonce+tag+ciphertext)
        with open(os.path.join(UPLOAD_FOLDER, filename + ".enc"), "wb") as f:
            f.write(nonce + tag + ciphertext)

        message = f"✅ {filename} has been encrypted & uploaded!"
        flash(message, "success")
        return redirect(url_for("home"))

    # Get list of encrypted files
    files = os.listdir(UPLOAD_FOLDER)
    return render_template("index.html", form=form, files=files)

@app.route("/download/<filename>")
def download(filename):
    filepath = os.path.join(UPLOAD_FOLDER, filename)

    # Read encrypted content
    with open(filepath, "rb") as f:
        data = f.read()

    # Split nonce, tag, ciphertext
    nonce, tag, ciphertext = data[:16], data[16:32], data[32:]

    # Decrypt
    plaintext = decrypt_file(nonce, tag, ciphertext)

    # Save decrypted file
    original_name = filename.replace(".enc", "")
    decrypted_path = os.path.join(DECRYPTED_FOLDER, original_name)
    with open(decrypted_path, "wb") as f:
        f.write(plaintext)

    flash(f"📂 {original_name} has been decrypted!", "info")
    return send_from_directory(DECRYPTED_FOLDER, original_name, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
