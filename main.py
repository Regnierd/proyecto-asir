from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import flash
from flask import session
from flask import url_for
from program import User, Login, EditProfile
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
    success = None
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
            success = "Te has registrado correctamente."
            return render_template('index.html', success=success)
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
             error = "Credenciales incorrectas o no exite la cuenta. \
                    Para ello registrese pulsando en el botón de abajo."
        return render_template('index.html', error = error)
@app.route("/perfil", methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        salt = b'supercalifragilisticoespialidous'
        password = password.encode('utf-8')
        dk = hashlib.pbkdf2_hmac('sha256', password, salt, 100000)
        password_encriptada = dk.hex()
        if name != "" and  email != "" and password_encriptada != "":
            profile = EditProfile(name, email, password_encriptada, session["name"])
            profile.edit()
        elif name == "" and email != "" and password_encriptada != "":
            profile = EditProfile(session["name"], email, password_encriptada, session["name"])
        elif

        return render_template('principal.html')
    return render_template('perfil.html')

@app.route("/salir")
def disconnect():
    logout = None
    session.clear()
    logout = "Sesión cerrada correctamente."
    return render_template('index.html', logout=logout)

if __name__ == "__main__":
    app.run(debug = True)
