from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db,  User, db
import smtplib
from email.message import EmailMessage

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def homepage():
    # View homepage and About Me

    return render_template("homepage.html")

@app.route("/contact", methods=["POST"])
def contact_me():
    # Send contact me form

    name = request.form.get("name")
    lname = request.form.get("lname")
    email = request.form.get("email")
    message = request.form.get("message")  

    s = smtplib.SMTP(host='smtp-relay.sendinblue.com', port=587)
    s.starttls()
    s.login('cadenamarlynn@gmail.com', 'TKbLGESCFdXVZO36')
    msg = EmailMessage()
    msg.set_content(f'Quote request from {email}, name = {name}, lname = {lname}, and the message is {message}'  )

    
    msg['Subject'] = ' Contact from Portfolio'
    msg['From'] = f'{email}'
    msg['To'] = 'Marlynn <cadenamarlynn@gmail.com>'

    s.send_message(msg)
    s.quit()
    
    return redirect("/")





if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)