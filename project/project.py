import logging
from flask import Flask
# import mysql.connector

app = Flask(__name__)

# Define a global database connection
# db = None

# Connect to the MySQL database
# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database=""
# )

@app.route('/')
def index():
    return "Hello World!"

if __name__ == "__main__":
    app.run(debug = True)