import socket

def main ():
    buffer = 32
    host = input ("Server IP: ")
    port = 3000
    sock = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    sock.connect ((host, port))
    print ("Connected to", host, "on port", str (port) + "\n")
    print ("Format: [$number] [$operator] [$number]. Send 'exit' to stop program on client and server.\n")

    while True:
        msg = input ("Send    : ")
        sock.send (msg.encode ())

        if msg.lower () == "exit":
            break

        response = sock.recv (buffer).decode ()
        print ("Response:", response, "\n")

    sock.close ()
    print ("Program terminated.")

if __name__ == "__main__":
    main ()
