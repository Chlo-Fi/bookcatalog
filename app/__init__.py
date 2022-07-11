#app\__init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

db = SQLAlchemy()
bootstrap = Bootstrap()

def create_app(config_type): # dev, test, or prod
    app = Flask(__name__)
    # cwd = current working directory
    configuration = os.path.join(os.getcwd(), 'config', config_type + '.py')
    app.config.from_pyfile(configuration)

    print('Binding database to app...')
    db.init_app(app)
    print('Initializing bootstrap...')
    bootstrap.init_app(app)

    from app.catalog import main
    app.register_blueprint(main)

    return app