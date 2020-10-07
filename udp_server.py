import socket


def server(host: str, port: int):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, port))

    print(f"udp server started at {host}:{port}")

    while True:
        data, addr = sock.recvfrom((1 << 16) - 1)
        print(f"{addr}: {data.decode('utf-8')}")
        sock.sendto(b"received", addr)


if __name__ == "__main__":
    server("127.0.0.1", 8888)
