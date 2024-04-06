import socket
import time
from dateutil import parser
from timeit import default_timer as timer
import datetime
import random

def TiempoSincronizacion():
    # Configuración del cliente
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    server_port = 4040
    client_socket.connect(('127.0.0.1', server_port))
    random_variable = random.randint(2, 7)

    request_time = timer()
 
    # receive data from the server

    server_time = parser.parse( client_socket.recv(1024).decode())
    time.sleep(random_variable)
    response_time = timer() 

    actual_time = datetime.datetime.now()
 
    print("El tiempo del Servidor es:" + str(server_time))
    
    
    
    time.sleep(random_variable)
    #Se calcula la latencia de procesamiento restando el tiempo de solicitud del tiempo de respuesta.
    process_delay_latency = response_time - request_time 
 
    print("Latencia de Retraso: " + str(process_delay_latency) + " segundos")
 
    print("El reloj actual del cliente es: "  + str(actual_time))
 
    # synchronize process client clock time
    #tiempo sincronizado del cliente para informar al usuario sobre el proceso de sincronización.
    #Se calcula el tiempo sincronizado del cliente sumando la mitad de la latencia de procesamiento al tiempo recibido del servidor.
    client_time = server_time  + datetime.timedelta(seconds = (process_delay_latency) / 2)
 
    print("Proceso de sincronización: " + str(client_time))

    # calculate synchronization error 
    #Se calcula el error de sincronización restando el tiempo actual del cliente del tiempo sincronizado del cliente.
    error = actual_time - client_time 

    print("Error de sincronizacion : "+ str(error.total_seconds()) + " segundos")
 
    client_socket.close()        
 
 
# Driver function

if __name__ == '__main__':
 

    # synchronize time using clock server

    TiempoSincronizacion()