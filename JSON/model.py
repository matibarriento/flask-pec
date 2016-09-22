class Personaje():
    """docstring for Personaje"""

    def __init__(self, nombre, pelicula, virtud):

        self.nombre = nombre
        self.pelicula = pelicula
        self.virtud = virtud


chuck = Personaje("Chuck Norris",
                  "The Delta Force",
                  "Roundhouse Kick")
bat = Personaje("Batman",
                "Batman",
                "Ser Batman")
spider = Personaje("Spiderman",
                   "The Amazing Spiderman",
                   "Un gran poder lleva a que nos rebooteen las peliculas")

soy_otro_mock = [chuck, bat, spider]
