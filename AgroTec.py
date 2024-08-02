from flask import Flask, request, jsonify

app = Flask(__name__)

valid_licenses = {
    "CHAVE-EXEMPLO-VALIDA": "valid",
    "OUTRA-CHAVE-VALIDA": "valid"
}

@app.route('/verify_license', methods=['POST'])
def verify_license():
    data = request.get_json()
    license_key = data.get("license_key")
    if license_key in valid_licenses:
        return jsonify({"status": "valid"})
    else:
        return jsonify({"status": "invalid"})

if __name__ == '__main__':
    # Bind to 0.0.0.0 to accept connections from any IP
    # Use the PORT environment variable to listen on the correct port
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
