
from flask import Flask, render_template, request# library
## module - flask
## class - Flask

studentsList = [
    {
        'name': 'Udit',
        'college': 'DIT'
    },
    {
        'name': 'Tushar',
        'college': 'DIT'
    },
    {
        'name': 'Gurjas',
        'college': 'DIT'
    }]

app = Flask(__name__) # initializing object

@app.route("/") # route # get
def index():
    return render_template('index.html', studentsList = studentsList)

## routes - > GET, POST
@app.route("/add", methods=['POST'])
def addStudent():
    data = request.form
    # print("data====", data)
    # return "New Student details added"
    user = data['user']
    college = data['college']
    studentsList.append({
        'name': user,
        'college': college
    })
    return "Welcome {0}. Your college is: {1}".format(user, college)

@app.route("/delete/<string:name>", methods=['GET'])
def deleteStudent(name):
    indexToBeDeleted = -1 # 0
    for i in range(len(studentsList)):
        if studentsList[i]['name'] == name: # XYZ # Udit
            indexToBeDeleted = i
            break
    if (indexToBeDeleted != -1):
        del studentsList[indexToBeDeleted]
        return "Student deleted"
    return "Student does not exist"

if __name__ == "__main__": # starting point of the application
    app.run(
        host="127.0.0.1",
        port=8000,
        debug=True)
