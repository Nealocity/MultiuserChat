from flask import Flask,redirect, url_for
from app.main import main as main_blueprint
from app.auth import auth as auth_blueprint
from app.extensions import db, migrate

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/chat_db'
    app.config['SECRET_KEY'] = 'your_secret_key'

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)


    # Register blueprints
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    def index():
        return redirect(url_for('auth.login'))

    return app