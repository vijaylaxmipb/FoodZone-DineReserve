import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env  

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL", "sqlite:///site.db")  # Default to SQLite if DB_URL is not set
print("SQLALCHEMY_DATABASE_URI:", app.config["SQLALCHEMY_DATABASE_URI"])
db = SQLAlchemy(app)

from taskmanager import routes
