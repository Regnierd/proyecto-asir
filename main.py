from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from program import users


app = Flask(__name__)
#user = users()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            email = request.form["email"]
            password = request.form["password"]
            user.login(email, password)
        except IndexError:
            return render_template('index.html', mensaje="No eres usuario")

    return render_template('index.html')

@app.route('/register', methods=['POST'])
def create_user():
    if request.method == 'POST':
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        users.add_user(name, email, password)
        return redirect('/')
    else:
        return render_template('register.html')

if __name__ == "__main__":
    app.run(debug = True)
