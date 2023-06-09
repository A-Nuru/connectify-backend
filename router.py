from flask import Flask, render_template, request, redirect
from controllers import UserController
from database import initialize_database

app = Flask(__name__)

@app.route('/')
def index():
    users = UserController.get_all_users()
    return render_template('index.html', users=users)

@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    UserController.register_user(username, password)
    return redirect('/')

if __name__ == '__main__':
    initialize_database()
    app.run(debug=True)
