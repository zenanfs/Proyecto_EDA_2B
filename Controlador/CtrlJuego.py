from Modelo.grafo import GrafoCuestionario, NodoPregunta
from Modelo.arbol import ArbolOpciones

class CtrlJuego:
    def __init__(self):
        self.grafo = GrafoCuestionario()
        self._iniciar_preguntas_espejo()

        self.p1_nodo_actual = None
        self.p2_nodo_actual = None

        self.p1_visitados = []
        self.p2_visitados = []

        #con esto se guardan diccionarios con el id de la pregunta y el tag de la respuesta
        self.p1_respuestas = {}
        self.p2_respuestas = {}

        self.juego_terminado = False

    def _iniciar_preguntas_espejo(self):
        #aqui se crean las preguntas espejadas y se aniaden al grafo

        #datos de preguntas: (id, texto_p1, texto_p2, opcion1_p1, etiqueta1_p1, opcion2_p1, etiqueta2_p1)
        datos = [
            (1, "¿Como recargas energia?", "¿Que buscas en tu pareja?",
             "Paz y soledad", "ESTABILIDAD", "Socializar y diversion", "ACCION"),

            (2, "Ante un cambio, tu...", "¿Prefieres a alguien que...",
             "Analice y planee", "ESTABILIDAD", "Se adapte rapido", "ACCION"),

            (3, "En el amor, priorizas...", "Para ti es esencial que...",
             "Seguridad y lealtad", "ESTABILIDAD", "Pasion y aventura", "ACCION"),

            (4, "Tu mayor fuerte es...", "Admiras a quien tiene...",
             "Logica y paciencia", "ESTABILIDAD", "Intuicion y rapidez", "ACCION"),

            (5, "En el dinero eres...", "Quieres que alguien sea...",
             "Previsor y ahorrador", "ESTABILIDAD", "Generoso y espontaneo", "ACCION"),

            # HOLA, AQUI FALTAN PONER 10 PREGUNTAS MAS, PARA QUE SEAN 15, PORFA AYUDEN CON ESO JASDJASHDKJA
        ]

        for pid, txt1, txt2, opA, tagA, opB, tagB in datos:
            arbol = ArbolOpciones(opA, tagA, opB, tagB)
            #se pasan ambos textos al nodo
            nodo = NodoPregunta(pid, txt1, txt2, arbol)
            self.grafo.aniadir_pregunta(nodo)
        self.grafo.conenctar_nodos()

    def iniciar_partida(self):

        self.p1_nodo_actual = self.grafo.obtener_pregunta_random(None, [])
        self.p2_nodo_actual = self.grafo.obtener_pregunta_random(None, [])

        if self.p1_nodo_actual: self.p1_visitados.append(self.p1_nodo_actual.id)
        if self.p2_nodo_actual: self.p2_visitados.append(self.p2_nodo_actual.id)

    def procesar_respuesta(self, jugador_id, opcion_escogida):
        if self.juego_terminado:
            return
        
        #se identifica el nodo actual
        nodo_actual = self.p1_nodo_actual if jugador_id == 1 else self.p2_nodo_actual
        if not nodo_actual: return

        #se obtienen respuestas
        op_izq, op_der = nodo_actual.arbol.obtener_opciones()
        #0 es izquierda (estabilidad), 1 es derecha (accion)
        respuesta_elegida = op_izq if opcion_escogida == 0 else op_der

        #se guarda la respuesta vinculada al id de la pregunta
        if jugador_id == 1:
            self.p1_respuestas[nodo_actual.id] = respuesta_elegida.etiqueta
        else:
            self.p2_respuestas[nodo_actual.id] = respuesta_elegida.etiqueta

        #finalmente, avanzar
        self._avanzar_jugador(jugador_id)

        if self.p1_nodo_actual is None and self.p2_nodo_actual is None:
            self.juego_terminado = True

    def _avanzar_jugador(self, jugador_id):
        if jugador_id == 1:
            nuevo = self.grafo.obtener_pregunta_random(
                self.p1_nodo_actual.id, self.p1_visitados)
            self.p1_nodo_actual = nuevo
            if nuevo: self.p1_visitados.append(nuevo.id)
        else:
            nuevo = self.grafo.obtener_pregunta_random(
                self.p2_nodo_actual.id, self.p2_visitados)
            self.p2_nodo_actual = nuevo
            if nuevo: self.p2_visitados.append(nuevo.id)

    def calcular_resultado(self):
        #si estan en el mismo nodo, son almas gemelas
        #si estan en el mismo lado, tienen gran sintonia
        #si estan en lados opuestos, son polos opuestos valga la redundancia jeje

        coincidencias = 0
        total_preguntas = len(self.p1_respuestas)

        if total_preguntas == 0: return ("No se respondieron preguntas", 0)

        #se compara pregunta por pregunta usando los ids
        for pid in self.p1_respuestas:
            if pid in self.p2_respuestas:
                tag_p1 = self.p1_respuestas[pid]
                tag_p2 = self.p2_respuestas[pid]

                #si ambos eligieron la misma etiqueta es match
                if tag_p1 == tag_p2:
                    coincidencias += 1

        #logica de rangos segun lo respondido
        if coincidencias == total_preguntas: #es decir, tienen todo igual
            return ("Almas Gemelas", 100)
        elif coincidencias >= total_preguntas / 2: #mayoria de respuestas iguales
            return ("Gran Sintonia", 70)
        else: #menos de la mitad igual
            return ("Polos Opuestos", 20)