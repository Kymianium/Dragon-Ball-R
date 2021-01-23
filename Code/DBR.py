from character import Character
import random, socket, time, threading

HOST = '127.0.0.1'
PORT = 1729

online = False
s = None
pj = None

context = ""

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def d(num, stat = None):
    global online
    global pj
    value = random.randint(1,num)
    if online and pj:
        global s
        if stat != None:
            cadena = "La tirada de " + str(stat) + " de " + pj.nombre + " ha sido " + str(value) + " + [" + str(pj.stats[stat]) + "]"
        else:
            cadena = "La tirada de " + pj.nombre + " ha sido " + str(value)
        s.sendall(cadena.encode("utf-8"))
    return value

def online_thread():
    global s
    global context
    print("ONLINE")
    while True:
        try:
            message = s.recv(2048)
            if message:
                clear()
                print(color.BLUE + "Nuevo mensaje del master:" + color.END)
                print(message.decode("utf-8"))
                print("Presiona enter para continuar")
                input()
                print(context)
        except:
            continue


def create():
    while(True):
        fuerza = 0
        carisma = 0
        destreza = 0
        pilotaje = 0
        copia = 0
        jinchoneria = 0
        logica = 0
        ki = 0
        weapon = ""
        print(color.BOLD + "Bienvenido al creador de personajes. Lárgate de aquí si no quieres sufrir." + color.END)

        while (True):
            print("¿Cuál es tu nombre?\n")
            nombre = input()
            if nombre == "character":
                print("Tu nombre no puede ser character. Cúrratelo un poco más.")
                continue
            break


        while (True):
            print("\n \t Selecciona tu raza:\n\t -> \033[91m Saiyan [saiyan]: \033[0m Tienen cola, tienen células S (les permiten transformarse en súper " +
            "saiyans) y reciben un excelente cada vez que les derrotan.\n\t -> \033[92m Droides [droide]; \033[0m Roban ki y se reparan. Son actualizables " +
            "(pueden conseguir atributos con discos y componentes de hardware). \n\t -> \033[94m Bestias [bestia]: \033[0m Tienen cola, se pueden transformar " +
            "en bestias más gordas (tienen un modo berserk) y consiguen un excelente cada vez que derrotan a alguien en una pelea." +
            "\n\t -> \033[36m Italianos [italiano]: \033[0m La escoria de Dragon Ball R. +1 en carisma. Tienen amplios conocimientos sobre la pasta, la única " +
            "energía renovable de Dragon Ball R. Son drogadictos, lo cual implica que tiran con ventaja cuando están bajo los efectos" +
            "de la droga y tiran con desventaja si están enmonaos.\n\t -> \033[95m Humanos [humano]: \033[0m Están extintos. No tienen nada. Dios no los quiere.")

            raza = input()

            if raza.lower() == "italiano":
                carisma += 1
                break
            elif (raza.lower() != "saiyan" and raza.lower() != "droide" and raza.lower() != "bestia" and raza.lower() != "humano"):
                print("No se ha reconocido esa raza.\n\n")
                continue
            break

        while (True):
            print("\n\n\t Selecciona una clase: \n\t \033[91m ->  Pirata [pirata]: \033[0m Es maricón. Tiene +2 de pilotaje y +2 de jinchonería.\n\t \033[95m -> Policía [policia]: \033[0m " +
            "+2 de carisma y +2 en lógica.\n\t \033[96m -> Artista Marcial [marcial]: \033[0m +2 en fuerza y -1 punto al daño, lo cual significa que recibe un punto "+
            "menos de daño.\n\t \033[92m -> Ninja [ninja]:\033[0m +2 de destreza y +2 de copia. \n\t \033[93m -> Caballero (BLOQUEADA) [caballero]:\033[0m Recibe la mitad del daño y tiene " +
            "+2 en carisma.")

            clase = input()

            if clase.lower() == "pirata":
                pilotaje += 2
                jinchoneria += 2
                break
            elif clase.lower() == "policia":
                carisma += 2
                logica += 2
                break
            elif clase.lower() == "marcial":
                fuerza += 2
                break
            elif clase.lower() == "ninja":
                destreza += 2
                copia += 2
                break
            elif clase.lower() == "caballero":
                print("Esta clase está bloqueada.\n")
                #carisma += 2
                #break
            else:
                print("No se ha reconocido esa clase.\n\n")
        while (True):
            print("Ahora, debes elegir con qué repartes leña. Tus opciones son:\n\t-> A puño [p]\n\t-> A patadas [t]\n\t-> Con mi arma [a]")
            weapon = input()
            if weapon.lower() == "p" or weapon.lower() == "t" or weapon.lower() == "a":
                break
            else:
                print("Aprende a escribir, maricón.\n")


        print("\n\nPor último, tienes que repartir 7 puntos entre tu fuerza, tu destreza y tu ki.")
        while(True):
            print("Fuerza: ")
            f = int(input())
            print("Destreza: ")
            d = int(input())
            print("Ki: ")
            k = int(input())
            if f+d+k!=7:
                print("Tus atributos no suman siete, maquinote. Mira a ver.\n\n")
                continue
            fuerza+=f
            destreza+=d
            ki+=k
            break
        arma = " con su arma."
        if weapon == "p":
            arma = " a puñetazos."
        elif weapon == "t":
            arma = " a patadas."
        print("\n\nSe va a crear el siguiente personaje:\n\n\t" + nombre + ", " + raza + " de la clase " + clase + " con fuerza " + str(fuerza) + ", con destreza " + str(destreza) + " y con ki " + str(ki) + " y que pega" + arma + "\n\n")
        print("¿Estás de acuerdo? [Si/No]\n")
        respuesta = input()
        if respuesta.lower() == "si":
            pj = Character(nombre, fuerza, destreza, ki, carisma, pilotaje, jinchoneria, logica, copia, raza, clase, weapon, max(2*(fuerza+destreza+ki+carisma+pilotaje+jinchoneria+logica+copia), 20), 0, 0)
            file = open(nombre + ".txt", "w")
            file.write("Personaje de DBR:\n")
            file.write(str(fuerza) + "\n")
            file.write(str(destreza)+ "\n")
            file.write(str(ki)+ "\n")
            file.write(str(carisma)+ "\n")
            file.write(str(pilotaje)+ "\n")
            file.write(str(jinchoneria)+ "\n")
            file.write(str(logica)+ "\n")
            file.write(str(copia)+ "\n")
            file.write(str(raza)+ "\n")
            file.write(str(clase)+ "\n")
            file.write(weapon + "\n")
            file.write(str(max(2*(fuerza+destreza+ki+carisma+pilotaje+jinchoneria+logica+copia), 20)) + "\n")
            file.write(str(0) + "\n")
            file.write(str(0) + "\n")
            file.close()
            file = open("characters.txt", "a")
            file.write(nombre + "\n")
            file.close()
            break
        play()



