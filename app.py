from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# initialize flask
app = Flask(__name__)
# initialize sqlalchemy
# three /// is relative path, four //// is exact path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# initialize database
db = SQLAlchemy(app)

# Create model
class Todo(db.Model):
    # create columns
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    # function to return a string everytime a new element is created
    def __repr__(self):
        return '<Task %r>' % self.id


# index route
@app.route('/', methods=['POST', 'GET']) # adds two methods to this route
# define function for that route
def index():
    # if the request sent to this method is POST...
    if request.method == 'POST':
        # logic for adding a task
        task_content = request.form['content']
        # create model for this, create todo object
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding task'
    else:
        # this looks at all the db content in the order it was created and return all
        tasks = Todo.query.order_by(Todo.date_created).all()
        # display all current tasks in table
        return render_template('index.html', tasks=tasks)
    
# ROUTE FOR DELETE
@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'

# ROUTE FOR UPDATE
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']
        
        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating the task'
    else:
        return render_template('update.html', task=task)

if __name__ == "__main__":
    app.run(debug=True)