from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/<name>")
def index(name=None):
    if(name):
        return "Hello {0}".format(name)
    return "Hello World"


@app.route("/cuadrado/<int:num>")
def cuadrado(num):
    return str(num ** 2)


if __name__ != "main":
    app.run("0.0.0.0", 5000, debug=True)
