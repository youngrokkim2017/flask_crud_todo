from flask import Flask, render_template, url_for
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
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)