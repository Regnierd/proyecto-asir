from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from program import users


app = Flask(__name__)
#user = users()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        id_user = 1
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        users.add_user(id_user, name, email, password)
        return redirect('/')
    else:
        return render_template('register.html')
