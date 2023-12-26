import logging
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/get_all_data', methods=['GET'])
def get_all_data():
    # Your logic to fetch and return data
    data = {"example": "data"}
    return jsonify(data)

@app.route('/')
def index():
    return "Hello World!"

if __name__ == '__main__':
    app.run(debug=True)