def load():
    global s
    global pj
    global online
    file = open("characters.txt", "r")
    linea = file.readline()
    if not linea:
        print("No tienes personajes para elegir, crea uno primero, subnormal.")
        return
    print(color.BOLD + "Selecciona un pj:"  + color.END)
    pjs = set()
    while linea:
        pjs.add(linea[:-1])
        linea = file.readline()
    for per in pjs:
        print("\t" + per)
    while (True):
        pejota = input()
        if (pejota in pjs):
            break
        print("No tienes ese personaje, tonto.")
    file.close()


    file = open(pejota + ".txt", "r")
    file.readline()
    str = int(file.readline())
    dst = int(file.readline())
    ki = int(file.readline())
    car = int(file.readline())
    pi = int(file.readline())
    jin = int(file.readline())
    log = int(file.readline())
    co = int(file.readline())
    raza = file.readline()[:-1]
    clase = file.readline()[:-1]
    wpn = file.readline()[:-1]
    life = int(file.readline())
    cki = int(file.readline())
    zenis = int(file.readline())
    pj = Character(pejota, str, dst, ki, car, pi, jin, log, co, raza, clase, wpn, life, cki, zenis)
    items = {}
    for line in file:
        raw = line.split(' ', 2)
        items[raw[2][:-1]] = [int(raw[0]), int(raw[1])]
    pj.set_items(items)
    if online:
        print("login succesfull")
        message = "login " + pejota
        s.sendall(message.encode('utf-8'))
    play()


