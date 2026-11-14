
import socket
import os

def main():
    host = "127.0.0.1"
    port = 5005

    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((host, port))

    print("UDP Server is waiting for client...")

    while True:
        data, client_address = server.recvfrom(1024)

        filename = data.decode()

        print("Requested file:", filename)

        if os.path.isfile(filename):
            with open(filename, "r") as file:
                content = file.read()

            server.sendto(content.encode(), client_address)
        else:
            server.sendto(b"File not found", client_address)


if __name__ == "__main__":
    main()
