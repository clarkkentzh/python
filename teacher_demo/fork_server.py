#!/usr/bin/python

import socket,traceback,os,sys

def reap():
    while True:
        try:
            result = os.waitpid(-1,os.WNOHANG)
            if not result[0]:break
        except:
            break
        print('Reaped child process %d'%result[0])

host = ''
port = 8888

s = socket.socket()
s.bind((host,port))
s.listen(5)

print('Parent at %d listening for connections'%os.getpid())

while True:
    try:
        c,addr = s.accept()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
        continue
    reap()

    pid = os.fork()

    if pid:
        c.close()
        continue
    else:
        s.close()

        try:
            print("Child from %s being hanled PID %d"%(c.getpeername(),os.getpid()))

            while True:
                data = c.recv(1024).decode()
                if not len(data):
                    break;
                print(data)
                c.send('recv your message'.encode())
        except (KeyboardInterrupt,SystemExit):
            raise
        except:
            traceback.print_exc()
        c.close()
        sys.exit(0)
