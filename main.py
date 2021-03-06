
from flask import Flask, render_template, request, redirect, url_for# library
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
@app.route("/add", methods=['GET', 'POST'])
def addStudent():
    if request.method == 'POST': # POST
        data = request.form
        user = data['user']
        college = data['college']
        studentsList.append({
            'name': user,
            'college': college
        })
        # return "Welcome {0}. Your college is: {1}".format(user, college)
        return redirect(url_for('index'))
    else: # GET
        return render_template('addStudent.html')

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

@app.route("/update/<string:name>", methods=['GET', 'POST'])
def updateStudent(name):
    for i in studentsList:
        if i['name'] == name:
            # return "Student name is : {0}\nStudent college is: {1}".format(i['name'], i['college'])
            if request.method == 'POST':
                data = request.form
                college = data['college']
                i['college'] = college
                return redirect(url_for('index'))
            else:
                return render_template('updateStudent.html', student=i)

if __name__ == "__main__": # starting point of the application
    app.run(
        host="127.0.0.1",
        port=8000,
        debug=True)
