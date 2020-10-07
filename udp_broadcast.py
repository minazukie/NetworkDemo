import socket


def client(host: str, port: int):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.sendto(b"HELLO EVERYONE!", (host, port))


if __name__ == '__main__':
    client("<broadcast>", 8888)
