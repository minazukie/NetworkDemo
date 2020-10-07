import socket


def client(host: str, port: int):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        send_msg = input("Input your message:")
        sock.sendto(send_msg.encode("utf-8"), (host, port))
        data, addr = sock.recvfrom((1 << 16) - 1)
        print(f"{addr}: {data.decode('utf-8')}")


if __name__ == "__main__":
    client("127.0.0.1", 8888)
