
from flask import Flask, render_template, request# library
## module - flask
## class - Flask

app = Flask(__name__) # initializing object

@app.route("/", methods=['GET']) # route # get
def index():
    return render_template('index.html')

## routes - > GET, POST
@app.route("/add", methods=['POST'])
def addStudent():
    data = request.form
    # print("data====", data)
    # return "New Student details added"
    user = data['user']
    college = data['college']
    return "Welcome {0}. Your college is: {1}".format(user, college)

if __name__ == "__main__": # starting point of the application
    app.run(
        host="127.0.0.1",
        port=8000,
        debug=True)
