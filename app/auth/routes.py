from flask import request, jsonify, render_template, redirect, url_for
from flask.views import MethodView
from app.auth import auth

class LoginAPI(MethodView):
    def get(self):
        return render_template('MUC_loginui.html')  # Render the login HTML page

    def post(self):
        data = request.form
        username = data.get('username')
        password = data.get('password')
        # Here you'd normally authenticate the user
        if username == "admin" and password == "password":
            return jsonify({"message": "Login successful"}), 200
        return jsonify({"error": "Invalid username or password"}), 400

# Add the URL rule for login using the `MethodView`
login_view = LoginAPI.as_view('login')
auth.add_url_rule('/login', view_func=login_view, methods=['GET', 'POST'])
