def analizadorSintaxis(orden):
    if orden == 1:
        respuesta = input("Hola, soy tu asistente iVii, ¿qué desea hacer?: ")
    else:
        respuesta = input("¿Qué desea hacer?: ")

    respuesta = respuesta.lower()

    if "cómo" in respuesta or "cuál" in respuesta or "qué" in respuesta:
        tipo = "pregunta"
    else:
        tipo = "normal"


    if "no " in respuesta:
        modo = "no"

    elif "hola" in respuesta:
        modo = "saludar"

    elif "estás" in respuesta:
        modo = "estado"

    elif "nombre" in respuesta or "llamas" in respuesta:
        if tipo == "pregunta":
            modo = "dar_nombre"
        else:
            modo = "recibir_nombre"

    elif "fecha" in respuesta or "dia" in respuesta:
        modo = "fecha"

    elif "hora" in respuesta:
        modo = "hora"

    elif "edad" in respuesta or "años" in respuesta:
        modo = "edad"

    elif "adios" in respuesta or "hasta luego" in respuesta or "apágate" in respuesta or "salir" in respuesta\
          or "hasta mañana" in respuesta:
        modo = "despedirse"

    elif "+" in respuesta or "suma" in respuesta:
        numeros = respuesta.split(" ")
        if numeros[0].isdigit() and numeros[2].isdigit():
            modo = ["suma", int(numeros[0]), int(numeros[2])]
        else:
            modo = "fallo"

    elif "-" in respuesta or "resta" in respuesta:
        numeros = respuesta.split(" ")
        if numeros[0].isdigit() and numeros[2].isdigit():
            modo = ["resta", int(numeros[0]), int(numeros[2])]
        else:
            modo = "fallo"
    
    elif "*" in respuesta or "por" in respuesta:
        numeros = respuesta.split(" ")
        if numeros[0].isdigit() and numeros[2].isdigit():
            modo = ["multiplicación", int(numeros[0]), int(numeros[2])]
        else:
            modo = "fallo"

    elif "/" in respuesta or "divide" in respuesta or ":" in respuesta:
        numeros = respuesta.split(" ")
        if numeros[0].isdigit() and numeros[2].isdigit():
            modo = ["división", int(numeros[0]), int(numeros[2])]
        else:
            modo = "fallo"
            
    else:
        modo = "desconocido"

    return modo