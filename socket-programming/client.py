import socket
 
def main():
    host = "127.0.0.1"
    port = 6116
                 
    _socket = socket.socket()
    _socket.connect ((host,port))
    print ("Connected to " + host + " on port " + str (port))
                 
    while True:
        msg = input ("Enter message: ")
        _socket.send (msg.encode ())
        reply = _socket.recv (1024).decode ()
        print ('Received from server: ' + reply)
                         
    _socket.close()
 
if __name__ == '__main__':
    main()
