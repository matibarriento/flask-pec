from flask import Blueprint, render_template

pelicula = Blueprint("pelicula", __name__,
                     template_folder='templates',
                     static_folder='static')


@pelicula.route("/")
def index():
    return render_template("peliculas/index.html")
