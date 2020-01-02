"""
* ¿De que trata este patrón?

El patrón Borg (también conocido como patrón Mono-estado) es la forma de
comportamiento único, pero en vez de tener solo una instancia de una clase,
existen múltiples instancias que comparten el mismo estado. 

En otras palabras, se centra en compartir el estado en vez de compartir 
la identidad.


*¿Que hace este ejemplo?

Para entender la implementación de este patrón en Python, es importante
conocer que los atributos de una instancia son almacenados en un diccionario
llamado __dict__. Normalmente, cada instancia tiene su propio diccionario, pero
en el patrón "Borg", cuando lo modificamos, los cambios afectan a todas las
instancias que tienen el mismo diccionario.

En el ejemplo, el atributo __shared_state es un diccionario compartido
por todas las instancias, y esto es asegurado por la asignación de 
__shared_state a __dict__ cuando inicializamos una nueva instancia. 
(ej, en el método _init_)


*¿Donde es usado este patrón de forma practica?

Compartir estados es útil en aplicaciones como por ejemplo cuando gestionamos 
una conexión a una base de datos:

https://github.com/onetwopunch/pythonDbTemplate/blob/master/database.py

*Referencias:
https://fkromer.github.io/python-pattern-references/design/#singleton

*TL;DR
Asegura comportamiento único entre instancias de una misma clase, compartiendo el estado.
"""


class Borg:
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
        self.state = 'Init'

    def __str__(self):
        return self.state


class YourBorg(Borg):
    pass


def main():
    """
    >>> rm1 = Borg()
    >>> rm2 = Borg()

    >>> rm1.state = 'Idle'
    >>> rm2.state = 'Running'

    >>> print('rm1: {0}'.format(rm1))
    rm1: Running
    >>> print('rm2: {0}'.format(rm2))
    rm2: Running

    # When the `state` attribute is modified from instance `rm2`,
    # the value of `state` in instance `rm1` also changes
    >>> rm2.state = 'Zombie'

    >>> print('rm1: {0}'.format(rm1))
    rm1: Zombie
    >>> print('rm2: {0}'.format(rm2))
    rm2: Zombie

    # Even though `rm1` and `rm2` share attributes, the instances are not the same
    >>> rm1 is rm2
    False

    # Shared state is also modified from a subclass instance `rm3`
    >>> rm3 = YourBorg()

    >>> print('rm1: {0}'.format(rm1))
    rm1: Init
    >>> print('rm2: {0}'.format(rm2))
    rm2: Init
    >>> print('rm3: {0}'.format(rm3))
    rm3: Init
    """


if __name__ == "__main__":
    import doctest
    doctest.testmod()
