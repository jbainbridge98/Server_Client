import socket
import sys
import time
import threading

def client():
    try:
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[C]: Client socket created")
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()

    # Define the port on which you want to connect to the server
    port = 50007
    localhost_addr = socket.gethostbyname(socket.gethostname())
    # connect to the server on local machine
    server_binding = (localhost_addr, port)
    cs.connect(server_binding)
    # Receive data from the server
    #data_from_server=cs.recv(100)
    #print("[C]: Data received from server: {}".format(data_from_server.decode('utf-8')))
    #sending message to server
    file = open('in-proj.txt', 'r')
    for line in file:
        msg = line
        cs.send(msg.encode('utf-8'))
        time.sleep(0.5)
        rm = cs.recv(1024)
        print("[C]: Data sent to server: " + msg)
        print("\n")
        print("[C]: Data received from server: {}".format(rm.decode('utf-8')))
        print("\n")
    # close the client socket
    cs.close()
    exit()
if __name__ == "__main__":
    t1 = threading.Thread(name='client', target=client)
    t1.start()
