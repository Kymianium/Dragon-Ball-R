import socket
import sys
import threading

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


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if len(sys.argv) != 2:
    print("Fallo en los argumentos, por favor, indica una IP y un puerto")
    exit()

IP = str(sys.argv[1])
PORT = 1729

server.bind((IP, PORT))

server.listen(10) #10 es el número máximo de conexiones que acepta
player_list = {}

def playerthread(conn, addr):
    print(color.BOLD + "Nuevo hilo creado" + color.END)
    while True:
        try:
            message = conn.recv(2048)
            if message:
                command = message.decode("utf-8").split()
                print(command)
                if command[0] == "admin":
                    if command[1] == "list":
                        print(color.BLUE + "El admin pide una lista." + color.END)
                        answer = ""
                        for i in player_list.keys():
                            answer = answer + i + "\n"
                        conn.sendall(answer.encode("utf-8"))
                        print("Se le envía la lista. " + answer)
                elif command[0] == "login":
                    print("Login:")
                    name = ""
                     #print(command.size())
                    for i in range(1, command.len()):
                        name = name + command[i]
                    #player_list[name] = conn
                    print("Añadido " + name + " a la lista de jugadores.")
                else:
                    print(message.decode("utf-8"))
        except:
            continue


while True:
    conn, addr = server.accept()
    print("Recibido intento de conexión de", addr[0])
    t = threading.Thread(target = playerthread, args = (conn, addr))
    t.start()
    #conn.close()
