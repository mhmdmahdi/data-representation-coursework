import logging
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
# import mysql.connector

app = Flask(__name__)
CORS(app, supports_credentials=True)  # Enable CORS for all routes

# Your endpoint for fetching all data
@app.route('/get_all_data', methods=['GET'])
@cross_origin(supports_credentials=True)  # Enable CORS for this specific route
def get_all_data():
    # Your logic to fetch and return data
    data = {"example": "data"}
    return jsonify(data)

@app.route('/')
def index():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)