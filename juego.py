import random as rd 

# Preguntas y respuestas para la trivia
preguntas = [
    {
        "pregunta": "¿Qué tecnología se utiliza en el fútbol para determinar si el balón cruzó la línea de gol?",
        "opciones": ["A) Hawk-Eye", "B) VAR", "C) Tecnología de línea de gol", "D) Ninguna de las anteriores"],
        "respuesta": "C"
    },
    {
        "pregunta": "¿Cuál es el nombre del sistema usado en el tenis para revisar si una pelota está dentro o fuera?",
        "opciones": ["A) VAR", "B) Hawk-Eye", "C) GoalRef", "D) TrackMan"],
        "respuesta": "B"
    },
    {
        "pregunta": "¿Qué dispositivo wearable se utiliza comúnmente para medir la frecuencia cardíaca de los atletas?",
        "opciones": ["A) Reloj inteligente", "B) Calzado inteligente", "C) Gafas inteligentes", "D) Sensor de impacto"],
        "respuesta": "A"
    },
    {
        "pregunta": "¿Qué deporte utiliza sensores GPS para monitorear la posición de los jugadores en tiempo real?",
        "opciones": ["A) Fútbol", "B) Baloncesto", "C) Tenis", "D) Natación"],
        "respuesta": "A"
    },
    {
        "pregunta": "¿Cómo se llama el sistema que ayuda a los árbitros a revisar decisiones controversiales en fútbol?",
        "opciones": ["A) Ojo de halcón", "B) VAR", "C) Chip en el balón", "D) Ninguna de las anteriores"],
        "respuesta": "B"
    },
    {
        "pregunta": "¿Qué tecnología se utiliza en los estadios inteligentes para mejorar la experiencia del espectador?",
        "opciones": ["A) Realidad aumentada", "B) Cámaras 360º", "C) Estadios con WiFi", "D) Todas las anteriores"],
        "respuesta": "D"
    },
    {
        "pregunta": "¿Qué tecnología se usa en las bicicletas profesionales para optimizar el rendimiento del ciclista?",
        "opciones": ["A) Frenos magnéticos", "B) Medidores de potencia", "C) GPS avanzado", "D) Cámaras térmicas"],
        "respuesta": "B"
    },
    {
        "pregunta": "¿Qué tipo de cámara se utiliza para estudiar el movimiento en detalle en deportes?",
        "opciones": ["A) Cámara lenta", "B) Cámara 360º", "C) Cámara de alta velocidad", "D) Cámara térmica"],
        "respuesta": "C"
    },
    {
        "pregunta": "¿Cómo ayudan los sensores en la ropa inteligente a los atletas?",
        "opciones": ["A) Miden la frecuencia cardíaca", "B) Detectan la postura", "C) Analizan el rendimiento físico", "D) Todas las anteriores"],
        "respuesta": "D"
    },
    {
        "pregunta": "¿Qué tecnología utiliza la natación para registrar los tiempos de los nadadores con precisión?",
        "opciones": ["A) Sensores de impacto en las paredes", "B) Cámaras subacuáticas", "C) Chips en las gorros", "D) Sensores en los trajes de baño"],
        "respuesta": "A"
    }
]

def elegir_jugador():
    player = input("Ingresar nombre: ")
    return player

def Bienvenido(player):
    print("¡Bienvenido a la Trivia sobre Tecnología en el Deporte!\n")
    print(f"Hola, {player}. Vamos a empezar la trivia. ¡Buena suerte!\n")

# Pregunta aleatoria
def obtener_pregunta_aleatoria(preguntas_hechas):
    pregunta = rd.choice(preguntas)
    while pregunta in preguntas_hechas:
        pregunta = rd.choice(preguntas)
    return pregunta

# Mostrar la pregunta y obtener la respuesta del usuario
def hacer_pregunta(pregunta):
    print(pregunta["pregunta"])
    for opcion in pregunta["opciones"]:
        print(opcion)
    respuesta_usuario = input("Ingrese su respuesta (A, B, C o D): ").upper()
    while respuesta_usuario not in ["A", "B", "C", "D"]:
        print("Elección inválida, elige una de las opciones mostradas.")
        respuesta_usuario = input("Ingrese su respuesta (A, B, C o D): ").upper()
    return respuesta_usuario

# Función para verificar si la respuesta es correcta
def verificar_respuesta(pregunta, respuesta_usuario):
    respuesta_correcta = pregunta["respuesta"]
    return respuesta_usuario == respuesta_correcta

# Función para mostrar el puntaje actualizado
def actualizar_puntaje(puntaje):
    print(f"Su puntaje actual es: {puntaje}")

# Generar secuencia Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Función para jugar el juego
def trivia():
    puntaje = 0
    preguntas_hechas = []
    player = elegir_jugador()
    Bienvenido(player)
    
    for i in range(1, 16):  # Jugar hasta 15 rondas o hasta que el jugador decida retirarse
        pregunta = obtener_pregunta_aleatoria(preguntas_hechas)
        preguntas_hechas.append(pregunta)
        respuesta_usuario = hacer_pregunta(pregunta)
                    
        if verificar_respuesta(pregunta, respuesta_usuario):
            puntaje += fibonacci(i)
            print(f"¡Correcto! Su puntaje es: {puntaje}")
        else:
            print(f"Incorrecto. La respuesta correcta era {pregunta['respuesta']}.")
            new_gamen = input("¿Quieres intentarlo de nuevo?").lower()
            if new_gamen == "si":
                trivia ()
            else:
                break
    
    if i == 10:
        print("¡Felicidades! Ha completado el juego. Su puntaje final es:", puntaje)

# Iniciar el juego
trivia()
