import math

# formula de la distancia entre dos puntos cartesianos
def distancia_euclidiana(origenx, origeny, destinox, destinoy):
    dist = math.sqrt((destinox-origenx)**2+(destinoy-origeny)**2)
    return dist
    