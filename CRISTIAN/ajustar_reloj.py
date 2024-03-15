# ajustar_reloj.py

import time
from datetime import datetime
import socket

def obtener_tiempo_remoto(servidor):
    cliente = socket.create_connection((servidor, 12345))   
    tiempo_servidor = float(cliente.recv(1024).decode())
    cliente.close()
    return tiempo_servidor

def ajustar_reloj(servidor):
    tiempo_remoto = obtener_tiempo_remoto(servidor)
    tiempo_local = time.time()
    ajuste = tiempo_remoto - tiempo_local
    tiempo_ajustado = datetime.fromtimestamp(tiempo_local + ajuste)
    print(f"Tiempo ajustado: {tiempo_ajustado}")

if __name__ == "__main__":
    # Cliente solicita el tiempo al servidor y ajusta su reloj
    servidor_ip = 'localhost'  
    ajustar_reloj(servidor_ip)
