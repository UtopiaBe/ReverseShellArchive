#!/usr/bin/python

import re


def validateHost(ip, port, parser):
    # Check for correct Port address.
    # up to (65535).
    port_pattern = re.compile(
        "^0*(?:6553[0-5]|655[0-2]\d|65[0-4]\d{2}|6[0-4]\d{3}|[1-5]\d{4}|[1-9]\d{1,3}|\d)$")
    check_port = port_pattern.match(port)
    # Check for correct IP address.
    # up to (255.255.255.254).
    ip_pattern = re.compile("^((25[0-4]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(25[0-4]|2[0-4][0-9]|[01]?[0-9][0-9]?)$")
    check_ip = ip_pattern.match(ip)
    if not check_ip and not check_port:
        parser.error("unacceptable [ip] argument provided\n\t\t"
                     "please provide correct -i [ip] or --ip=[ip] argument, [254.254.254.254]\n\t\t"
                     "unacceptable [port] argument provided\n\t\t"
                     "please provide correct -p [port] or --port=[port] argument, [1-65535]")
    elif not check_ip:
        parser.error("unacceptable [ip] argument provided\n\t\t"
                     "please provide correct -i [ip] or --ip=[ip] argument, [254.254.254.254]")
    elif not check_port:
        parser.error("unacceptable [port] argument provided\n\t\t"
                     "please provide correct -p [port] or --port=[port] argument, [1-65535]")


# Validate [script] argument.
def validateScript(script):
    if script == "bash" or script == "php" \
            or script == "perl" or script == "python" \
            or script == "ruby" or script == "netcat" \
            or script == "telnet":  # or script == "xterm":
        pass
    elif script is None:
        script = ""
    else:
        script = 13
    return script


# Validate [os] argument.
def validateOs(os):
    if os == "w" or os == "windows" \
            or os == "l" or os == "linux":
        pass
    elif os is None:
        os = ""
    else:
        os = 13
    return os
