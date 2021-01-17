import socket
import sys
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if len(sys.argv) != 3:
    print("Fallo en los argumentos, por favor, indica una IP y un puerto")
    exit()

IP = str(sys.argv[1])
PORT = int(sys.argv[2])

server.bind((IP, PORT))

server.listen(10) #10 es el número máximo de conexiones que acepta
player_list = []

def playerthread(conn, addr):
    print("Nuevo hilo creado")
    while True:
        try:
            message = conn.recv(2048)
            if message:
                #print("Nuevo mensaje de", addr[0])
                print(message.decode("utf-8"))
        except:
            continue


def remove(connection):
    if connection in player_list:
        player_list.remove(connection)

while True:
    conn, addr = server.accept()
    player_list.append(conn)
    print("Recibido intento de conexión de", addr[0])
    t = threading.Thread(target = playerthread, args = (conn, addr))
    t.start()
    #conn.close()
