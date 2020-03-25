from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import flash
from flask import session
from program import User, Login
import hashlib

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
        salt = b'supercalifragilisticoespialidous'
        password = password.encode('utf-8')
        dk = hashlib.pbkdf2_hmac('sha256', password, salt, 100000)
        password_encriptada = dk.hex()
        #creamos un usuario
        user = User(name, email, password_encriptada)
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
        salt = b'supercalifragilisticoespialidous'
        password = password.encode('utf-8')
        dk = hashlib.pbkdf2_hmac('sha256', password, salt, 100000)
        password_encriptada = dk.hex()
        log = Login(email, password_encriptada)
        log.login()
        if password_encriptada == dk.hex():
            return render_template('principal.html')
        else:
            return render_template('index.html')

if __name__ == "__main__":
    app.run(debug = True)
