from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from program import users, loggins


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        user = users(name, email, password)
        user.add_user()
        return redirect('/')
    else:
        return render_template('register.html')

@app.route('/index', methods=['GET', 'POST'])
def connected():
    if request.method == 'POST':
        try:
            email = request.form["email"]
            password = request.form["password"]
            log = loggins(email, password)
            log.login()
            return render_template('principal.html')

        except IndexError:
            return render_template('index.html', message='No estas registrado')

if __name__ == "__main__":
    app.run(debug = True)
