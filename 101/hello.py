from flask import Flask
app = Flask(__name__)


@app.route("/")
def index():
    i = 1
    return "<h1>Hello World</h1>"


if __name__ != "main":
    app.run("0.0.0.0", 5000, True)
