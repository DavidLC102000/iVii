import acciones
import analizadorSintaxis

def procesarRespuesta():
    salir = False
    orden = 1

    while(salir == False):
        modo = analizadorSintaxis.analizadorSintaxis(orden)

        if modo == "no":
            print("Vale, Usuario, no lo haré")
            
        elif modo == "saludar":
            acciones.saludar()

        elif modo == "estado":
            acciones.estado()
            
        elif modo == "dar_nombre":
            acciones.darNombre()
            
        elif modo == "recibir_nombre":
            acciones.recibirNombre()
            
        elif modo == "fecha":
            acciones.darFecha()
            
        elif modo == "hora":
            acciones.darHora()
            
        elif modo == "edad":
            acciones.darEdad()
            
        elif modo == "despedirse":
            salir = acciones.despedirse()
            
        elif modo == "fallo":
            print("Introduce un número correcto")
            
        elif modo[0] == "suma":
            acciones.sumar(modo[1], modo[2])
            
        elif modo[0] == "resta":
            acciones.restar(modo[1], modo[2])
            
        elif modo[0] == "multiplicación":
            acciones.multiplicar(modo[1], modo[2])
            
        elif modo[0] == "división":
            acciones.dividir(modo[1], modo[2])
            
        else:
            print("No entiendo lo que has dicho, Usuario. ¿Podrías repetirlo?")

        orden = 2
