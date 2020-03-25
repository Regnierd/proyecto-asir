from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import flash
from flask import session
from program import users, loggins
import bcrypt

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inicio')
def inicio():
    if 'name' in session:
        return render_template('principal.html')
    else:
        return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        #codigo para encriptamiento
        salt = bcrypt.gensalt()
        password = password.encode()
        password_encriptada = bcrypt.hashpw(password, salt)

        #creamos un usuario
        user = users(name, email, password_encriptada)
        user.add_user()

        #Hago un registro de la sesión.
        #session["name"] = name
        #session["email"] = email

        return redirect('/index')
        print(repr(password_encriptada))
    else:
        return render_template('register.html')

@app.route('/index', methods=['GET', 'POST'])
def connected():
    if request.method == 'GET':
        if 'name' in session:
            return render_template('principal.html')
        else:
            return render_template('index.html')
    else:
        email = request.form["email"]
        password = request.form["password"]
        log = loggins(email, password)
        log.login()
        return render_template('principal.html')


if __name__ == "__main__":
    app.run(debug = True)
