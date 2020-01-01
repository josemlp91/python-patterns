"""
* ¿De que trata este patrón?

En Java y otros lenguajes, el "Patrón Factoría Abstracta", provee un interfaz 
para la creación de objetos relacionados/dependientes sin necesidad de 
especificar la clase actual.

La idea es abstraer la creación de objetos de la lógica de negocio, la plataforma 
elegida, etc.


En Python, el interfaz que nosotros usamos es simplemente un "callable", el cual es un interfaz
"builtin" en Python. En circunstancias normales nosotros podemos usar la propia clase como
"callable", puesto que en Python las clases en primera instancia, son clases de "object".

*¿Que hace este ejemplo?

Esta implementación particular abstrae la creación de una mascota dependiendo 
de la factoría seleccionada, teniendo disponibles (Perros, Gatos o Animales aleatorios)

Esto funciona dado que tanto Perro/Gato como "Animal Aleatorio", 
respetan una interfaz común de creación (llamable para creación y función .speak()).

Ahora my aplicación puede crear mascotas de forma abstracta y decidir su naturaleza después
basándose en mi propio criterio, perros o gatos. 


*¿Donde es usado este patrón de forma practica?

*Referencias:
https://sourcemaking.com/design_patterns/abstract_factory
http://ginstrom.com/scribbles/2007/10/08/design-patterns-python-style/

*TL;DR
Proporciona una forma de encapsular un grupo o una factoría. 
"""

import random


class PetShop:

    """Una tienda de mascotas"""

    def __init__(self, animal_factory=None):
        """pet_factory es nuestra factoría abstracta. Podemos configurarlo a voluntad."""

        self.pet_factory = animal_factory

    def show_pet(self):
        """Creamos y mostramos mascotas usando factorías abstractas"""

        pet = self.pet_factory()
        print("We have a lovely {}".format(pet))
        print("It says {}".format(pet.speak()))


class Dog:
    def speak(self):
        return "woof"

    def __str__(self):
        return "Dog"


class Cat:
    def speak(self):
        return "meow"

    def __str__(self):
        return "Cat"


# Factorías adicionales:

# Crea un animal aleatorio
def random_animal():
    """Puede ser dinámico!"""
    return random.choice([Dog, Cat])()


# Mostramos mascotas de varias factorías.
if __name__ == "__main__":

    # Una tienda que vende solo gatos.
    cat_shop = PetShop(Cat)
    cat_shop.show_pet()
    print("")

    # Una tienda que vende animales aleatorios.
    shop = PetShop(random_animal)
    for i in range(3):
        shop.show_pet()
        print("=" * 20)

### OUTPUT ###
# We have a lovely Cat
# It says meow
#
# We have a lovely Dog
# It says woof
# ====================
# We have a lovely Cat
# It says meow
# ====================
# We have a lovely Cat
# It says meow
# ====================
