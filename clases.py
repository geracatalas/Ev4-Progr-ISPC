# clases.py
import math

# Esta clase representa a un arco de una forma simple y clara para poder interacturar sin necesidad de conocer a fondo todos los detalles de como se realizan los calculos
class Arco:
    # la clase Arco aplica los principios de abstracción al ofrecer una interfaz sencilla y oculta los detalles complejos de las operaciones internas. A su vez, utiliza encapsulamiento para proteger el estado interno del objeto, permitiendo que los usuarios interactúen con la clase de una manera controlada y segura
    
    def __init__(self, fuerza_tiro, angulo):
        # Inicializa el arco con la fuerza de tiro y el ángulo.
        self.fuerza_tiro = fuerza_tiro  # Fuerza en newtons
        self.angulo = angulo  # Ángulo en grados

    def tirar(self):
        # Calcula la distancia que recorrerá la flecha según la fuerza y el ángulo.
        # Los detalles de la fórmula matemática se encapsulan dentro del método, lo que permite a otros desarrolladores o usuarios llamar a tirar sin entender cómo se calcula la distancia
        radianes = math.radians(self.angulo)
        distancia = (self.fuerza_tiro ** 2) * math.sin(2 * radianes) / 9.81  # Fórmula simplificada, sería ((velocidad o fuerza)^2 * sen(2 * radianes) / gravedad)
        return distancia

    def ajustar(self, nueva_fuerza, nuevo_angulo):
        # Ajusta la fuerza de tiro y el ángulo del arco.
        self.fuerza_tiro = nueva_fuerza
        self.angulo = nuevo_angulo

    def calcular_puntaje(self, distancia_objetivo):
        # Calcula el puntaje basado en la distancia de la flecha al objetivo.
        distancia_flecha = self.tirar()
        diferencia = abs(distancia_flecha - distancia_objetivo)
        if diferencia <= 5:
            return 10
        elif diferencia <= 15: # Estos numeros serían en metros, si la flecha cae en una distancia de 6 a 15 metros, suma 7 puntos al jugador
            return 7
        elif diferencia <= 25:
            return 5
        else:
            return 0

    def __str__(self):
        # Este método proporciona una forma de visualizar el objeto sin exponer directamente sus atributos.
        # Devuelve una representación en cadena del estado del arco.
        return f"Arco con fuerza de {self.fuerza_tiro}N y ángulo de {self.angulo} grados"


# Código principal para demostrar que funciona
if __name__ == "__main__":
    # Crea una instancia de Arco
    arco = Arco(fuerza_tiro=50, angulo=45)

    # Muestra el estado inicial del arco
    print(arco)

    # Realiza un tiro y muestra la distancia
    # El .2f es para que el numero mostrado sea flotante y con 2 decimales
    distancia = arco.tirar()
    print(f"Distancia de la flecha: {distancia:.2f} metros")

    # Ajusta los parámetros del arco
    arco.ajustar(nueva_fuerza=35, nuevo_angulo=30)
    print("Después de ajustar el arco:")
    print(arco)

    # Realiza otro tiro con los nuevos parámetros
    nueva_distancia = arco.tirar()
    print(f"Nueva distancia de la flecha: {nueva_distancia:.2f} metros")

    # Calcula puntaje basado en la distancia objetivo
    puntaje = arco.calcular_puntaje(distancia_objetivo=100)
    # La distancia al objetivo en este caso es 100 y la flecha cae a 108.14m, lo que equivale a obtener 7 puntos
    print(f"Puntaje obtenido: {puntaje}")