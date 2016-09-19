from flask import Flask
from personajes.personaje import personaje
from peliculas.pelicula import pelicula


app = Flask(__name__)
app.register_blueprint(personaje, url_prefix="/personaje")
app.register_blueprint(pelicula, url_prefix="/pelicula")

if __name__ != "main":
    print(app.url_map)
    app.run("0.0.0.0", 5000, debug=True)
