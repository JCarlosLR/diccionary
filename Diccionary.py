import random
import string
from difflib import get_close_matches
import os,pyfiglet
from colorama import Fore,Style

palabras = []

ban = """ (                                           
 )\ )           )                            
(()/( (      ( /((               ) (   (     
 /(_)))\  (  )\())\  (   (    ( /( )(  )\ )  
(_))_((_) )\(_))((_) )\  )\ ) )(_)|()\(()/(  
 |   \(_)((_) |_ (_)((_)_(_/(((_)_ ((_))(_)) 
 | |) | / _||  _|| / _ \ ' \)) _` | '_| || | 
 |___/|_\__| \__||_\___/_||_|\__,_|_|  \_, | 
                                       |__/ """

all_col= [Style.BRIGHT+Fore.RED,Style.BRIGHT+Fore.CYAN,Style.BRIGHT+Fore.LIGHTCYAN_EX, Style.BRIGHT+Fore.LIGHTBLUE_EX, Style.BRIGHT+Fore.LIGHTCYAN_EX,Style.BRIGHT+Fore.LIGHTMAGENTA_EX,Style.BRIGHT+Fore.LIGHTYELLOW_EX]

ran = random.choice(all_col)
print(ran,ban)
print(ran + "\n\t\tPOR SENATINOS\t\n\n")

print("\n" , "*" * 63)

while True:
    print(Style.BRIGHT+Fore.LIGHTCYAN_EX, "Selecciona una opción:")
    print(Style.BRIGHT+Fore.LIGHTCYAN_EX,"1. Ingresar una palabra nueva")
    print(Style.BRIGHT+Fore.LIGHTCYAN_EX,"2. Guardar las palabras en un archivo de texto")
    print(Style.BRIGHT+Fore.LIGHTCYAN_EX,"3. Salir")

    opcion = input(ran + "Ingresa el número de la opción: ")

    if opcion == "1":
        nueva_palabra = input(ran +"Ingresa una palabra nueva: ")
        palabras.append(nueva_palabra)
        for _ in range(1000):
            combinacion = nueva_palabra + "".join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, 10)))
            palabras.append(combinacion)

        print(ran + "La palabra se ha guardado en la lista.")

    elif opcion == "2":
        nombre_archivo = input(ran + "Ingresa el nombre del archivo de texto (sin .txt): ")
        with open(f"{nombre_archivo}.txt", "w") as archivo:
            for palabra in palabras:
                archivo.write(palabra + "\n")
            archivo.write("66202028")
        print(ran + f"Las palabras se han guardado en el archivo '{nombre_archivo}.txt'.")

    elif opcion == "3":
        print(ran + "¡Hasta luego!")
        break

    else:
        print(ran + "Opción inválida. Intenta de nuevo.")
