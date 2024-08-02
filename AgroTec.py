from flask import Flask, request, jsonify
import os

app = Flask(__name__)

valid_licenses = {
    "CHAVE-EXEMPLO-VALIDA": "valid",
    "OUTRA-CHAVE-VALIDA": "valid"
}

@app.route('/verify_license', methods=['POST'])
def verify_license():
    if request.content_type != 'application/json':
        return jsonify({"error": "Invalid Content-Type"}), 415
    
    data = request.get_json()
    if not data or 'license_key' not in data:
        return jsonify({"error": "Missing license_key"}), 400
    
    license_key = data['license_key']
    if license_key in valid_licenses:
        return jsonify({"status": "valid"})
    else:
        return jsonify({"status": "invalid"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
