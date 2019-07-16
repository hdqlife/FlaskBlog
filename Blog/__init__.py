import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

base_dir=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

template=os.path.join(base_dir,"templates")
static=os.path.join(base_dir,"static")

app=Flask(__name__,template_folder=template,static_folder=static)

sqlite_db="sqlite:///"+os.path.join(base_dir,"article.sqlite3")
app.config["SQLALCHEMY_DATABASE_URI"]=sqlite_db
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=True

db=SQLAlchemy(app)
