"""
This is the server portion of a multithreaded server / client program
"""
import threading
import socket

# receive packets from any network interfaces of this family
hostname = ''
# default non-privileged port
portnum = 42000


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
            print("Revving up those fryers...\n")
            client_sock, addr = self.sock.accept()
            client_sock.settimeout(10)
            print("Request from the IP ", addr[0])
            process = threading.Thread(target=self.handle_client, args=(client_sock, addr))
            print("Started process {process}".format(process=process))
            process.run()
            Server.client_cnt += 1
            print("Client count is {count}\n".format(count=Server.client_cnt))


    def handle_client(self, connection, address):
        """ Fetch data from client and send response """
        size = 1024
        print("Connected {connect} at {addr}".format(connect=address[0], addr=address[1]))
        try:
            print("Fetching data from client")
            while True:
                get_data = connection.recv(size)
                if not get_data:
                    break
                if get_data == "":
                    print("Socket closed remotely")
                print("Received data {data}".format(data=get_data))
                bytes.decode(get_data, encoding="utf-8", errors="strict")
                response = get_data
                connection.sendall(response)
        except OSError:
            Server.client_cnt -= 1
            print("There was an error with receiving client data")
        finally:
            print("Closing socket")
            connection.close()

if __name__ == "__main__":
    server = Server(hostname, portnum)
    server.run()
