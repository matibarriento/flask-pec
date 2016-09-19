from flask import Flask, render_template
from model import soy_un_mock

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/<int:times>")
def index_times(times):
    return render_template("times.html", times=times)


@app.route("/personajes/")
@app.route("/personajes/<int:take>")
def personajes(take=None):
    if not take:
        personajes = []
    elif take > 0:
        personajes = soy_un_mock[:take]
    else:
        personajes = soy_un_mock
    return render_template("personajes2.html", personajes=personajes)


if __name__ != "main":
    app.run("0.0.0.0", 5000, debug=True)
