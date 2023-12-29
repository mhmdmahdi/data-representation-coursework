from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('personalbest.html')

# Endpoint for fetching all data
@app.route('/get_all_data', methods=['GET'])
def get_all_data():
    # Your logic to fetch and return data
    data = {"example1": "data1"}
    return jsonify(data)

# Endpoint for creating
@app.route('/post', methods=['POST'])
def post():
    # Your logic to fetch and return data
    data = {"example2": "data2"}
    return jsonify(data)

# Endpoint for updating
@app.route('/put', methods=['PUT'])
def post():
    # Your logic to fetch and return data
    data = {"example3": "data3"}
    return jsonify(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)



# pythonanywhere database password = datapassword