def clear():
    for i in range(0,100):
        print(" \n")


def process_input(str, values):
    while(True):
        printc(str)
        action = input()
        if action.lower() in values:
            return action.lower()
        else:
            print("La opción seleccionada no es válida.")

def read_from_master(s):
    while True:
        try:
            message = s.recv(2048)
            if message:
                command = message.decode("utf-8").split(' ', 1)
                print(command)
                if command[0] == "msg":
                    clear()
                    print(color.BOLD + "Nuevo mensaje del master:" + color.END)
                    print(command[1])
                    input()
                    clear()
                else:
                    print(message.decode("utf-8"))
        except:
            continue

def process_action(action):
    if action=="a":
        clear()
        action = process_input("Selecciona una acción:\n\t-> Ataque cuerpo a cuerpo [c]\n\t-> Ataque de ki [k]", set(["c", "k"]))
        if action=="c":
            clear()
            action = process_input("Elige tu ataque:\n\t-> Puñetazo [p]\n\t-> Patada [t]\n\t-> Con el arma [a]", set(["p", "t", "a"]))
            tirada = d(20, "fuerza")
            print("Has elegido atacar y has sacado " + str(tirada) + " + [" + str(pj.stats["fuerza"]) + "] = " + str(tirada + pj.stats["fuerza"]))
            if action == pj.arma:
                print("Deberías hacer " + str(d(4, "fuerza")) + " + [" + str(pj.stats["fuerza"]) + "] de daño (ataque diestro).")
            else:
                print("Deberías hacer " + str(d(2, "fuerza")) + " + [" + str(pj.stats["fuerza"]) + "] de daño (ataque débil).")
            input()
        elif action=="k":
            clear()
            action = process_input("Elige una acción:\n\t-> Bola [b]\n\t-> Técnicas [t]", set(["t", "b"]))
            tirada = d(20, "destreza")
            if action == "b":
                print("Has elegido atacar y has sacado " + str(tirada) + " + [" + str(pj.stats["destreza"]) + "] = " + str(tirada + pj.stats["destreza"]))
                print("Deberías hacer " + str(d(2)) + " + [" + str(pj.stats["ki"]) + "] de daño.")
            elif action == "t":
                if pj.cargas_ki < 2:
                    print("No tienes suficiente ki")
                else:
                    while True:
                        clear()
                        action = process_input("Elige tu técnica\n\t-> Técnica media [m]\n\t-> Técnica fuerte [f]", set(["f", "m"]))
                        if action == "f" and pj.cargas_ki < 4:
                            print("No tienes el suficiente ki")
                            input()
                            continue
                        break
                    clear()
                    print("Tu tirada de ki es de " + str(d(20, "ki")) + " + [" + str(pj.stats["ki"]) + "].")
                    if action == "m":
                        print("Con tu técnica media, haces " + str(d(6, "ki")) + " + [" + str(pj.stats["ki"]) + "] de daño." )
                        pj.cargas_ki -= 2
                    elif action == "f":
                        print("Con tu técnica fuerte, haces " + str(d(10, "ki")) + " + [" + str(pj.stats["ki"]) + "] de daño." )
                        pj.cargas_ki -= 4
            input()
    elif action=="d":
        action = process_input("¿De qué quieres que sea tu tirada?"
        + "\n\tFuerza [F]\tDestreza [D]\tKi [K]\tJinchonería [J]\tCopia [C]\n\tCarisma [A]\tPilotaje [P]\tLógica [L]\tTirada plana [N]", set(["f", "d", "k", "j", "c", "a", "p", "l", "n"]))
        clear()
        if action == "f":
            print("Tu tirada de fuerza ha sido de " + str(d(20, "fuerza")) + " + [" + str(pj.stats["fuerza"]) + "]")
            input()
        elif action == "d":
            print("Tu tirada de destreza ha sido de " + str(d(20, "destreza")) + " + [" + str(pj.stats["destreza"]) + "]")
            input()
        elif action == "k":
            print("Tu tirada de ki ha sido de " + str(d(20, "ki")) + " + [" + str(pj.stats["ki"]) + "]")
            input()
        elif action == "j":
            print("Tu tirada de jinchonería ha sido de " + str(d(20, "jinchoneria")) + " + [" + str(pj.stats["jinchoneria"]) + "]")
            input()
        elif action == "c":
            print("Tu tirada de copia ha sido de " + str(d(20, "copia")) + " + [" + str(pj.stats["copia"]) + "]")
            input()
        elif action == "a":
            print("Tu tirada de carisma ha sido de " + str(d(20, "carisma")) + " + [" + str(pj.stats["carisma"]) + "]")
            input()
        elif action == "p":
            print("Tu tirada de pilotaje ha sido de " + str(d(20, "pilotaje")) + " + [" + str(pj.stats["pilotaje"]) + "]")
            input()
        elif action == "l":
            print("Tu tirada de lógica ha sido de " + str(d(20, "logica")) + " + [" + str(pj.stats["logica"]) + "]")
            input()
        elif action == "n":
            print("Tu tirada ha sido de " + str(d(20)))
            input()

    elif action == "i":
        clear()
        printc("Has seleccionado inventario" + "\n"
        + color.PURPLE + "Tienes " + str(pj.nofils) + " nofils." + color.END + "\n"
        + color.BOLD + "Tus objetos son:" + color.END + "\n")
        for item in pj.items.keys():
            print("-> " + item + " x" + str(pj.items[item][1]) + "\t\t\t" + str(float(pj.items[item][0])/1000) + "kg")
        action = process_input("Selecciona una opción:\n\tAñadir objeto [a]\tModificar nofils [m]\tTirar objeto [t]\tNotas[n]", set(["a", "m", "t", "n"]))
        if action == "a":
            clear()
            printc("¿Qué objeto quieres añadir?")
            objeto = input()
            clear()
            if objeto in pj.items.keys():
                pj.items[objeto][1] += 1
            else:
                printc("¿Cuántos gramos pesa?")
                peso = int(input())
                pj.items[objeto] = [peso, 1]
            printc(objeto + " ha sido añadido a tu inventario.")

        elif action == "m":
            clear()
            printc("¿Cuánto cambian tus nofils?")
            cambio = input()
            if pj.nofils + int(cambio) < 0:
                printc("Estás arruinado.")
            else:
                pj.nofils += int(cambio)
                printc("Tu balance actual es de " + str(pj.nofils) + " nofils")
        input()
    elif action == "c":
        tirada = d(2)
        printc("Has elegido cargar. Consigues " + str(tirada) + " cargas de ki.")
        pj.cargas_ki += tirada
        input()
    elif action == "e":
        printc("Tu tirada de esquivar ha sido " + str(d(20, "destreza")) + " + [" + str(pj.stats["destreza"]) + "]")
        input()
    else:
        clear()
        printc("Esa no es una opción mongolo")
        input()
        clear()

