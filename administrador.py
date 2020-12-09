from particula import Particula
import json

# constructror
class Administrador:
    def __init__(self):
        # self. ==> atributo privado
        # [] ==> lista de elementos.
        self.__particulas = [] 

        # agregar al final.
    def agregar_final(self, particula:Particula): 
        # append ==> agregar lista en el final hasta agotar memoria.
        # append ==> agrega elementos nuevos al final del programa
        self.__particulas.append(particula)

    def agregar_inicio(self, particula:Particula):
        # insert ==> agregar elementos en el principio,
        # recibe dos parametros: posición de inicio "0", objeto "particula",
        # que queremos guardar en esa posición.
        # insert ==> recorre la posicion de los elementos para incluir la nueva particula
        # al inicio de nuestra lista
        self.__particulas.insert(0, particula)

    def mostrar(self):
        # inserta particulas en la posición nueva ingresada
        for particula in self.__particulas:
            # imprime los posiciones
            print(particula)

    def __str__(self):
        # presentar en pantalla
        # '\n' ==> salto de linea
        # for... ==> Repetir ciclo de posicion registrados
        # "" ==> string vacío
        # .join() ==> es un metodo que rebibe n cantidad de elementos para meter en el strings
        return "".join(
            str(particula) + '\n' for particula in self.__particulas)

    # metodo para obtener la cantidad de particulas introducidas
    def __len__(self):
        return len(self.__particulas)

    # itineración de los elementos del administrador
    def __iter__(self):
        self.cont = 0

        return self
    
    # impresion de particulas desde el administrador con el itinerador
    def __next__(self):
        if self.cont < len(self.__particulas):
            particula = self.__particulas[self.cont]
            self.cont += 1
            return particula
        else:
            # detener el ciclo al terminar la instruccion if anterior
            raise StopIteration

    # guardar ==> metodo que recibe la ubicación desde la interfaz grafica.
    def guardar(self, ubicacion):
        try:       
            # imprimir informacion en una archivo y no en la consola
            with open(ubicacion, 'w') as archivo:
                # guardar particulas en un ciclo
                lista = [particula.to_dict() for particula in self.__particulas]
                print(lista)
                # guardar archivo con formato json
                # indent=5 ==> formato de escritura del texto en json
                json.dump(lista, archivo, indent=5)
            return 1
        except:
            return 0
    
    def abrir(self, ubicacion):
        try:
            with open(ubicacion, 'r') as archivo:
                # json.load ==> metodo para extraer contenido del archivo
                lista = json.load(archivo)
                self.__particulas = [Particula(**particula) for particula in lista]
            return 1
        except:
            return 0

    def wheelEvent(self, event):
        if event.delta() > 0:
            self.ui.graphicsView.scale(1.2, 1.2)
        else:
            self.ui.graphicsView.scale(0.8, 0.8)
