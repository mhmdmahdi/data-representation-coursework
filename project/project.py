# Mohammed Mahdi (G00411358)
# Data Representation
# Flask Application

import logging
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from dbconfig import mysql
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{mysql['user']}:{mysql['password']}@{mysql['host']}/{mysql['database']}"
db = SQLAlchemy(app)
logging.basicConfig(level=logging.DEBUG)

class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Exercise = db.Column(db.String(255), nullable=False)
    Sets = db.Column(db.Integer, nullable=False)
    Reps = db.Column(db.Integer, nullable=False)
    Weight = db.Column(db.Float)  

@app.route('/')
def index():
    app.logger.info('Endpoint: /')
    return render_template('personalbest.html')

@app.route('/get_all_data', methods=['GET'])
def get_all_data():
    app.logger.info('Endpoint: /get_all_data')
    exercises = Exercise.query.all()
    data = [{"id": exercise.id, "Exercise": exercise.Exercise, "Sets": exercise.Sets, "Reps": exercise.Reps, "Weight": exercise.Weight} for exercise in exercises]
    return jsonify(data)

@app.route('/', methods=['POST'])
def create():
    app.logger.info('Endpoint: / (POST)')
    try:
        data = request.get_json()
        new_exercise = Exercise(Exercise=data['Exercise'], Sets=data['Sets'], Reps=data['Reps'], Weight=data.get('Weight'))
        db.session.add(new_exercise)
        db.session.commit()
        app.logger.info('Exercise created successfully')
        return jsonify({"message": "Exercise created successfully"})
    except Exception as e:
        app.logger.error(f'Error creating exercise: {str(e)}')
        return jsonify({"error": "Error creating exercise"}), 500

@app.route('/<int:id>', methods=['PUT'])
def update(id):
    app.logger.info(f'Endpoint: /{id} (PUT)')
    try:
        data = request.get_json()
        exercise = Exercise.query.get(id)

        if exercise is None:
            return jsonify({"error": f"Exercise with ID {id} not found"}), 404

        if 'Exercise' in data:
            exercise.Exercise = data['Exercise']

        if 'Sets' in data:
            exercise.Sets = data['Sets']

        if 'Reps' in data:
            exercise.Reps = data['Reps']

        if 'Weight' in data:
            exercise.Weight = data['Weight']

        db.session.commit()
        app.logger.info('Exercise updated successfully')
        return jsonify({"message": "Exercise updated successfully"})
    except SQLAlchemyError as e:
        db.session.rollback()
        app.logger.error(f'Error updating exercise: {str(e)}')
        return jsonify({"error": f"Error updating exercise: {str(e)}"}), 500
    except Exception as e:
        app.logger.error(f'Unhandled error updating exercise: {str(e)}')
        return jsonify({"error": "Unhandled error updating exercise"}), 500

@app.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    app.logger.info(f'Endpoint: /delete/{id} (DELETE)')
    try:
        exercise = Exercise.query.get(id)

        if exercise is None:
            return jsonify({"error": f"Exercise with ID {id} not found"}), 404

        db.session.delete(exercise)
        db.session.commit()
        app.logger.info(f'Exercise {id} deleted successfully')
        return jsonify({"message": f"Exercise {id} deleted successfully"})
    except Exception as e:
        app.logger.error(f'Error deleting exercise: {str(e)}')
        return jsonify({"error": "Error deleting exercise"}), 500

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host='mhmdmahdi1.pythonanywhere.com', port=5000, debug=True)
