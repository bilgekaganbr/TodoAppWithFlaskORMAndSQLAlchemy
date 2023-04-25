#importing Flask and SQLAlchemy modules
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#creating an intance of Flask(definition of the application)
app = Flask(__name__)
#configuring the uri for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/Admin/OneDrive/Masaüstü/PythonCodes/Todo App with Flask, ORM, and SqlAlchemy/TodoApp/todo.db'
#creating an instance of SQLAlchemy
db = SQLAlchemy(app)

#defining the database table for Todo items
class Todo(db.Model):

    #defining columns of the table
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    complete = db.Column(db.Boolean)

#checking if the current file is being run as the main program
if __name__ == "__main__":
    
    #creating all tables defined in the app
    with app.app_context():

        db.create_all()

    #starting the Flask application in debug mode
    app.run(debug=True)