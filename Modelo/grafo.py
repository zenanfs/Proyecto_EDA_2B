'''
Aqui estan las preguntas, cada nodo del grafo tiene el texto de la pregunta y contiene un
arbol de respuestas. Esta orientado para que dos personas jueguen al mismo tiempo
'''

import random

class NodoPregunta:
    def __init__(self, id_pregunta, texto_pregunta, arbol_respuestas):
        self.id = id_pregunta
        self.texto_p1 = texto_p1
        self.texto_p2 = texto_p2
        self.arbol = arbol_respuestas
        
class GrafoCuestionario:
    def __init__(self):
        #se usa un diccionario para acceder a la info de la pregunta por su id
        self.nodos = {}
        
        #este es el mapa de conexiones. Se hace una lista de adyacencia, que permite que desde
        #la pregunta 1 pueda saltar a la pregunta 2, 3, o 4 y asi sucesivamente
        self.adyacencia = {}
        
        def aniadir_pregunta(self, nodo_pregunta):
            
            #este recibe un objeto NodoPregunta y lo aniade al grafo
            p_id = nodo_pregunta.id
            self.nodos[p_id] = nodo_pregunta
            
            #se inicializa su lista de adyacencia en primera instancia vacia
            if p_id not in self.adyacencia:
                self.adyacencia[p_id] = []
                
        def conenctar_nodos(self):
            
            #conecta todos con todos, justificando los saltos de una pregunta a otra
            ids = list(self.nodos.keys())
            for id_inicio in ids:
                for id_destino in ids:
                    if id_inicio != id_destino:
                        self.adyacencia[id_inicio].append(id_destino)
               
        def obtener_pregunta_random(self, id_actual, visitados):
            
            #se obtiene una pregunta random basada en las conexiones del grafo
            #el id_actual corresponed a la pregunta en la que se encuentra, o None si empieza el juego
            #visitados es la lista de ids que ya se respondio
            
            if id_actual is None:
                disponibles = [pid for pid in self.nodos if pid not in visitados]
                
            else:
                cercanos = self.adyacencia.get(id_actual, [])
                disponibles = [pid for pid in cercanos if pid not in visitados]
                
            if not disponibles:
                return None #el juego se termino
                
            #se eligen de manera aleatoria los caminos disponibles
            siguiente_id = random.choice(disponibles)
            return self.nodos[siguiente_id]