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

def isNumber (n):
    if n.isdigit ():
        return True
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
    else:
        return str (round (op[msg[1]] (float (msg[0]), float (msg[2])), 2))

def main ():
    buffer = 1024
    host = ""
    port = 3000
    sock = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind ((host, port))
    print ("Listening on port", str (port), "...")

    while True:
        msg, client = sock.recvfrom (buffer)
        msg = msg.decode ()

        if msg.lower () == "exit":
            break

        print ("Receives message from:", client[0])
        print ("Received message     :", msg)

        result = parseMessage (msg)
        print ("Returning            :", result, "\n")

        sock.sendto (result.encode (), client)
        print ("Waiting for another connection...")

    print ("Program terminated.")

if __name__ == "__main__":
    main ()
