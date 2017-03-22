import socket

def main ():
    buffer = 32
    port = 3000
    sock = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
    print ("Format: [$number] [$operator] [$number]. Send 'exit' to stop program on client and server.\n")

    while True:
        host = input ("Server IP: ")
        msg  = input ("Send     : ")
        sock.sendto (msg.encode (), (host, port))

        if msg.lower () == "exit":
            break

        response, server = sock.recvfrom (buffer)
        print ("Response :", response.decode (), "\n")

    sock.close ()
    print ("Program terminated.")

if __name__ == "__main__":
    main ()
