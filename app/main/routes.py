from flask import Blueprint, render_template
from flask_login import login_required

main = Blueprint('main', __name__)

@main.route('/')
@login_required
def dashboard():
    # Logic to fetch and display user dashboard
    return render_template('MUC_listuserui.html')