import socket, random, rol


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




print("Introduce la IP del servidor.")
HOST = str(input())
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((HOST, 1729))
except:
    print("No se ha podido establecer la conexión.")
    quit()




def main_menu():
    global s
    while True:
        action = rol.process_input(color.BOLD + "\t\tDragon Ball Rol: Master Edition\n\n"
        + color.END + "Hola, Juan. " + random.choice(saludo) + "\n\t -> Lista de jugadores [lista]" +
        "\n\t -> Crear personaje [crear]\n\t -> Enviar mensaje [mensaje]\n\t -> Cargar personaje [cargar]\n\t -> Tienda [tienda]\n\t -> Subir de nivel [nivel]",
        set(["lista", "mensaje"]))
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
#Comienzo del programa
main_menu()


#Una vez que hayas cargado un personaje, entonces debes poder tirar dados
