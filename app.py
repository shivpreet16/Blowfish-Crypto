from flask import Flask, request, jsonify, send_from_directory
from blowfish_1 import Blowfish

app = Flask(__name__)
# blowfish = None

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)


@app.route('/encrypt', methods=['POST'])
def encrypt_data():
    data = request.json.get('data')  # Assuming you receive data as JSON
    # global blowfish 
    blowfish = Blowfish(request.json.get('key'))
    encrypted_data = blowfish.blowFish_encrypt(data)
    return jsonify({'encrypted_data': encrypted_data})

@app.route('/decrypt', methods=['POST'])
def decrypt_data():
    data = request.json.get('data')  # Assuming you receive data as JSON
    blowfish = Blowfish(request.json.get('key'))
    decrypted_data = blowfish.blowFish_decrypt(data)
    return jsonify({'decrypted_data': decrypted_data})

if __name__ == '__main__':
    app.run(debug=True)