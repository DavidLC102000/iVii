import datetime
import time

def saludar():
    print("Hola, usuario.")

def estado():
    print("Estoy bien, Usuario.")

def recibirNombre():
    nombre = input("Vale, dímelo: ")

def darFecha():
    fecha = datetime.date.today()
    print("Estamos a: ", fecha.strftime("%d/%m/%Y"))

def darHora():
    print("Son las: ", time.strftime("%X"))

def darEdad():
    print("Tengo 21 años.")

def darNombre():
    print("Me llamo iVii.")

def despedirse():
    print("Adios, Usuario.")
    return True

def sumar(numero1, numero2):
    total = numero1 + numero2
    print("El resultado es: ", total)

def restar(numero1, numero2):
    total = numero1 - numero2
    print("El resultado es: ", total)

def multiplicar(numero1, numero2):
    total = numero1 * numero2
    print("El resultado es: ", total)

def dividir(numero1, numero2):
    total = numero1 / numero2
    print("El resultado es: ", total)