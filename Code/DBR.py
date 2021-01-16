from character import Character
import random, socket

HOST = '127.0.0.1'
PORT = 1729

online = True
s = None
pj = None

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
    global pj

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
    if online:
        s.send(pejota.encode('utf-8'))
    play()


def clear():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")




def process_input(str, values):
    while(True):
        print(str)
        action = input()
        if action.lower() in values:
            return action
        else:
            print("La opción seleccionada no es válida.")


def process_action(action):
    if action=="a":
        clear()
        action = process_input("Selecciona una acción:\n\t-> Ataque cuerpo a cuerpo [c]\n\t-> Ataque de ki [k]", set(["c", "k"]))
        if action=="c":
            clear()
            action = process_input("Elige tu ataque:\n\t-> Puñetazo [p]\n\t-> Patada [t]\n\t-> Con el arma [a]", set(["p", "t", "a"]))
            tirada = random.randint(1,21)
            print("Has elegido atacar y has sacado " + str(tirada) + " + [" + str(pj.stats["fuerza"]) + "] = " + str(tirada + pj.stats["fuerza"]))
            if action == pj.arma:
                print("Deberías hacer " + str(random.randint(1,5)) + " + [" + str(pj.stats["fuerza"]) + "] de daño (ataque diestro).")
            else:
                print("Deberías hacer " + str(random.randint(1,3)) + " + [" + str(pj.stats["fuerza"]) + "] de daño (ataque débil).")
            input()

        elif action=="k":
            clear()
            action = process_input("Elige una acción:\n\t-> Bola [b]\n\t-> Técnicas [t]", set(["t", "b"]))
            tirada = random.randint(1,21)
            if action == "b":
                print("Has elegido atacar y has sacado " + str(tirada) + " + [" + str(pj.stats["destreza"]) + "] = " + str(tirada + pj.stats["destreza"]))
                print("Deberías hacer " + str(random.randint(1,3)) + " + [" + str(pj.stats["ki"]) + "] de daño.")
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
                    print("Tu tirada de ki es de " + str(random.randint(1,21)) + " + [" + str(pj.stats["ki"]) + "].")
                    if action == "m":
                        clear()
                        print("Con tu técnica media, haces " + str(random.randint(1,7)) + " + [" + str(pj.stats["ki"]) + "] de daño." )
                        pj.cargas_ki -= 2
                    elif action == "f":
                        clear()
                        print("Con tu técnica fuerte, haces " + str(random.randint(1,11)) + " + [" + str(pj.stats["ki"]) + "] de daño." )
                        pj.cargas_ki -= 4
            input()
    elif action == "i":
        clear()
        print("Has seleccionado inventario")
        print(color.PURPLE + "Tienes " + str(pj.nofils) + " nofils." + color.END)
        print(color.BOLD + "Tus objetos son:" + color.END)
        for item in pj.items.keys():
            print("-> " + item)
        action = process_input("Selecciona una opción:\n\tAñadir objeto [a]\tModificar nofils [m]\tTirar objeto [t]\tNotas[n]", set(["a", "m", "t", "n"]))
        if action == "a":
            clear()
            print("¿Qué objeto quieres añadir?")
            objeto = input()
            clear()
            print(objeto + " ha sido añadido a tu inventario.")
            if objeto in pj.items.keys():
                pj.items[objeto]+=1
            else:
                pj.items[objeto] = 1
        elif action == "m":
            clear()
            print("¿Cuánto cambian tus nofils?")
            cambio = input()
            if pj.nofils + int(cambio) < 0:
                print("Estás arruinado.")
            else:
                pj.nofils += int(cambio)
                print("Tu balance actual es de " + str(pj.nofils) + " nofils")
        input()
    elif action == "c":
        tirada = random.randint(1,3)
        print("Has elegido cargar. Consigues " + str(tirada) + " cargas de ki.")
        pj.cargas_ki += tirada
        input()

def play():
    global pj
    while (True):
        clear()
        print(color.BOLD + "\t\t" + pj.nombre + color.END)
        print(color.BLUE + "\t" +"FUERZA = " + str(pj.stats["fuerza"]) + "\tDESTREZA = " + str(pj.stats["destreza"]) + color.END)
        print(color.BLUE + "\t" + "KI = " + str(pj.stats["ki"]) + "\t\tCARISMA = " + str(pj.stats["carisma"]) + color.END)
        print(color.BLUE + "\t" + "PILOTAJE = " + str(pj.stats["pilotaje"]) + "\tJINCHONERÍA = " + str(pj.stats["jinchoneria"]) + color.END)
        print(color.BLUE + "\t" + "LÓGICA = " + str(pj.stats["logica"]) + "\tCOPIA = " + str(pj.stats["copia"]) + color.END)
        print(color.GREEN + "\t" + "VIDA = " + str(pj.salud_actual) + "/" + str(pj.salud) + "\tCARGAS DE KI = " + str(pj.cargas_ki) + color.END)
        print("Elige una acción:\n\tAtacar [a]\tInventario [i]\tCargar [c]\tVolver [v]")
        action = input()
        if action.lower() == "v":
            break
        process_action(action.lower())
    main_menu()




def main_menu():
    #COMIENZA EL PROGRAMA
    print(color.BOLD + "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t Dragon Ball Rol" + color.END)
    #MENÚ PRINCIPAL
    while(True):
        print("Selecciona una opción:\n \t -> Crear un personaje [crear]\n\t -> Cargar un personaje [cargar]")
        command = input()
        if command.lower() == "crear":
            create()
        elif command.lower() == "cargar":
            load()
        else:
            print("No has escrito un comando correcto. Vuelve a intentarlo.")

#En primer lugar, nos conectamos al host

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((HOST, PORT))
except:
    online = False
if online:
    s.sendall(b'Nueva conexion')
#    data = s.recv(1024)
#print('Recibido', repr(data))

#Ahora, llamamos al main menu

main_menu()
