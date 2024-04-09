import socket

def listener_handler():
    # bind to local address
    sock.bind((host_ip, host_port))
    print('[+] Its so quiet')
    sock.listen()
    remote_target, remote_ip = sock.accept()
    print(f'[+] Connection received from {remote_ip}')
    
    while True:
        try:
            message = input('Message to send#> ')
            # remember that we need to convert the string value of message to bytes using .encode()
            remote_target.send(message.encode())
            response = remote_target.recv(1024).decode()
            print(response)
        except KeyboardInterrupt:
            # close out 
            remote_target.close()
            break
    
    




# socket.AF_INET = IPV4 address family used in sockets where we will be referring
# to socket connections through a host IP and port address scheme (AF_INET6 would refer to IPV6)

# SOCK_STREAM = communication channel that allows communications to occur from one point to another
#       Until that communication is terminated
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_ip = '127.0.0.1'
host_port = 2222

# call listener handler
listener_handler()


#send_message = 'Hello world !'.encode()
#remote_target.send(send_message)
#remote_target.recv(1024).decode()




