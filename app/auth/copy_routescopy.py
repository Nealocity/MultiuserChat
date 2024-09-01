from flask import request, jsonify, render_template, redirect, url_for, flash
from flask.views import MethodView
from app.auth import auth
from werkzeug.security import check_password_hash
from app.models import User

class LoginAPI(MethodView):
    def get(self):
        return render_template('MUC_loginui.html')  # Render the login HTML page

    def post(self):
        # Get the form data
        username = request.form.get('username')
        password = request.form.get('password')

        # Query the database to find the user
        user = User.query.filter_by(username=username).first()

        # Check if the user exists and the password is correct
        if user and check_password_hash(user.password, password):
            # If successful, redirect to the list of users (or another page)
            flash('Login successful!', 'success')
            return redirect(url_for('main.list_users'))
        else:
            # If authentication fails, show an error message
            flash('Invalid username or password.', 'danger')
            return redirect(url_for('auth.login'))

# Register the URL rule for login using the `MethodView`
login_view = LoginAPI.as_view('login')
auth.add_url_rule('/login', view_func=login_view, methods=['GET', 'POST'])
