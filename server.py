"""
This is the server portion of a multithreaded server / client program
"""
import threading
import socket

# receive packets from any network interfaces of this family
hostname = '127.0.0.1'
# default non-privileged port
portnum = 47989


class Server(object):
    """ Threaded server """
    client_cnt = 0

    def __init__(self, host, port):
        """ Server constructor """
        print("Constructing")
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def run(self):
        """ Prepare a server socket and listen """
        print("Listening")
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        self.sock.listen(1)

        while True:
            print("Revving up those fryers...")
            client_sock, addr = self.sock.accept()
            client_sock.settimeout(10)
            print("Request from the IP ", addr[0])
            process = threading.Thread(target=handle_client, args=(client_sock, addr))
            process.run()
            print("Started process {process}".format(process=process))
            Server.client_cnt += 1
            print("Client count is {count}".format(count=Server.client_cnt))


def handle_client(connection, address):
    size = 1024
    try:
        print("Connected {connect} at {addr}".format(connect=connection, addr=address))
        while True:
            get_data = connection.recv(size)
            if get_data:
                bytes.decode(get_data, encoding='utf-8')
                if get_data == "":
                    print("Socket closed remotely")
                    break
            print("Received data {data} ".format(data=get_data))
            connection.sendall(get_data)
    except socket.error:
        Server.client_cnt -= 1
        print("There was a problem handling the request")
    finally:
        print("Closing socket")
        connection.close()

if __name__ == "__main__":
    server = Server(hostname, portnum)
    server.run()
