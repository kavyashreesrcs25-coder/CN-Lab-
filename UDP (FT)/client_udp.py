
import socket

def main():
    host = "127.0.0.1"
    port = 5005

    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    filename = input("Enter filename to request: ")

    client.sendto(filename.encode(), (host, port))

    data, server_address = client.recvfrom(4096)

    print("\nFile Content:")
    print(data.decode())

    client.close()


if __name__ == "__main__":
    main()
