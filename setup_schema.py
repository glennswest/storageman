from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv, dotenv_values
import os

app = Flask(__name__)
load_dotenv()
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Node(db.Model):
      id     = db.Column(db.Integer, primary_key=True)
      name   = db.Column(db.String(128),index=True)
      ip     = db.Column(db.String(32),index=True)
      enable = db.Column(db.Boolean(), default=False)
      alive  = db.Column(db.Boolean(), default=False)
