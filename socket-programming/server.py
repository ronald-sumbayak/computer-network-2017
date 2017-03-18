import socket
 
def main():
    host = ""
    port = 6116
    
    _socket = socket.socket ()
    _socket.bind ((host,port))
    _socket.listen (1)
    client, address = _socket.accept ()
    print ("Listening on port " + str (port) + "...")
    
    while True:
        msg = client.recv (1024).decode()
        if not msg:
            break

        print ("Received message: " + msg)
        msg = str (msg).upper ()
        client.send (msg.encode ())
        print ("Message replied to " + address[0] + "on port " + str (address[1]))

    client.close ()
     
if __name__ == '__main__':
    main()
