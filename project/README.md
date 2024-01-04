# Mohammed Mahdi (G00411358)
# Data Representation

# Personal Best Tracker

## Description

Personal Best Tracker is a web application that allows users to track their exercise routines, including details like sets, reps, and weight. It provides a user-friendly interface to manage and view personal bests for different exercises.

## Getting Started

To get started with Personal Best Tracker on your local machine, follow these steps:

### Prerequisites

- Python
- Flask
- MySQL

### Installation

1.  Clone the repository: `git clone https://github.com/mhmdmahdi/data-representation-coursework.git`
    cd to 'project' folder and open 'project.py' which contains the Flask Application.
    Templates folder contains the html file
2.  Install dependencies: `pip install -r requirements.txt`
3.  Set up a database:
    - If running locally: `python create_db.py`. Ensure to set up table as per below commands:
        create table exercise(
            id int NOT NULL AUTO_INCREMENT,
            exercise varchar(250),
            sets varchar(250),
            reps varchar(250),
            weight varchar(250),
            PRIMARY KEY id,
        )
    - If running on PythonAnywhere: Database setup is handled on the PythonAnywhere platform. Same instructions as above for database creation. 

4.  Run the application: `python project.py`
5.  Link below for project result hosted on pythonanywhere,
    which ties together the html code on client side, 
    the flask server and the mysql database:

    https://mhmdmahdi1.pythonanywhere.com/

## Usage

- Access the application at http://127.0.0.1:5000/ or https://mhmdmahdi1.pythonanywhere.com/ depending on if you want to view it locally or on the host site.
- View, create, update, and delete exercises using the web interface.

## Endpoints/Features

- **GET /get_all_data:** Retrieve all exercise data.
- **POST /:** Create a new exercise.
- **PUT /<id>:** Update an existing exercise.
- **DELETE /delete/<id>:** Delete an exercise.

## Technologies Used

- Python
- Flask (API)
- SQLAlchemy (API)
- Bootstrap CDN (API)
- JQuery MySQL
- AJAX (API)

## Database

The application uses MySQL to store exercise data. The database structure is managed by SQLAlchemy.


## Acknowledgments

- Thanks to [Bootstrap](https://getbootstrap.com/) for the front-end framework.
- Thanks to [Pythonanywhere](https://mhmdmahdi1.pythonanywhere.com/) for the free hosting services and database executions
- Thanks to [Lecturer]Andrew Beatty (email:andrew.beatty@atu.ie) for the guidance over the semester and throughout the course 'Higher Diploma in Science in Data Analytics' at 'Atlantic Technological University'.

## Contact Information

For questions or feedback, contact [Mohammed Mahdi](mailto:mhmd.mahdi1@gmail.com)

## Demo

Live demo [here](https://mhmdmahdi1.pythonanywhere.com/)