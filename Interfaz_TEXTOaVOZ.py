# Autor: Ian Bejenaru
# Fecha de creación: 30/11/2024
# Descripcion del código: en este código se crea una interfaz de usuario con la que se podrá interactuar
# para pedir conversiones de texto a voz.
#-------------------------------------------------------------------------------------------------------

# Importamos la librería para convertir texto a voz:
import pyttsx3

# Creamos la función que va a inicializar el audio:
def textoVoz(texto):
    # INPUT
    # texto: es el texto que se dirá por audio.
    # OUTPUT: El sonido del texto.

    # Inicializamos el convertidor de texto a voz:
    engine = pyttsx3.init()
    # Le decimos lo que queremos que convierta a voz:
    engine.say(texto)
    # Iniciamos el audio:
    engine.runAndWait()

# Creamos la función que nos va a permitir leer lineas de un TXT:
def leerLineasTXT(archivo):
        # INPUT
        # archivo: es el título del archivo que tenemos que leer.
        # OUTPUT: El texto línea por línea.

        # abrimos el archivo:
        try: # Manejamos el error en caso de que cambie de nombre o de lugar el TXT.
            book = open(archivo)
            # Leemos el archivo entero y lo guardamos en una variable:
            book_text= book.readlines()
            # Creamos un bucle for que recorrerá línea por línea lo que tenemos
            for line in book_text:
                # Llamamos a la función que nos va a permitir leer el texto
                textoVoz(line)
        except FileNotFoundError:
            print("El archivo no se encuentra")


# Creamos un menú en el que el usuario pueda decidir si quiere escribir un texto para que se lea o que pille el texto de un archivo .txt 
# variable que nos permite salir del bulce:
salir = True
while salir:
    opcion=input("Elige una opción que quieres convertir a texto:\n1) Escribir texto y convertir a voz\n2) Leer texto de un archivo txt\n3) Salir\n")

    # El usuario escribe por pantalla el texto que quiere leer:
    if opcion =="1":
        # Creamos una variable en la que el usuario va a escribir un texto que quiera ser leído:
        texto_usuario = input("Escribe un texto que quieres que se lea: ")
        # Llamamos a la función que nos va a permitir leer el texto
        textoVoz(texto_usuario)
    elif opcion == "2":
        # Pedimos al usuario que elija un archivo txt que quiere leer de su PC:
        leerLineasTXT("archivoPrueba.txt")
    elif opcion == "3":
        # Llamamos a la función que nos va a permitir leer el texto
        textoVoz("Saliendo del programa....")
        salir = False
    # Cuando se selecciona una opcion que no existe:
    else:
        print("La opcion seleccionada no existe, prueba otra vez")