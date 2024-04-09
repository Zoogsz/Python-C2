import socket

def session_handler():
    print(f'[+] Connecting to {host_ip}.')
    sock.connect((host_ip, host_port))
    print(f'[+] Connected to {host_ip}.')
    
    
    while True:
        try:
            #decode encoded message
            print("[+] Awaiting Response from server #>")
            message = sock.recv(1024).decode()
            print(message)
            response = input('Message to send#> ')
            sock.send(response.encode())
        except Exception:
            sock.close()
            break

# socket.AF_INET = IPV4 address family used in sockets where we will be referring
# to socket connections through a host IP and port address scheme (AF_INET6 would refer to IPV6)

# SOCK_STREAM = communication channel that allows communications to occur from one point to another
#       Until that communication is terminated
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host_ip = '127.0.0.1'
host_port = 2222

# call session_handler
session_handler()
