
from flask import Flask, render_template # library
## module - flask
## class - Flask

app = Flask(__name__) # initializing object

@app.route("/") # route # get
def index():
    return render_template('index.html')

## routes - > GET, POST
@app.route("/add")
def addStudent():
    return "New Student added"


if __name__ == "__main__": # starting point of the application
    app.run(
        host="127.0.0.1",
        port=8000,
        debug=True)
