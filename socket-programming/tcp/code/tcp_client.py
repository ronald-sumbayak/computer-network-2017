import socket

def main ():
    buffer = 1024
    host = input ("Server IP: ")
    port = 3000
    sock = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    sock.connect ((host, port))
    print ("Connected to", host, "on port", str (port), "\n")

    while True:
        msg = input ("Send    : ")
        sock.send (msg.encode ())

        if msg.lower () == "exit":
            break

        response = sock.recv (buffer).decode ()
        print ("Response:", response, "\n")

    print ("Program terminated.")
    sock.close ()

if __name__ == "__main__":
    main ()
