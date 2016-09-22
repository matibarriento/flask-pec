from flask import Flask, flash, redirect, render_template, request, url_for, session
from .models import check

app = Flask(__name__)
app.secret_key = 'asdasd'


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/forms/", methods=["GET", "POST"])
def forms():
    if request.method == 'GET':
        return render_template("forms.html")
    elif request.method == 'POST':
        if check(request.form['username'], request.form['pass']):
            flash('Gracias por ingresar')
            session["current_user"] = "Admin"
            return redirect(url_for('index'))
        else:
            error = 'Nope!'
    return render_template('forms.html', error=error)


@app.route("/logout/<user>")
def logout(user):
    session.pop("current_user", None)
    return redirect(url_for('index'))
