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


# @app.route("/cuadrado/<int:num>")
# def cubo(num):
#     return str(num ** 3)

@app.errorhandler(500)
def internal_error(error):

    return "500 error, se pudrió todo"


@app.errorhandler(404)
def not_found(error):
    return "404 error, no existo", 404


@app.route("/dividecero")
def divide_cero():
    return str(1 / 0)


if __name__ != "main":
    app.run("0.0.0.0", 5000, debug=True)
