from flask import Flask, render_template

app = Flask(__name__)

# index route
@app.route('/')
# define function for that route
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)