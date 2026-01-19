'''
Estructura de las respuestas, cada pregunta tiene asociado un arbol binario que contiene
las opciones de respuesta. La raiz es un nodo conector y sus hijos las respuestas tangibles
'''

class NodoRespuesta:
    def __init__(self, texto, etiqueta):
        self.texto = texto
        self.etiqueta = etiqueta
        self.izquierda = None
        self.derecha = None
        
'''
Este arbol contiene las respuestas, la raiz es un nodo neutro, o sea, el punto de decision,
el hijo izquierdo es la opcion uno y el hijo derecho es la opciones dos
'''
        
class ArbolOpciones:
    def __init__(self, opcionUno, etiquetaUno, opcionDos, etiquetaDos):
        self.raiz = NodoRespuesta("Punto de Decision", None)
        
        #se asignan las respuestas a las ramas
        self.raiz.izquierda = NodoRespuesta(opcionUno, etiquetaUno)
        self.raiz.derecha = NodoRespuesta(opcionDos, etiquetaDos)
        
def obtener_opciones(self):
    #basicamente retorna las opciones en forma de tupla
    return (self.raiz.izquierda, self.raiz.derecha)