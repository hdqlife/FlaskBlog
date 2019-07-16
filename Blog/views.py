from Blog import app
from Blog.models import Article
from flask import render_template

@app.route("/say_hello/")
def say_hello():
    return  "hello world"

@app.route("/")
def index():
    return render_template("index.html")


