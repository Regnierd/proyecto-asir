from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from program import users


app = Flask(__name__)
user = users()

@app.route('/register', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        name = varchar(request.form["name"])
        email = varchar(request.form["email"])
        password = varchar(request.form["password"])
        user.add_user(name, email, password)
        return redirect('/')
    else:
        return render_template('register.html')
