
import socket

def main():
    host = "127.0.0.1"
    port = 65432

    filename = input("Enter filename to request: ")

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    client.sendall(filename.encode())

    data = client.recv(4096).decode()

    print("\nFile Content:")
    print(data)

    client.close()


if __name__ == "__main__":
    main()