def printc(msg):
    global context
    context = msg
    print(msg)

def play():
    global s
    global pj
    while (True):
        clear()
        printc(color.BOLD + "\t\t" + pj.nombre + color.END + "\n"
        + color.BLUE + "\t" +"FUERZA = " + str(pj.stats["fuerza"]) + "\tDESTREZA = " + str(pj.stats["destreza"]) + color.END + "\n"
        + color.BLUE + "\t" + "KI = " + str(pj.stats["ki"]) + "\t\tCARISMA = " + str(pj.stats["carisma"]) + color.END + "\n"
        + color.BLUE + "\t" + "PILOTAJE = " + str(pj.stats["pilotaje"]) + "\tJINCHONERÍA = " + str(pj.stats["jinchoneria"]) + color.END + "\n"
        + color.BLUE + "\t" + "LÓGICA = " + str(pj.stats["logica"]) + "\tCOPIA = " + str(pj.stats["copia"]) + color.END + "\n"
        + color.GREEN + "\t" + "VIDA = " + str(pj.salud_actual) + "/" + str(pj.salud) + "\tCARGAS DE KI = " + str(pj.cargas_ki) + color.END + "\n"
        + "Elige una acción:\n\tAtacar [a]\tEsquivar [e]\tInventario [i]\tCargar [c]\tVolver [v]\n\tTirar dado [d]")
        action = input()
        if action.lower() == "v":
            #Volver
            if online:
                s.sendall("logout".encode("utf-8"))


            file = open(pj.nombre + ".txt", "w")
            file.write("Personaje de DBR:\n")
            file.write(str(pj.stats["fuerza"]) + "\n")
            file.write(str(pj.stats["destreza"])+ "\n")
            file.write(str(pj.stats["ki"]) + "\n")
            file.write(str(pj.stats["carisma"]) + "\n")
            file.write(str(pj.stats["pilotaje"]) + "\n")
            file.write(str(pj.stats["jinchoneria"]) + "\n")
            file.write(str(pj.stats["logica"]) + "\n")
            file.write(str(pj.stats["copia"]) + "\n")
            file.write(str(pj.raza) + "\n")
            file.write(str(pj.clase) + "\n")
            file.write(pj.arma + "\n")
            file.write(str(pj.salud) + "\n")
            file.write(str(pj.cargas_ki) + "\n")
            file.write(str(pj.nofils) + "\n")
            for item in pj.items.keys():
                file.write(str(pj.items[item][0]) + " " + str(pj.items[item][1]) + " " + str(item) + "\n")
            file.close()


            break
        process_action(action.lower())
    main_menu()


