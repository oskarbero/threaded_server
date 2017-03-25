"""
This is the client portion of the client server program
"""
import socket

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', 42000))
    data = 'some nice shiny data'
    sock.sendto(data.encode('utf-8'),('127.0.0.1', 42000))
    print("client data sent")
    sock.recv(1024)
    print("client data received")
    sock.close()
