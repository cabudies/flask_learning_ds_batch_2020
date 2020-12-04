
from flask import Flask # library
## module - flask
## class - Flask

app = Flask(__name__) # initializing object

@app.route("/") # route
def index():
    print("print this message only in console")
    var = 10
    # return "hello data science batch - soai" + str(var)
    return "hello data science batch - soai - {}".format(var)

if __name__ == "__main__": # starting point of the application
    app.run(
        host="127.0.0.1",
        port=8000,
        debug=True)
