from flask import Flask, request, jsonify

app = Flask(__name__)   

valid_licenses = {
    '123456789999':'valid',
    'XZXZXZXZXZXZ':'valid'
}

@app.route('/verify_license', methods=['POST'])
def verify_license():
    data = request.get_json()
    license_key = data.get("license_key")
    if license_key in valid_licenses:
        return jsonify({"status":"valid"})
    else:
        return jsonify({"status":"invalid"})
    
if __name__ == '__main__':
    app.run(debug=True)