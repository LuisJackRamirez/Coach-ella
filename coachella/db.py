import click
import pymysql

from flask import current_app, g
from flask.cli import with_appcontext
from mysql.connector import errorcode

def execute_init_query (db):
    with current_app.open_resource ('schema.sql') as f:
        ret = f.read ().decode ("utf8").split (';')
        ret.pop ()

        for sql_request in ret:
            db.cursor ().execute (sql_request + ';')

        db.commit ()

def get_db ():
    # Create a connection to a database.
    # Any query and operations are performed
    # using that connection, which is closed
    # after the work is finished.
    if 'db' not in g:
        try:
            # The object 'g' stores data that might
            # be accessed during any given request.
            # We save the connection and re-use it
            # instead of creating a new one if 
            # "get_db ()" is called a second time
            # during the same request.
            #
            # "current_app" points to the Flask application
            # handling the request. Even though there is no
            # application at the moment of writing the code,
            # "get_db ()" will be called when the application 
            # has been created, so "current_app" can be used.
            #
            # We establish a connection to the database with
            # the configuration from the current_app, which,
            # again, won't exist until we initialize the app.
            g.db = pymysql.connect (
                user = current_app.config["MYSQL_USER"], 
                password = current_app.config["MYSQL_PASSWORD"],
                host = current_app.config["MYSQL_HOST"]
            )
        except Exception as e:
            print (e)
            # g.db.row_factory = g.db.cursor (dictionary = True)
        
        return g.db

# Check if a connection was created (g.db was set).
# If such connectino exists, it will be closed.
def close_db (e = None):
    db = g.pop ('db', None)

    if db is not None:
        db.close ()

def init_db ():
    db = get_db ()

    # Open "schema.sql" with a path relative to the package,
    # and use the connection with get_db to execute the SQL
    # commands read from the SQL file.
    db.cursor ().execute ("CREATE DATABASE IF NOT EXISTS saes;")
    db.select_db ("saes")
    execute_init_query (db)

# click.command () defines a command line command called
# 'init-db' so we can initialize the database and show a 
# success message to the user.
@click.command ('init-db')
@with_appcontext
def init_db_command ():
    # By executing the commands from "schema.sql",
    # we clear existing data and create new tables.
    init_db ()
    click.echo ('Initialized database')

# This function registers the close_db () 
# and init_db_command () functions so that 
# they can be used by the application.
def init_app (app):
    # Used by Flask to clean up after returning the response.
    app.teardown_appcontext (close_db)
    
    # Add a new command that can be called 
    # with the 'flask' command line command
    app.cli.add_command (init_db_command)