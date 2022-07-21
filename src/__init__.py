import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


from src.Auth.auth import auth
from src.Branch.branch import branch
from src.Auth.database import db
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    


    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY'),
        SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DB_URI'),
        SQLALCHEMY_TRACK_MODIFICATIONS = False
    )
        
    else:
        
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)
    db.init_app(app)
    app.register_blueprint(auth)
    app.register_blueprint(branch)
    return app
