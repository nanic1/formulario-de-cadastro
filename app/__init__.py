import os
from flask import Flask, app
from flask_sqlalchemy import SQLAlchemy
import pymysql
from dotenv import load_dotenv

db = SQLAlchemy()

# load .env acess
load_dotenv()

# create db if not exist on MySQL workbench
def create_database():
    connection = pymysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

    cursor = connection.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {os.getenv('DB_NAME')}")
    connection.commit()
    cursor.close()
    connection.close()

# create tables if not exist on MySQL workbench
def create_app():
    # setting directories for templates and static files
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    templates_dir = os.path.join(base_dir, "templates")
    static_dir = os.path.join(base_dir, "static")

    app = Flask(__name__, template_folder=templates_dir, static_folder=static_dir)
    create_database()

    app.config.from_object("app.config.Config")

    db.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    with app.app_context():
        db.create_all()

    return app