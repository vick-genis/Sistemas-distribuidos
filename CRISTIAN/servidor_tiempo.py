# servidor_tiempo.py

import time
import socket

def manejar_cliente(client_socket):
    tiempo_servidor = str(time.time())
    client_socket.send(tiempo_servidor.encode())
    client_socket.close()

def servidor_tiempo():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(('localhost', 12345))  
    servidor.listen(1)

    print("Esperando conexión...")
    conn, addr = servidor.accept()
    print("Conectado a", addr)

    manejar_cliente(conn)

    servidor.close()

if __name__ == "__main__":
    servidor_tiempo()
