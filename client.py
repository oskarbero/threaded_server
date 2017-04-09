"""
This is the client portion of the client server program
"""
import socket

# CARO_IP = '50.163.98.9'
MY_SOCKET = 42000
if __name__ == "__main__":
    ip_addr = input ("Ip: ")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.connect((ip_addr, MY_SOCKET))
    cmd = ''
    while cmd is not 'q':
        cmd = input('Command: ')
        sock.sendto(cmd.encode('utf-8'), ('192.168.10.108', 42000))

        data = sock.recv(1024)
        print(str(data.decode('utf-8')))

    print("client data received")
    sock.close()




