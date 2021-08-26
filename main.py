import socket
import os
import sys
from time import sleep as timeout
import time
os.system('clear')


def ahmed () :
    print('___author___:Ahmed mowafy')
    print(' ')
    print('\033[1;31m                                          To Close "exit" ')
    print('\033[1;31m ')

    os.system('figlet D a r k')
    os.system('figlet P h a n t o m')
    print(' ')
    print(' ')
    print('\033[1;31mEnter your ("DNS") or target ')
    print(' ')
    host=input('>>>:')
    if host != 'exit':
        ip=socket.gethostbyname(host)
        print('thehost name:'+host)
        print('\033[1;33mtarget ip is:'+ip)
        time.sleep(9)
        os.system('clear')
        ahmed ()
    elif host=='exit':
        os.system('clear')


ahmed ()
