import argparse
import socket


def server(host: str, port: int):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.bind((host, port))

    print(f"udp server started at {host}:{port}")

    while True:
        data, addr = sock.recvfrom((1 << 16) - 1)
        print(f"{addr}: {data.decode('utf-8')}")
        sock.sendto(b"received", addr)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", type=int, default=8888)
    args = parser.parse_args()
    server("", args.p)
