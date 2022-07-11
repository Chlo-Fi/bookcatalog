#app\__init__.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_type): # dev, test, or prod
    app = Flask(__name__)
    # cwd = current working directory
    configuration = os.path.join(os.getcwd(), 'config', config_type + '.py')
    app.config.from_pyfile(configuration)

    print('Initializing database...')
    db.init_app(app)

    from app.catalog import main
    app.register_blueprint(main)

    return app