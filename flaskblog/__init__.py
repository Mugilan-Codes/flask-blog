from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # to disable deprecation warning

# import secrets
# secrets.token_hex(16)
app.config["SECRET_KEY"] = "ecc3c74cde310eb6fc1d801b266aa3c8"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"

from flaskblog import routes