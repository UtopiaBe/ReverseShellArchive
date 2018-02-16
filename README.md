# ReverseShellArchive

Reverse Shell Archive is a handy tool to quickly generate needed reverse shell, one line script, or to upgrade your shell to fully interactive TTY.

Supported reverse shell commands:
- Bash, PHP, Perl, Python, Ruby, Netcat, Telnet

## Usage:

    Usage: rsa.py [options]

    Basic usage: rsa.py -s <script> -o <os.
        Will create Script without given ip and port address.

    Advanced usage: rsa.py -s [script] -o [os] -i [ip] -p [port]
        Will create Script with given ip and port address.

    Help: rsa.py -h [help] --help [help]


    Options:
      -h, --help            show this help message and exit
      -s SCRIPT, --script=SCRIPT
                            bash, php, perl, python, Ruby, netcat, telnet
      -o OS, --os=OS        l/linux, w/windows
      -i HOST, --ip=HOST    Your listening ip address (optional)
      -p PORT, --port=PORT  Your listening port address (optional)

## Example

![Reverse Shell Archive](https://github.com/UtopiaBe/ReverseShellArchive/lib/reverseshellsarchive.gif

Basic reverse shell command generator:
```
python rsa.py -s <script> -o <os>
```

To generate shell command with your ip:port provided: 
```
python rsa.py -s <script> -o <os> -i <ip> -p <port>
```

### Ideas/Coming soon

* Local TTY shell upgrades.

### License