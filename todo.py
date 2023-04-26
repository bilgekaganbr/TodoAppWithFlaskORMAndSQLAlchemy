#importing Flask and SQLAlchemy modules
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

#creating an intance of Flask(definition of the application)
app = Flask(__name__)
#configuring the uri for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/Admin/OneDrive/Masaüstü/PythonCodes/Todo App with Flask, ORM, and SqlAlchemy/TodoApp/todo.db'
#creating an instance of SQLAlchemy
db = SQLAlchemy(app)

#defining the route for the main page of the web application
@app.route("/")
def index():

    #query all the items from the Todo table
    todos = Todo.query.all()

    #render the template with the todos
    return render_template("index.html", todos = todos) 

#defining the route for adding a new todo item
@app.route("/add", methods=["POST"])
def add():

    #get the title of the new todo item from the form
    title =  request.form.get("title")
    
    #create a new Todo object
    newTodo = Todo(title = title, complete = False)

    #add the new todo item to the database
    db.session.add(newTodo)

    #update the database
    db.session.commit()

    #redirect to the main page
    return redirect(url_for("index"))

#defining the route for marking a todo item as complete
@app.route("/complete/<string:id>")
def complete(id):

    #find the todo item with the given id
    todo = Todo.query.filter_by(id = id).first()
    
    #toggle the complete status of the todo item
    todo.complete = not todo.complete

    #update the database
    db.session.commit()

    #redirect to the main page
    return redirect(url_for("index"))

#defining the route for deleting a todo item
@app.route("/delete/<string:id>")
def delete(id):

    #find the todo item with the given id
    todo = Todo.query.filter_by(id = id).first()

    #delete the todo item from the database
    db.session.delete(todo)

    #update the database
    db.session.commit()

    #redirect to the main page
    return redirect(url_for("index"))

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