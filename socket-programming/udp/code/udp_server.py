import operator
import socket

op = {
    "+":  operator.add,
    "-":  operator.sub,
    "*":  operator.mul,
    "/":  operator.__truediv__,
    "%":  operator.mod,
    "**": operator.pow
}

def number (n):
    try:
        float (n)
    except ValueError:
        return False
    return True

def parse (msg):
    msg = msg.split (" ")
    if len (msg) != 3:
        return "Invalid format!"
    elif (msg[1] not in op or not number (msg[0]) or not number (msg[2])):
        return "Invalid format!"
    return str (round (op[msg[1]] (float (msg[0]), float (msg[2])), 2))

def main ():
    buffer = 32
    host = ""
    port = 3000
    sock = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind ((host, port))
    print ("Listening on port", str (port) + "...")

    while True:
        msg, client = sock.recvfrom (buffer)
        msg = msg.decode ()

        if msg.lower () == "exit":
            break

        print ("Receives message from", client[0])
        print ("Received message:", msg)

        result = parse (msg)
        print ("Returning       :", result, "\n")

        sock.sendto (result.encode (), client)
        print ("Waiting for another connection...")

    sock.close ()
    print ("Program terminated.")

if __name__ == "__main__":
    main ()
