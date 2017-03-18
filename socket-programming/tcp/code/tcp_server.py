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

def isNumber (n):
    if n.isdigit ():
        return True
    else:
        try:
            float (n)
            return True
        except ValueError:
            return False

def parseMessage (msg):
    msg = msg.split (" ")
    if len (msg) != 3:
        return "Invalid format!"
    elif (msg[1] not in op or not isNumber (msg[0]) or not isNumber (msg[2])):
        return "Invalid format!"
    return str (round (op[msg[1]] (float (msg[0]), float (msg[2])), 2))

def main ():
    buffer = 32
    host = ""
    port = 3000
    sock = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    sock.bind ((host, port))
    sock.listen (1)
    print ("Listening for connection on port", str (port), "...")
    connection, client = sock.accept ()
    print ("Receives connection from:", client[0], "\n")

    while True:
        msg = connection.recv (buffer).decode ()

        if msg.lower () == "exit":
            break

        print ("Received message        :", msg)
        result = parseMessage (msg)
        print ("Returning               :", result, "\n")

        connection.send (result.encode ())
        print ("Waiting for another request...")

    print ("Program terminated.")
    sock.close ()

if __name__ == "__main__":
    main ()