def connect():
    global s
    global online
    clear()
    print("¿Cuál es la IP a la que quieres conectarte?")
    HOST = str(input())
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((HOST, PORT))
    except:
        print("No se ha podido establecer la conexión.")
        return
    time.sleep(1)
    s.sendall(b'El jugador ha establecido conexion.')
    clear()
    print("Estás en línea. Bienvenido a Dragon Ball R Online.")
    t = threading.Thread(target = online_thread)
    t.start()
    input()
    online = True
    clear()

def main_menu():
    #MENÚ PRINCIPAL
    while(True):
        #COMIENZA EL PROGRAMA
        print(color.BOLD + "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t Dragon Ball Rol" + color.END)
        if online:
            print(color.BOLD + "Status: " + color.GREEN + "ONLINE" + color.END)
        else:
            print(color.BOLD + "Status: " + color.RED + "OFFLINE" + color.END)
        print("Selecciona una opción:\n \t -> Crear un personaje [crear]\n\t -> Cargar un personaje [cargar]\n\t -> Conectarse al servidor [conectar]\n\t -> Comprobar conexión con el servidor [ping]")
        command = input()
        if command.lower() == "crear":
            create()
        elif command.lower() == "cargar":
            load()
        elif command.lower() == "conectar":
            connect()
        elif command.lower() == "ping":
            ping()
        else:
            print("No has escrito un comando correcto. Vuelve a intentarlo.")
def ping():
    global s
    global online
    clear()
    if online:
        s.sendall(b'Ping')
        print("Al host debe haberle llegado un mensaje.")
        input()
        clear()
    else:
        print("No estás online.")
        input()
        clear()
main_menu()
