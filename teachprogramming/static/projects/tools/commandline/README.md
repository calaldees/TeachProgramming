CommandLine Exercises
=====================

bash, terminal, command line, commandline, shell


* https://github.com/onceupon/Bash-Oneliner

xargs in general https://stackoverflow.com/questions/35589179/when-to-use-xargs-when-piping

find | xargs
get cookie from browser - export use in `curl`
curl | jq
curl | htmlq
| grep
| unique

alias

function

netcat
diff
gzip
rsa??

Print the first line of each file in a folder

SQL dump strip inserts to table with grep



```bash
# see http headers with `nc`
nc -l 8000
open http://localhost:8000/MyRequest?id=test
```

Nc as a chat tool!
```
# From server A:
$ sudo nc -l 80
# then you can connect to the 80 port from another server (e.g. server B):
# e.g. telnet <server A IP address> 80
# then type something in server B
# and you will see the result in server A!
```
```bash
# `nc -u` is NOT pure udp - there is a protocol happening under the hood - can't really be used for inspecting pure udp
# for tcp `nc` seems to be fine?
# https://help.ubidots.com/en/articles/937233-sending-tcp-udp-packets-using-netcat
nc -u -l 5005
nc -u 127.0.0.1 5005
  #<type stuff>
netstat | 5005  # does not work on my mac - can't see it
```

```bash
# fine for sending - can't recv this way
echo "hello3" > /dev/udp/127.0.0.1/5005

```

netcat


forward x11


diff files and apply

append

read file into variable


magic mime


convert pdf to text
xls to csv

pandoc in docker alias
ffmpeg in docker alias

screen for multiprocess

Project Ideas?
=======

pipe into pyhton program with std.in and output to std.out via netcat to another location

Video encoding?

SSL from commandline?

rsa key encode/decode?