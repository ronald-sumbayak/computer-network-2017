import operator
import socket
import sys

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
    sock = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    sock.bind ((host, port))
    sock.listen (1)
    print ("Listening for connection on port", str (port) + "...")
    connection, client = sock.accept ()
    print ("Receives connection from", client[0], "\n")

    while True:
        msg = connection.recv (buffer).decode ()

        if msg.lower () == "exit":
            break

        print ("Received message:", msg)
        result = parse (msg)
        print ("Returning       :", result, "\n")

        connection.send (result.encode ())
        print ("Waiting for another request...")

    sock.close ()
    print ("Program terminated.")

if __name__ == "__main__":
    main ()
