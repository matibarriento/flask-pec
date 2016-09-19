from flask import Blueprint, render_template

personaje = Blueprint("personaje", __name__,
                      template_folder='templates',
                      static_folder='static')


@personaje.route("/")
def index():
    return render_template("personajes/index.html")
