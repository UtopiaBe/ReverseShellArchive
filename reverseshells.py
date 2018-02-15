#!/usr/bin/python

from optparse import OptionParser
from core.scripts import *
from core.validators import *
from core.colors import COLORS


def banner():
    print """
 _____                                  _____ _          _ _     
|  __ \                                / ____| |        | | |      /\            | |   (_)          
| |__) |_____   _____ _ __ ___  ___   | (___ | |__   ___| | |     /  \   _ __ ___| |__  ___   _____ 
|  _  // _ \ \ / / _ \ '__/ __|/ _ \   \___ \| '_ \ / _ \ | |    / /\ \ | '__/ __| '_ \| \ \ / / _ \ 
| | \ \  __/\ V /  __/ |  \__ \  __/   ____) | | | |  __/ | |   / ____ \| | | (__| | | | |\ V /  __/
|_|  \_\___| \_/ \___|_|  |___/\___|  |_____/|_| |_|\___|_|_|  /_/    \_\_|  \___|_| |_|_| \_/ \___|
                                                                                               
----[ Version: 0.1                                     Author: Alexander Kravchenko <UtopiaBe> ]----
----[ Web: https://csi-blog.com                        GitHub: https://GitHub.com/             ]----
 --------------------------------------------------------------------------------------------------
| (1) Reverse Shell One Liners:                                                                    |
| BASH, PHP, PERL, PYTHON, RUBY, NETCAT, TELNET                                                    |                             
| (2) How to check which Script will work on linux?:                                               |
| user@linux:~ which [bash/php/perl/python/ruby/netcat/telnet]                                     |
| Answer needed: /usr/bin/[script]                                                                 |
| (3) Don't forget to open correct listener on YOUR attacking machine, such as: nc -nvlp PORT      |  
| (4) Author assume no liability and not responsible for any  damage caused by this program.       |
 --------------------------------------------------------------------------------------------------
    """


def main():
    # Print banner at the start.
    banner()

    # Begin with parses.
    parser = OptionParser()

    # Usage custom message.
    parser.usage = "%prog [options]\n" \
                   "\nBasic usage: %prog -s [script] -o [os]\n" \
                   "\tWill create Script without given ip and port address.\n\n" \
                   "Advanced usage: %prog -s [script] -o [os] -i [ip] -p [port]\n" \
                   "\tWill create Script with given ip and port address.\n\n" \
                   "Help: %prog -h [help] --help [help]\n"

    # Set the script options.
    parser.add_option("-s", "--script", type="str",
                      help="bash, php, perl, python, Ruby, netcat, telnet",
                      dest="script")

    parser.add_option("-o", "--os", type="str",
                      help="l/linux, w/windows",
                      dest="os")

    parser.add_option("-i", "--ip", type="str", default=False,
                      help="Your listening ip address (optional)",
                      dest="host")

    parser.add_option("-p", "--port", type="str", default=False,
                      help="Your listening port address (optional)",
                      dest="port")

    (options, args) = parser.parse_args()

    # OS string fix to Uppercase
    os = ""
    if options.os == "w" or options.os == "windows":
        os = "Windows"
    elif options.os == "l" or options.os == "linux":
        os = "Linux"

    # If good [script] and [os] arguments provided:
    if validateScript(options.script) != 13 and validateScript(options.script) != "" \
            and validateOs(options.os) != 13 and validateOs(options.os) != "" and not options.host and not options.port:
        msg = COLORS.bg.green + "[+]" + COLORS.reset + " Making '%s' reverse shell for '%s'.\n" \
              % (options.script, os) + \
              COLORS.bg.red + "[-]" + COLORS.reset + "Advanced: Please remember to change \"ATTACKING-IP\" and PORT!"
        createShell(options.script, options.os, None, None, msg)
        exit(0)

    # If all good arguments provided:
    if validateScript(options.script) and validateOs(options.os) and options.host and options.port:
        validateHost(options.host, options.port, parser)
        if options.os == "w" or options.os == "windows":
            os = "Windows"
        elif options.os == "l" or options.os == "linux":
            os = "Linux"
        # If IP and PORT are acceptable.
        msg = COLORS.bg.green + "[+]" + COLORS.reset + " Making '%s' reverse shell for '%s'.\n" \
              % (options.script, os) + \
              COLORS.bg.green + "[+]" + COLORS.reset + " Advanced: will open reverse shell to: %s:%s." \
              % (options.host, options.port)
        createShell(options.script, options.os, options.host, options.port, msg)
        exit(0)

    """
    # Basic:
    # If bad [script] and [os] arguments provided, or missing.
    """

    # If bad [script] and bad [os] arguments provided:
    if validateScript(options.script) == 13 and validateOs(options.os) == 13:
        parser.error("both arguments are wrong\n\t\t"
                     "please provide correct arguments")

    # If bad [script] and empty [os] arguments provided:
    if validateScript(options.script) == 13 and validateOs(options.os) == "":
        parser.error("unacceptable [script] argument provided\n\t\t"
                     "please provide correct -s [script] or --script=[script] argument\n\t\t"
                     "missing -o [os] or --os=[os] argument")

    # If empty [script] and bad [os] arguments provided:
    if validateScript(options.script) == "" and validateOs(options.os) == 13:
        parser.error("unacceptable [os] argument provided\n\t\t"
                     "please provide correct -o [os] or --os=[os] argument\n\t\t"
                     "missing -s [script] or --script=[script] argument")

    # If empty [script] and good [os] arguments provided:
    if validateScript(options.script) == "" and validateOs(options.os):
        parser.error("good [os] argument provided\n\t\t"
                     "missing -s [script] or --script=[script] argument")

    # If good [script] and bad [os] arguments provided:
    if validateScript(options.script) and validateOs(options.os) == 13:
        parser.error("good [script] argument provided\n\t\t"
                     "unacceptable [os] argument provided\n\t\t"
                     "please provide correct -o [os] or --os=[os] argument")

    # If bad [script] and good [os] arguments provided:
    if validateScript(options.script) == 13 and validateOs(options.os):
        parser.error("good [os] argument provided\n\t\t"
                     "unacceptable [script] argument provided\n\t\t"
                     "please provide correct -s [script] or --script=[script] argument")

    # If good [script] and empty [os] arguments provided:
    if validateScript(options.script) and validateOs(options.os) == "":
        parser.error("good [script] argument provided\n\t\t"""
                     "missing -o [os] or --os=[os] argument")

    # If no arguments provided:
    if not options.script and not options.os:
        parser.error("no arguments were given")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print "Keyboard Interrupt: exiting."
