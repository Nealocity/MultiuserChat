from flask import redirect, url_for, render_template, request
from app.main import main
from app.models import User

@main.route('/')
def index():
    return redirect(url_for('auth.login'))

@main.route('/list_users')
def list_users():
    users = User.query.all()
    return render_template('MUC_listuserui.html', users=users)

@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Handle registration logic
        pass
    return render_template('MUC_register.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login logic
        pass
    return render_template('MUC_loginui.html')