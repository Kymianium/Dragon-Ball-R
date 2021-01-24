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
store = {}
player_list = {}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if len(sys.argv) != 2:
    print("Fallo en los argumentos, por favor, indica una IP y un puerto")
    exit()

IP = str(sys.argv[1])
PORT = 1729

server.bind((IP, PORT))

server.listen(10) #10 es el número máximo de conexiones que acepta

print(color.BOLD + "El servidor está operativo." + color.END)


def playerthread(conn, addr):
    print(color.BOLD + "Nuevo hilo creado" + color.END)
    global player_list
    player = ""
    while True:
        try:
            message = conn.recv(2048)
            if message:
                command = message.decode("utf-8").split(' ', 1)
                arguments = message.decode("utf-8").split(' ')
                print(command)
                if command[0] == "admin":
                    if command[1] == "list":
                        print(color.BLUE + "El admin pide una lista." + color.END)
                        if not player_list:
                            answer = "No hay jugadores "
                        else:
                            answer = ""
                            for i in player_list.keys():
                                answer = answer + i + "\n"
                        conn.sendall(answer.encode("utf-8"))
                        print("Se le envía la lista. " + answer)
                    elif command[1] == "msg1":
                        print(color.BLUE + "El admin quiere enviar un mensaje. Se le envía la lista." + color.END)
                        players = ""
                        for pyr in player_list.keys():
                            players = players + pyr + "\n"
                        conn.sendall(players.encode("utf-8"))
                    elif arguments[1] == "msg2":
                        dst = arguments[2]
                        print(color.BLUE + "El admin ha enviado un mensaje a " + dst + "." + color.END)
                        amsg = command[1].split(' ', 2)
                        print(color.BOLD + amsg[2] + color.END)
                        player_list[dst].sendall(amsg[2].encode("utf-8"))

                elif command[0] == "adminmsg":
                    print(color.PURPLE + player + " quiere enviar un mensaje al admin." + color.END)
                    print(color.BOLD + command[1] + color.END)

                elif command[0] == "login":
                    print(color.PURPLE + "Login:" + color.END)
                    print("Añadido " + command[1] + " a la lista de jugadores.")
                    player_list[command[1]] = conn
                    player = command[1]
                elif command[0] == "logout":
                    player = ""
                    del player_list[player]
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


#TIENDA
#BOLSA
