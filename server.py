from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db,  User, db

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def homepage():
    # View homepage and About Me

    return render_template("homepage.html")

@app.route("/contact")
def contact_me():
    #show contact me form

    fname = request.form.get("fname")
    lname = request.form.get("lname")
    email = request.form.get("email")
    message = request.form.get("message")
    
    return render_template("contact_me.html")

@app.route("/projects")
def projects():
    # Show projects main page

    return render_template("projects.html")


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)