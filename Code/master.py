import socket, random, rol, threading
from character import Character

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

saludo = ["¿Te has hecho ya una paja hoy?",
"Esperemos que hoy salgan muchas pifias para Johnny.",
"Purple te saluda.",
"Así me gusta, elfos. Aléjate del LoL",
"Bebe agua, mantente hidratado."]

s = None
pj = None


print("Introduce la IP del servidor.")
HOST = str(input())
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((HOST, 1729))
except:
    print("No se ha podido establecer la conexión.")
    quit()
rol.clear()


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


        print("\n\nPor último, tienes que repartir puntos entre tu fuerza, tu destreza y tu ki.")
        print("Fuerza: ")
        f = int(input())
        print("Destreza: ")
        d = int(input())
        print("Ki: ")
        k = int(input())
        fuerza+=f
        destreza+=d
        ki+=k

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


def main_menu():
    global s
    while True:
        action = rol.process_input(color.BOLD + "\t\tDragon Ball Rol: Master Edition\n\n"
        + color.END + "Hola, Juan. " + random.choice(saludo) + "\n\t -> Lista de jugadores [lista]" +
        "\n\t -> Crear personaje [crear]\n\t -> Enviar mensaje [mensaje]\n\t -> Cargar personaje [cargar]\n\t -> Tienda [tienda]\n\t -> Subir de nivel [nivel]",
        set(["lista", "mensaje", "crear"]))
        print(action)
        if action == "lista":
            rol.clear()
            s.sendall("admin list".encode("utf-8"))
            answer = s.recv(2048)
            print(answer.decode("utf-8")[:-1])
            input()
        elif action == "mensaje":
            rol.clear()
            s.sendall("admin msg1".encode("utf-8"))
            list = s.recv(2048).decode("utf-8")
            list = list.split("\n")[:-1]
            while True:
                print("¿A quién quieres enviarle el mensaje?")
                for p in list:
                    print("--> " + p)
                pyr = input()
                if not pyr in list:
                    print("Creo que has escrito mal el nombre Juan, deja los porros.")
                    input()
                    continue
                break
            print("Escribe el mensaje")
            msg = input()
            msg = "admin msg2 " + pyr + " " + msg
            s.sendall(msg.encode("utf-8"))
        elif action == "crear":
            create()
#Comienzo del programa
main_menu()


#Una vez que hayas cargado un personaje, entonces debes poder tirar dados
