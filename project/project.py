from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Your endpoint for fetching all data
@app.route('/get_all_data', methods=['GET'])
def get_all_data():
    # Your logic to fetch and return data
    data = {"example": "data"}
    return jsonify(data)

@app.route('/')
def index():
    return render_template('personalbest.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)



# pythonanywhere database password = datapassword