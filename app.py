from flask import Flask

app = Flask(__name__)

# index route
@app.route('/')
# define function for that route
def index():
    return "Hello, world!"

if __name__ == "__main__":
    app.run(debug=True)