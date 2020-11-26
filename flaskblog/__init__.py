from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # to disable deprecation warning

# import secrets
# secrets.token_hex(16)
app.config["SECRET_KEY"] = "ecc3c74cde310eb6fc1d801b266aa3c8"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)

from flaskblog import routes