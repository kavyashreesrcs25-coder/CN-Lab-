
import socket
import os

def main():
    host = "127.0.0.1"
    port = 65432

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)

    print("Server is waiting for client...")

    conn, addr = server.accept()

    with conn:
        print("Connected to:", addr)

        filename = conn.recv(1024).decode()

        if os.path.isfile(filename):
            with open(filename, "r") as file:
                content = file.read()

            conn.sendall(content.encode())
        else:
            conn.sendall(b"File not found")

    server.close()


if __name__ == "__main__":
    main()
