# Autor: Ian Bejenaru
# Fecha de creación: 30/11/2024
# Descripcion del código: en este código se crea una interfaz de usuario con la que se podrá interactuar
# para pedir conversiones de texto a voz.
#-------------------------------------------------------------------------------------------------------

# Importamos la librería para convertir texto a voz:
import pyttsx3
# Importamos la librería para crear una interfaz, poder cargar archivos abriendo el explorador de archivos y mostrar mensajes por pantalla:
import tkinter as tk
from tkinter import filedialog, messagebox

# FUNCIONES

def textoVoz(texto):
    """
    Convierte un texto dado en audio utilizando la biblioteca pyttsx3.

    INPUT:
        texto (str): El texto que será convertido en audio.

    OUTPUT:
        El audio se reproduce directamente, no se retorna ningún valor.
    """
    # Inicializamos el convertidor de texto a voz:
    engine = pyttsx3.init()
    # Le decimos lo que queremos que convierta a voz:
    engine.say(texto)
    # Iniciamos el audio:
    engine.runAndWait()


def execute_code():
    """
    Funcion que se ejecutará al presionar el primer botón 'LEER TEXTO ESCRITO'.
    Se encargará de leer el contenido que esta escrito en el cuadro de escritura.

    INPUT:
        Guardará el contenido del cuadro de escritura en una variable.

    OUTPUT:
        Reproducirá el texto escrito en forma de audio, no se retorna ningún valor.
    """
    input_text = text_area.get("1.0", tk.END).strip()  # Obtener texto del área
    # Si el area de texto existe, llamamos a la funcion textoaVoz() sino mostramos un mensaje de que no está rellenado el área.
    if input_text:
        # Llamamos a la función que nos va a permitir leer el texto
        textoVoz(input_text)
        # Aquí puedes agregar la lógica que deseas ejecutar
    else:
        messagebox.showwarning("Advertencia", "Por favor, escribe algo antes de ejecutar.")


def open_file():
    """
    Funcion que se ejecutará al presionar el botón 'LEER TEXTO DE UN ARCHIVO'
    y que se encargará de guardar la ruta de un archivo txt que quiera ser leido.

    INPUT:
        Guardará la ruta del archivo que se seleccione en una variable.

    OUTPUT:
        Llamará a la función leerLineasTXT si la ruta es correcta y
        si la ruta es incorrecta, mostrará un mensaje de advertencia.
    """
    # Abrir el explorador de archivos para seleccionar un archivo
    file_path = filedialog.askopenfilename(
        title="Seleccionar un archivo",
        filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*"))
    )
    if file_path:
        leerLineasTXT(file_path)
    else:
        messagebox.showwarning("Sin Selección", "No seleccionaste ningún archivo.")


# Creamos la función que nos va a permitir leer lineas de un TXT:
def leerLineasTXT(archivo):
    """
    Leerá las líneas que tiene un archivo txt. En caso de que el archivo no se encuentre saltará una excepción avisando al usuario.

    INPUT:
        archivo (str): Ruta del archivo txt que será convertido en audio.

    OUTPUT:
        El audio se reproduce línea por línea, no se retorna ningún valor.
    """
    # abrimos el archivo:
    try: # Manejamos el error en caso de que cambie de nombre o de lugar el TXT.
        book = open(archivo)
        # Leemos el archivo entero y lo guardamos en una variable:
        book_text= book.readlines()
        # Creamos un bucle for que recorrerá línea por línea lo que tenemos
        for line in book_text:
            # Llamamos a la función que nos va a permitir leer el texto
            textoVoz(line)
    except FileNotFoundError: # Si el archivo no se encuentra, saltará esta advertencia
        messagebox.showwarning("Advertencia", "El archivo no se encuentra")
    except UnicodeDecodeError: # Si el archivo no es un txt, saltará esta advertencia
        messagebox.showwarning("Advertencia", "El archivo no es un .txt")


# Función que se activará cuando se cierre la ventana de la interfaz:
def on_close():
    """
    Al presionarse la X para cerrar el programa, activará un audio para indicar que salimos del programa.

    INPUT:
        Presionar la X para cerrar el programa.

    OUTPUT:
        Reproducirá un audio indicando el cierre del programa.
    """
    textoVoz("Saliendo del programa....")
    root.destroy()  # Cerrar la ventana


# CREAR VENTANA PRINCIPAL
root = tk.Tk()
root.title("Interfaz de Texto") # Título de la ventana
root.geometry("400x260")  # Tamaño de la ventana
root.resizable(False, False)  # Desactivar redimensionado
# Conectar el evento de cierre a la función on_close
root.protocol("WM_DELETE_WINDOW", on_close)

# CREAR WIDGETS
# Area de texto en el que se podrá escribir:
text_area = tk.Text(root, wrap="word", height=5, font=("Arial", 12), borderwidth=2, relief="groove")
# Diseño del primer botón, que nos permitirá leer lo que se ha escrito:
execute_button = tk.Button(root, text="LEER TEXTO ESCRITO", command=execute_code, bg="#4caf50", fg="white", font=("Arial", 12), relief="raised")
# Diseño del segundo botón, que nos permitirá leer lo que se ha escrito en un txt:
button_two = tk.Button(root, text="LEER TEXTO DE UN ARCHIVO", command=open_file, bg="#2196f3", fg="white", font=("Arial", 12), relief="raised")

# ORGANIZAR WIDGETS EN LA VENTANA:
text_area.pack(pady=20, padx=20, fill="x")
execute_button.pack(pady=10, fill="x", padx=50)
button_two.pack(pady=5, fill="x", padx=50)

# Iniciar el bucle principal de la aplicación
root.mainloop()
