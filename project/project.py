from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from dbconfig import mysql

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{mysql['user']}:{mysql['password']}@{mysql['host']}/{mysql['database']}"
db = SQLAlchemy(app)

class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Exercise = db.Column(db.String(255), nullable=False)
    Sets = db.Column(db.Integer, nullable=False)
    Reps = db.Column(db.Integer, nullable=False)

@app.route('/')
def index():
    return render_template('personalbest.html')

# Endpoint for fetching all data
@app.route('/get_all_data', methods=['GET'])
def get_all_data():
    # Your logic to fetch and return data
    exercises = Exercise.query.all()
    data = [{"id": exercise.id, "Exercise": exercise.Exercise, "Sets": exercise.Sets, "Reps": exercise.Reps} for exercise in exercises]
    return jsonify(data)

# Endpoint for creating
@app.route('/', methods=['POST'])
def create():
    # Your logic to fetch and return data
    data = request.get_json()
    new_exercise = Exercise(Exercise=data['Exercise'], Sets=data['Sets'], Reps=data['Reps'])
    db.session.add(new_exercise)
    db.session.commit()
    return jsonify({"message": "Exercise created successfully"})

# Endpoint for updating
@app.route('/<int:id>', methods=['PUT'])
def update(id):
    data = request.get_json()
    exercise = Exercise.query.get(id)
    exercise.Exercise = data['Exercise']
    exercise.Sets = data['Sets']
    exercise.Reps = data['Reps']
    db.session.commit()
    return jsonify({"message": "Exercise updated successfully"})

# Endpoint for deleting
@app.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    exercise = Exercise.query.get(id)
    db.session.delete(exercise)
    db.session.commit()
    return jsonify({"message": f"Exercise {id} deleted successfully"})

if __name__ == "__main__":
    db.create_all()
    app.run(host='0.0.0.0', port=5001, debug=True)

# Continue from 4. Update JavaScript AJAX Requests: