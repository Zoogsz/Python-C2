import socket
import sys



def listener_handler():
    # bind to local address
    sock.bind((host_ip, host_port))
    print('[+] Its so quiet')
    sock.listen()
    remote_target, remote_ip = sock.accept()
    comm_handler(remote_target, remote_ip)
    
    
def comm_handler(remote_target, remote_ip):
    print(f'[+] Connection received from {remote_ip}')
    while True:
        try:
            message = input('Message to send#> ')
            #exit message handling
            if message == 'exit':
                remote_target.send(message.encode())
                remote_target.close()
                break
            # remember that we need to convert the string value of message to bytes using .encode()
            remote_target.send(message.encode())
            response = remote_target.recv(1024).decode()
            print(response)
        except KeyboardInterrupt:
            # close out 
            print("[-] Keyboard interrupt issued")
            message = 'Exiting due to keyboard interrupt'
            remote_target.send(message.encode())
            sock.close()
            break
        except Exception as fail:
            print(f"[-] Closing ... Exception caught {fail}")
            sock.close()
            break
    


def comm_in(remote_target):
    print('[+] Awaiting response...')
    response = remote_target.recv(1024).decode()
    return response

def comm_out(remote_target, message):
    remote_target.send(message.encode())

################
# main function
################

if __name__ == '__main__':

    ##############################
    # socket.AF_INET = IPV4 address family used in sockets where we will be referring
    # to socket connections through a host IP and port address scheme (AF_INET6 would refer to IPV6)

    # SOCK_STREAM = communication channel that allows communications to occur from one point to another
    #       Until that communication is terminated
    ##############################

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        host_ip = sys.argv[1]
        host_port = int(sys.argv[2])
        # call listener handler
        listener_handler()
    except IndexError: 
        print('[-] Command line argument(s) missing. Please try again.')
    except Exception as fail:
            print(f"[-] Closing ... Exception caught {fail}")
            sock.close()
