from os import getenv
from app import app
from flask_sqlalchemy import SQLAlchemy
from flask import session
from sqlalchemy.sql import text

app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

#db.py