# ReverseShellArchive

Reverse Shell Archive is a handy tool to quickly get needed reverse shell script, and to upgrade shells to fully interactive TTYs.

Supported scripts:
- Bash, PHP, Perl, Python, Ruby, Netcat, Telnet

## Usage:

    Usage: reverseshells.py [options]

    Basic usage: everseshells.py -s <script> -o <os.
        Will create Script without given ip and port address.

    Advanced usage: everseshells.py -s [script] -o [os] -i [ip] -p [port]
        Will create Script with given ip and port address.

    Help: everseshells.py -h [help] --help [help]


    Options:
      -h, --help            show this help message and exit
      -s SCRIPT, --script=SCRIPT
                            bash, php, perl, python, Ruby, netcat, telnet
      -o OS, --os=OS        l/linux, w/windows
      -i HOST, --ip=HOST    Your listening ip address (optional)
      -p PORT, --port=PORT  Your listening port address (optional)

## Example

![Reverse Shell Archive](https://github.com/UtopiaBe/ReverseShellArchive/lib/reverseshellsarchive.gif

Basic Reverse Shell script:
```
python reverseshells.py -s <script> -o <os>
```

To receive script with your <ip>:<port>: 

```
python reverseshells.py -s <script> -o <os> -i <ip> -p <port>
```

After that just copy the generated script, and good luck in receiving reverse shell.


### Vulnerable environment

To simulate this attack you can use a vulnerable docker image. If you have docker installed, just run

```
docker run --rm -it \
       -p 137-139:137-139 \
       -p 445:445 -p 6699:6699 \
       vulnerables/cve-2017-7494
```

If you want to access, use the following credentials.

* User: `sambacry`
* Password: `nosambanocry`



### Alternative payloads

You can find one example of binding shell payload for this exploit in `bindshell-samba.c` file. Change it as you may find necessary. After that to generate a new binary, use:

```
gcc -c -fpic bindshell-samba.c
gcc -shared -o libbindshell-samba.so bindshell-samba.o
```

### Afftected software

Samba 3.x after 3.5.0 and 4.x before 4.4.14, 4.5.x before 4.5.10, and 4.6.x before 4.6.4

### Mitigation

Add the parameter:

```
nt pipe support = no
```

to the `[global]` section of your smb.conf and restart smbd. This prevents clients from accessing any named pipe endpoints. Note this can disable some expected functionality for Windows clients.

Also consider mounting the filesystem which is used by samba for its writable share using `noexec` option.

### Disclaimer

This or previous program is for Educational purpose ONLY. Do not use it without permission. The usual disclaimer applies, especially the fact that me (opsxcq) is not liable for any damages caused by direct or indirect use of the information or functionality provided by these programs. The author or any Internet provider bears NO responsibility for content or misuse of these programs or any derivatives thereof. By using these programs you accept the fact that any damage (dataloss, system crash, system compromise, etc.) caused by the use of these programs is not opsxcq's responsibility.
