from algoritmos import distancia_euclidiana

class Particula:
    def __init__(self, identificador=0, origenx=0 , origeny=0, destinox=0, destinoy=0, velocidad=0, red=0, green=0, blue=0):
        self.__id = identificador
        self.__origen_x = origenx
        self.__origen_y = origeny
        self.__destino_x = destinox
        self.__destino_y = destinoy
        self.__velocidad = velocidad
        self.__red = red
        self.__green = green
        self.__blue = blue
        self.__distancia = distancia_euclidiana(origenx, origeny, destinox, destinoy)
    
    # converitir objeto particula a String(cadena)
    def __str__(self):
        return (
            'ID: ' + str(self.__id)+'\n' +
            'Origen en x: ' + str(self.__origen_x) +'\n' +
            'Origen en y: ' + str(self.__origen_y) +'\n' +
            'Destino en x: ' + str(self.__destino_x) +'\n' +
            'Destino en y: ' + str(self.__destino_y) +'\n' +
            'Velocidad: ' + str(self.__velocidad) +'\n' +
            'Red: ' + str(self.__red) +'\n' +
            'Green: ' + str(self.__green) +'\n' +
            'Blue: ' + str(self.__blue) +'\n' +
            'Distancia: ' + str(self.__distancia) +'\n'
        )
    
    # metodos de acceso a los elementos de la particula
    # @property ==> decorador para el metodo
    # aquí generamos los widget para obtener la informacion
    @property
    def identificador(self):
        return self.__id

    @property
    def origenx(self):
        return self.__origen_x
    
    @property
    def origeny(self):
        return self.__origen_y

    @property
    def destinox(self):
        return self.__destino_x

    @property
    def destinoy(self):
        return self.__destino_y

    @property
    def velocidad(self):
        return self.__velocidad

    @property
    def red(self):
        return self.__red

    @property
    def green(self):
        return self.__green

    @property
    def blue(self):
        return self.__blue

    @property
    def distancia(self):
        return self.__distancia

    # to_dict ==> metodo para convertir nuestra particula a un 
    # diccionario mediante llaves tomadas de class Particula
    def to_dict(self):
        return {
            "identificador": self.__id,
            "origenx": self.__origen_x,
            "origeny": self.__origen_y,
            "destinox": self.__destino_x,
            "destinoy": self.__destino_y,
            "velocidad": self.__velocidad,
            "red": self.__red,
            "green": self.__green,
            "blue": self.__blue
        }
