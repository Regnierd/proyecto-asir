from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import flash
from flask import session
from flask import url_for
from program import User, Login
import hashlib

app = Flask(__name__)

app.secret_key = "appLogin"



@app.route('/')
def index():
    if 'email' in session:
        return redirect('/principal')
    else:
        return render_template('index.html')

@app.route('/principal')
def inicio():
    if 'email' in session:
        return render_template('principal.html')
    else:
        return redirect('/')

@app.route('/register', methods=['GET', 'POST'])
def create_user():
    error_user = None
    if request.method == 'GET':
        if 'email' in session:
            return redirect('/principal')
        else:
            return render_template('register.html')
    elif request.method == 'POST':
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
        try:
            user.add_user()
            return redirect('/')
        except:
            error_user = "El email ya existe."
            return render_template('register.html', error_user=error_user)


@app.route('/principal', methods=['GET', 'POST'])
def connected():
    if request.method == 'GET':
        if 'email' in session:
            return render_template('principal.html')
        else:
            return render_template('index.html')
    else:
        error = None
        email = request.form["email"]
        password = request.form["password"]
        salt = b'supercalifragilisticoespialidous'
        password = password.encode('utf-8')
        dk = hashlib.pbkdf2_hmac('sha256', password, salt, 100000)
        password_encriptada = dk.hex()
        log = Login(email, password_encriptada)
        datos_log = log.login()
        if datos_log != None:
            session["name"] = datos_log
            session["email"] = email
            return render_template('principal.html')
        else:
             error = "Credenciales incorrectas."
        return render_template('index.html', error = error)

@app.route("/salir")
def disconnect():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug = True)
