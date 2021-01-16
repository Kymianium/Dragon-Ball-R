import socket

HOST = '127.0.0.1'
PORT = 1729

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Se ha conectado', addr)
        while True:
            data = conn.recv(1024)
            if data:
                print("Nuevo mensaje;\n", str(data, 'utf-8'))
#            if not data:
#                break
#            conn.sendall(data)
