from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Your endpoint for fetching all data
@app.route('/get_all_data', methods=['GET'])
def get_all_data():
    # Your logic to fetch and return data
    data = {"example": "data"}
    return jsonify(data)

@app.route('/')
def index():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
