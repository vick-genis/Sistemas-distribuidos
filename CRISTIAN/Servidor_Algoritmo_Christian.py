import socket
import datetime
import time
# function used to initiate the Clock Server

def RelojInicio():
    i=0
    client_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("El socket se creo de forma correcta")
 
    # Server port

    port = 4040
 
    client_socket.bind(('127.0.0.1', port))

    # Start listening to requests

    client_socket.listen(5)      

    print("El socket esta en modo escucha")


    # Clock Server Running forever
    try:
        while True: 

       # Establish connection with client

            if(i==0):
                time.sleep(0.1)
            
            else:
                time.sleep(10)
                print("Esperando la conexión...")
            

            connection, address = client_socket.accept()      

            print('El servidor está conectado a la dirección siguiente:', address)
       
       # Respond the client with server clock time

            connection.send(str(datetime.datetime.now()).encode())
             
            i=1

       # Close the connection with the client process 
            
            

    except KeyboardInterrupt:
        print("Interrupción mediante Ctrl + C")
        connection.close()
 
# Driver function

if __name__ == '__main__':
 

    # Trigger the Clock Server    

    RelojInicio()