import json
from flask import Flask, jsonify
from model import soy_otro_mock
app = Flask(__name__)


def obj_dict(obj):
    return obj.__dict__


@app.route("/")
@app.route("/<name>")
def index(name=None):
    message = "Hello {0}".format(name) if name else "Hello World"
    return jsonify(message=message)


@app.route("/cuadrado/<int:num>")
def cuadrado(num):
    return jsonify(result=num ** 2)


@app.route("/personajes/")
@app.route("/personajes/<int:take>")
def personajes(take=None):
    if not take:
        personajes = []
    elif take > 0:
        personajes = soy_otro_mock[:take]
    else:
        personajes = soy_otro_mock
    return json.dumps(personajes, default=obj_dict)


if __name__ != "main":
    app.run("0.0.0.0", 5000, debug=True)
