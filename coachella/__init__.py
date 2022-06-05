#   Application factory to create a Flask 
#   instance globally. Any setup the application 
#   needs will  happen inside a function 
#   before returning the application.

import os

from . import coachella
from . import db
from flask import Flask

# Application factory function
def create_app (test_config = None):
    # Create and configure app. We use '__name__'
    # to know where the current Python module is located
    # in order to set up some paths. 
    # We also let the Flask application know that configuration
    # files are relative to the instance folder located outside
    # the 'coachella' package, and holds data like configuration
    # secrets and database file.
    app = Flask (__name__, instance_relative_config = True)

    #app.config.setdefault('MYSQL_HOST', 'localhost')
    #app.config.setdefault('MYSQL_USER', 'root')
    #app.config.setdefault('MYSQL_PASSWORD', 'Jack_Rourke_343')
    #app.config.setdefault('MYSQL_DB', 'saes')

    # We set default configuration for the app to use.
    #
    # - SECRET_KEY is used to keep data safe.
    #   'dev' is a provisional value, and SHOULD BE
    #   OVERRIDEN DURING DEPLOYMENT with a random value.
    #
    # - DATABASE is the path where the MySQL file will be saved.
    #   It's under app.instance path.
    app.config.from_mapping (
        SECRET_KEY = 'dev',
        MYSQL_HOST = 'localhost',
        MYSQL_USER = 'root',
        #MYSQL_PORT = 3001,
        MYSQL_PASSWORD = 'Jack_Rourke_343',
        MYSQL_DB = 'saes'
        # MYSQL_DB = os.path.join (app.instance_path, saes.sql)
    )
    
    # Override default configuration with a 'config.py' file
    # only if it exists in the instance folder (this can
    # contain a real SECRET_KEY, for example)
    #
    # test_config allows to write independently-configured tests
    # regardless of the development values used 
    if test_config is None:
        app.config.from_pyfile ('config.py', silent = True)
    else:
        app.config.from_mapping (test_config)

    # Ensure that app.instance_path exists. It needs to be
    # created to setup the MySQL database there.
    try:
        os.makedirs (app.instance_path)
    except OSError:
        pass

    # Simple test route
    @app.route ('/hello')
    def hello ():
        return "Hello, world!"

    # Call the 'init_app ()' function from the factory
    db.init_app (app)

    # Import and register coachella blueprint from factory
    app.register_blueprint (coachella.bp)

    return app