import string
import random


def procesar_renglones_vocales(texto: str, vocales: str = "AEIOUaeiou"):  # para el punto 1
    for linea in texto.splitlines():
        linea = linea.strip()
        palabras = linea.split()
        if len(palabras) > 1 and palabras[1][0] in vocales:
            print("------------------------------")
            print(linea)



def max_palabras (titulos):  # para el punto 2, saca los titulos con mas palabras
    maximo = 0
    tit = " "
    for titulo in titulos:
        palabras = titulo.split()
        if len(palabras) > maximo:
            tit = titulo
            maximo = len(palabras)
    print (f"el titulo con mas palabras es el: {tit} , y tiene {maximo} palabras " )


def buscar_palabra (strg: str): # para buscar la palabra en las reglas. Punto 3
    reglas = strg.split(".") #separo las reglas por punto
    buscar = input ("ingrese la palabra clave con la que quiere buscar las reglas: ")
    encontrado = False
    for regla in reglas:
         if buscar.casefold() in regla.casefold(): # con el casefold lo q hago es ignorar si esta con mayusculas o minusculas
            encontrado = True
            print (regla)
    if not encontrado:
        print (" No se encuentra esa palabra ")


def hacer_user (user_name:str):   # condiciones para hacer usuario, punto 4
    if len(user_name) >= 5:
        tiene_num= False
        tiene_may=False
        for caracter in user_name:
            if caracter.isdigit():
                 tiene_num=True
            if caracter.isupper():
                 tiene_may=True
            if not caracter.isalnum():
                 break
        if tiene_num and tiene_may:
            print ( " usuario creado con exito !! " + user_name)   
        else:
            print (" El nombre de usuario no cumple con los requisitos")
    else:
        print (" El nombre de usuario no cumple con los requisitos")


def calcular_tiempo (seg:int):
    if seg < 200:
        print (" Categoria: Rapido")
    elif (200 <= seg <= 500):
        print (" Categoria: Normal")
    elif seg > 500:
        print (" Categoria: Lento")


def cantidad_menciones (texto: list[str]):
    cant_charla = 0
    cant_music= 0
    cant_entre = 0
    for descripcion in texto:
      if "entretenimiento" in descripcion.lower():
            cant_entre += 1
      if "música" in descripcion.lower():
            cant_music += 1
      if "charla" in descripcion.lower():
            cant_charla += 1
    return cant_entre, cant_music,cant_charla

def codigo_descuento (us,date:str):
    if len(us) < 16:
        date = "".join(date.split("-"))
        caracteres = string.ascii_uppercase + string.digits
        k = 30 - len(us) - len(date) - 2 
        cadena_aleatoria = "".join(random.choices(caracteres, k=k)) # pq si no me quedan separados A , 2 , K , M

        print(f"{us.upper}-{date}-{cadena_aleatoria}")
    else:
        print (" El usuario debe tener 15 caracteres o menos")



def son_anagramas (one, two):
    uno= sorted(one.lower().strip()); # paso a minuscula, por las dudas, con el sorted ordeno alfabeticamente y con el strip le saco espacios pq me paso que puse un espacio al final y no lo reconocio
    dos = sorted (two.lower().strip());

    if uno == dos:
        print (f"{one} y {two} , son anagramas")
    else:
        print (f"{one} y {two} no son anagramas")
               


def lista_limpia (lista):
    i= 0
    longitud = len(lista)
    vistos = set() # creo un set vacio para ir agregando los nombres. Lo que hace el set es evitar q hayan repeticiones
    while i < longitud:
        if lista[i] is None or not lista[i].strip(): # pregunto si es igual a none o esta vacia luego de eliminar los espacios
            lista.pop (i)  # lo elimino
            longitud -=1
        else:
            lista[i] = lista[i].title().strip() # paso todo con la primera letra de cada palabra en mayuscula y de paso con eso comparo
            if lista[i] not in vistos:
                 vistos.add(lista[i])
                 if i< longitud:
                     i+= 1
            else:
                lista.pop(i) # si ya esta, lo elimino   
                longitud -=1 # tuve que hacer esto pq co un for me dana index out of range
    
    print (lista)
    


############################ funciones del punto 10







def imprimir_rdos_partidas (rondas):
    """imprime los resultados de cada partida, ordenado x el que mas puntos tiene"""
    i = 1
    estadisticas_totales = {}
    for ronda in rondas:
        print ("RANKING RONDA", str(i))
        encabezado = f"{'JUGADOR':<10} {'KILLS':<8} {'ASISTENCIAS':<14} {'MUERTES':<10} {'PUNTOS':<9}"
        print (encabezado)
        print ("-"* len(encabezado))
        player = [] # creo una lista vacia para ir agregando los jugadores en cada partida y luego la ordeno para imrpimir
        for jugador, datos in ronda.items(): # accedo a los valores de la ronda, de cada clave-jugador
            kill = datos["kills"]
            asist = datos["assists"]
            muertes = datos["deaths"]
            if muertes == True:
                muertes = -1 
            else:
                muertes = 0
            puntos= kill*3 + asist + muertes
            player.append ((jugador, kill*3, asist, muertes, puntos))
        jugadores_ordenados = sorted(player, key=lambda x: x[4], reverse=True)  
    
        for jug in jugadores_ordenados:
             play,kill,asist,muertes,puntos = jug #desarmo la tupla para qeu sea mejor
             print (f" {play:<10}{kill:<8}{asist:<16}{(muertes)*-1:<13}{puntos:<9} ")
             if play not in estadisticas_totales:
                 estadisticas_totales[play] = { "kills":0 , "asistencias":0 , "muertes":0,"MPVs":0, "puntos":0 }
             estadisticas_totales [play]["kills"] += kill
             estadisticas_totales [play]["asistencias"] += asist
             estadisticas_totales [play]["muertes"] += muertes
             estadisticas_totales [play]["puntos"] += puntos
             if jugadores_ordenados[0][0] == play:
                 estadisticas_totales [play]["MPVs"] += 1                      
        i += 1
        print ("")
    
    ordenados_totales = sorted(estadisticas_totales.items(), key = lambda x: x[1]["puntos"], reverse = True) # creo una tupla con dos valores, primero el nombre del jugador,y dps un diccionario con los valores de cada situacion


    print ("RANKING FINAL:")
    print (f"{'JUGADOR':<10} {'KILLS':<8} {'ASISTENCIAS':<14} {'MUERTES':<10} {'PUNTOS':<9} {'MPVs':<6}")
    for jugadores, detalles in ordenados_totales:
        print (f" {jugadores:<10} {detalles['kills']:<8} {detalles['asistencias']:<16} {(detalles['muertes'])*-1:<13}{detalles['puntos']:<9}{detalles['MPVs']:<6}")





