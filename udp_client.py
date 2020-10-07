import argparse
import socket


def client(host: str, port: int, has_input: int = 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        if has_input:
            send_msg = input("Input your message:")
            sock.sendto(send_msg.encode("utf-8"), (host, port))

        data, addr = sock.recvfrom((1 << 16) - 1)
        print(f"{addr}: {data.decode('utf-8')}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", type=str, default="")
    parser.add_argument("-p", type=int, default=8888)
    parser.add_argument("-i", type=int, default=1)
    args = parser.parse_args()
    client(args.a, args.p, args.i)
