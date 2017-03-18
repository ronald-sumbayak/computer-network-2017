import socket

def main ():
    buffer = 1024
    port = 3000
    sock = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        host = input ("Server IP: ")
        msg  = input ("Send     : ")
        sock.sendto (msg.encode (), (host, port))

        if msg.lower () == "exit":
            break

        response, server = sock.recvfrom (buffer)
        print ("Response :", response.decode (), "\n")

    print ("Program terminated.")
    sock.close ()

if __name__ == "__main__":
    main ()
