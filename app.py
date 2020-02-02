from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# our app name will be app, since the file is called app.py
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']= 'postgres://ibrahimelgohary@localhost:5432/todoapp'

db = SQLAlchemy(app)

# inheriting from db.Model and to be linked to sqlalchemy
# we will be defining our model
class Todo(db.Model):
	__tablename__ = 'todos'
	id = db.Column(db.Integer, primary_key=True)
	description = db.Column(db.String(), nullable=False)

# for debugging within the Todo class:
	def __repr__(self):
		return f'<Todo {self.id} {self.description}>'

# to make sure everything was created in the database: 
db.create_all()	

#we get the description from the form
#create an object todo using the Todo class
# we add todo to the database and commit the changes
# we redirect to index route to display the modified view
@app.route('/todos/create', methods=['POST'])
def create_todo():
  description = request.form.get('description', '')
  todo = Todo(description=description)
  db.session.add(todo)
  db.session.commit()
  return redirect(url_for('index'))

@app.route('/')
def index():
    return render_template('index.html',data=Todo.query.all())

