from whispyr.config import Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    from whispyr.main.routes import main

    app.register_blueprint(main)

    with app.app_context():
        db.create_all()

    return app
