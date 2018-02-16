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
$ python rsa.py -s <script> -o <os>
```

To generate shell command with your ip:port provided: 
```
$ python rsa.py -s <script> -o <os> -i <ip> -p <port>
```

### Ideas/Coming soon

* Local TTY shell upgrades.

### License

MIT License

> Copyright (c) 2018 Alexander Kravchenko < iqxtech@gmail.com >
>
> Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
>
> The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
>
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.