import random
import os
import time

def reglas_del_juegos(): #mostrara las reglas a traves de salidas de texto
    os.system("cls")
    print("[1] Tienes cierta cantidad de oportunidades para adivinar la palabra")
    print("[2] Puedes ingresar cualquier dijito. si no corresponde se te restara un intento")
    print("[3] puede utilizar el caracter '#' cerrar (menos en elegir nivel).")
    enter_continuar = input("Enter para continuar")

def lista_de_palabras():
    palabras = ["python","desarrollo","programacion","computadora","tecnologia"]
    return random.choice(palabras) #Se elegira una palabra aleatoria de la lista de palabras

def Estado_del_juego(palabra_O, palabras_false, intentos_r): #cargara el estado actual del juego
    print("palabra : ", palabra_O)
    print("Letras inscorrectas : ", palabras_false)
    print(f"Intentos restantes : {intentos_r}")

def cargar_juego_guardado(archivo_guardado = "juego_ahorcado_guardado.txt"):
    palabra_oculta = ""
    num_intentos = 0
    palabra_escondida_guardada = []
    letras_incorrectas_guardada = []

    try:
        with open(archivo_guardado, 'r') as archivo: #se abrira el archivo donde se han guardado los datos del juego y se obtendran los datos en las variables
            palabra_oculta = archivo.readline().strip()
            num_intentos = archivo.readline().strip()
            palabra_escondida_guardada = archivo.readline().strip().split(',')
            letras_incorrectas_guardada = archivo.readline().strip().split(',')

        Juego_del_ahorcado(palabra_oculta, palabra_escondida_guardada, letras_incorrectas_guardada, int(num_intentos)) #se cargara el juego con los datos guardados

    except:
        print("Hubo un error al cargar los datos del juego")

def menu_guardar_juego(palabra_escondida ,intentos_restantes, datos_juego,letras_incorrectas, nombre_archivo = "juego_ahorcado_guardado.txt"):
    while True:
        os.system("cls")
        print("""\n¿Desea guardar el juego antes de salir?
[S] si
[N] no""")
        opcion_guardar = input("Ingresar opcion : ").upper()

        if opcion_guardar == "S":
            try:
                with open (nombre_archivo, 'w') as archivo:#se creara un archivo de texto en el que se van a guardar los datos del juego
                    archivo.write(palabra_escondida + "\n")#guardara la palabra escodida
                    archivo.write(str(intentos_restantes) + "\n")#guardara los intentos restanes
                    archivo.write(','.join(datos_juego)+"\n")#guarada la lista con las letras ya encontradas
                    archivo.write(','.join(letras_incorrectas)+"\n")#guardara la lista de palabras incorrectas
                
                print("El juego se ha guardado correctamente")

            except:
                print("Hubo un error al guardar el juego") #en caso de haber error al guardar los datos se mandara un mensaje 

            time.sleep(2)#congelara el programa durante 2 segundos para que se pueda leer el mensaje
            break

        elif opcion_guardar == "N":
            print("Saliendo del juego")
            time.sleep(2)
            break
        else:
            print("Elegir entre [S/N]")
            time.sleep(1)

def Juego_del_ahorcado(palabra_ADI, palabra_OCUL, letras_INCORRECT, Intentos):
    print("\nPuedes adivinar la palabra")
    palabra_adivinar = palabra_ADI #palabra que se tiene que adivinar
    palabra_oculta = palabra_OCUL #Lista de letras ocultas que forman la palabra
    letras_incorrectas = letras_INCORRECT #Lista con las letras incorrectas
    intentos = Intentos #Intentos restantes
    
    while intentos > 0 and "_" in palabra_oculta: #el bucle se realizara mientras que los intentos sean mayores que 0 y ademas no exista el caracter de '_' en la palabra oculta
        os.system("cls")
        Estado_del_juego(palabra_oculta, letras_incorrectas, intentos)#metodo que cargara el estado del juego
        letra_adivinar = input("Adivina una letra : ")

        if letra_adivinar == "#":#si se utiliza el caracter de '#' se activara el metodo para guardar los datos del juego
            menu_guardar_juego(palabra_adivinar, intentos, palabra_oculta, letras_incorrectas)
            break#el programa finalizara

        for ubicacion, letra in enumerate(palabra_adivinar):#se agregara la letra ingresada por el usuario si esta existe en la palabra oculta
            if letra_adivinar in letra:
                palabra_oculta[ubicacion] = letra_adivinar

        if letra_adivinar not in palabra_oculta: #se ingresara si la letra ingresada por el usuario no existe en la palabra oculta  
            if letra_adivinar not in letras_incorrectas:#se ingresara si la palabra ingresada por el usuario no existe en la lista de letras incorrectas
                letras_incorrectas.append(letra_adivinar)
                intentos -= 1 #los intentos disminuiran
            else:
                print("Esa letra ya se ha ingresado")
                time.sleep(1)

    #se mandara un mensaje segun sea la razon por la que finalizo el juego
    if "_" not in palabra_oculta:
        print(f"Felicidades has logrado adivinar la palabra : {palabra_adivinar}")
        time.sleep(3)
    elif intentos == 0:
        print(f"Has perdido la palabra oculta era : {palabra_adivinar}")
        time.sleep(3)

def nivel_de_dificultad():
    os.system("cls")
    intentos_juego = 0
    while True:
        print("""Elegir un nivel de dificultad
[1] Facil
[2] Normal
[3] Dificil""")
        opcion_nivel  = input("Seleccionar un nivel de dificultad : ")
        if opcion_nivel == "1":
            intentos_juego = 6
            return intentos_juego
        elif opcion_nivel == "2":
            intentos_juego = 4
            return intentos_juego
        elif opcion_nivel == "3":
            intentos_juego = 2
            return intentos_juego
        else:
            print("Opcion no disponible")
            time.sleep(1)

def menu_del_juego():
    while True:
        os.system("cls")
        print("""\nBienvenido al juego del ahorcado
[1] Iniciar juego
[2] Cargar juego guardado
[#] Cerrar juego""")
    
        opcion_menu = input("Ingresar opcion : ")
        if opcion_menu == "1":
            palabra_adivinar = lista_de_palabras() #el metodo retornara una palabra de la lista para adivinar
            palabra_oculta = ["_"] * len(palabra_adivinar) #se creara una lista con n cantidad de digitos y con el caracter de '_'
            letras_incorrectas = [] #lista para las letras incorrectas
            intentos = nivel_de_dificultad()#metodo que retornara los intentos segun el nivel de dificultad
            reglas_del_juegos()#metodo que mostrara las reglas del juego
            Juego_del_ahorcado(palabra_adivinar, palabra_oculta, letras_incorrectas, intentos)#cargara los datos del juego

        elif opcion_menu == "2":
            cargar_juego_guardado()#el metodo cargara los datos guardados del juego
        elif opcion_menu == "#":
            break
        else:
            print("opcion no disponible")
        time.sleep(1)

menu_del_juego()
print("Juego fianlizado")