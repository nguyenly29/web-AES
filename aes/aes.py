from flask import Flask, render_template, request, send_file, redirect, url_for
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

app = Flask(__name__)

def encrypt_file(file_path, key):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    with open(file_path, 'rb') as f:
        data = f.read()
    
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(data) + padder.finalize()

    encrypted = encryptor.update(padded_data) + encryptor.finalize()

    with open(file_path + '.enc', 'wb') as f:
        f.write(iv + encrypted)

def decrypt_file(file_path, key):
    with open(file_path, 'rb') as f:
        iv = f.read(16)
        encrypted_data = f.read()

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    decrypted_padded = decryptor.update(encrypted_data) + decryptor.finalize()

    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    decrypted_data = unpadder.update(decrypted_padded) + unpadder.finalize()

    with open(file_path[:-4], 'wb') as f:
        f.write(decrypted_data)

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ""
    if request.method == 'POST':
        action = request.form['action']
        key = request.form['key'].encode('utf-8')

        if len(key) != 16:
            message = "Key must be 16 bytes long!"
            return render_template('index.html', message=message)

        if action == 'encrypt':
            file = request.files['file']
            file_path = os.path.join('uploads', file.filename)
            file.save(file_path)
            encrypt_file(file_path, key)
            message = "File encrypted successfully!"
            return render_template('index.html', message=message)

        elif action == 'decrypt':
            file = request.files['file']
            file_path = os.path.join('uploads', file.filename)
            file.save(file_path)
            decrypt_file(file_path, key)
            message = "File decrypted successfully!"
            return render_template('index.html', message=message)

    return render_template('index.html', message=message)

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)