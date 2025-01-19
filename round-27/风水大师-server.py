#!/usr/bin/env python3

'''
A mock webserver using C memory functions reimplemented in Python.

All "C" functions should be approximately equivalent to the C stdlib,
with malloc being the equivalent of mmap.

The server takes requests in the following form:

GET /url_to_visit
Header1: Value1
Header2: Value2
...

Enter a blank line to send the request.
'''

from random import randint, choice

mem = [0]*2**16
free_space = [(0, 2**16 - 1)]
sizes = {}

### Heap helper functions ###

def coalesce(): # coalesce adjacent free memory regions into one region
    global free_space
    free_space = sorted(free_space, key=lambda x:x[0])
    for i in range(len(free_space)-1, 0, -1):
        if free_space[i][0] == free_space[i-1][1]:
            free_space[i-1] = free_space[i-1][0], free_space[i][1]
            free_space.pop(i)

def remove_empty(): # remove chunks of free memory that are size 0
    global free_space
    for i in range(len(free_space)-1, -1, -1):
        if free_space[i][0] >= free_space[i][1]:
            free_space.pop(i)

def is_mapped(ptr): # checks if a ptr has been allocated and is allowed to be written to
    for addr in sizes:
        if addr <= ptr < addr+sizes[addr]:
            return True
    return False

### C stdlib functions ###

def malloc(n):
    if n <= 0:
        return 0
    for i, pair in reversed(list(enumerate(free_space))):
        start, end = pair
        if end-start > n:
            sizes[end-n] = n
            free_space[i] = (start, end-n)
            coalesce()
            remove_empty()
            return end-n
    print("Out of space!")
    print("You're probably doing something horribly wrong.")
    return 0

def free(ptr):
    global free_space, sizes
    free_space.append((ptr, ptr+sizes[ptr]))
    del sizes[ptr]
    coalesce()
    remove_empty()

def realloc(ptr, size):
    global free_space, sizes
    cur_size = sizes[ptr]
    if size <= cur_size:
        return ptr
    size_diff = size - cur_size
    for i, pair in enumerate(free_space):
        if pair[0] == ptr + cur_size and pair[1] >= ptr + size:
            sizes[ptr] = size
            free_space[i] = pair[0]+size_diff, pair[1]
            coalesce()
            remove_empty()
            return ptr
    newptr = malloc(size)
    write(newptr, read(ptr))
    free(ptr)
    return newptr

def read(ptr):
    return mem[ptr:ptr+sizes[ptr]]

def read_str(ptr): # read memory as a string, not as a list of numbers
    return ''.join(chr(i) for i in mem[ptr:ptr+sizes[ptr]]).split('\x00')[0]

def write(ptr, data):
    if ptr == 0:
        return 0
    for i, c in enumerate(data):
        if not is_mapped(ptr+i):
            print(ptr, data)
            print("Attempting to write to unallocated memory!")
            exit()
        if type(c) == str:
            c = ord(c)
        mem[ptr+i] = c

def zero(ptr): # set a malloc'd region to all zeroes
    write(ptr, [0]*sizes[ptr])

def strlen(inp):
    for i, c in enumerate(inp):
        if c == '\x00':
            return i
    return len(inp)

def print_heap(): # for debugging
    sorted_sizes = sorted([(i,sizes[i]) for i in sizes], key=lambda x:x[0])
    print()
    print("="*80)
    for ptr, sz in sorted_sizes:
        print(f"{ '{:5d}'.format(sz)} bytes mapped from {hex(ptr)} - {hex(ptr+sz)}")
    print("="*80)
    print()

### "webserver" functions ###

def process_request():
    ret = f'You are visiting {read_str(url)}.\n\n'
    user = read_header("User")
    ret += f"Current user is {user}.\n\n"
    if read_str(url) == "/flag":
        if user == 'admin':
            ret += f"User is admin. Congrats! {open('flag.txt').read()}\n"
        else:
            ret += "User is not admin!\n"
    return ret

def print_headers(): # for debugging
    curr = header_dict
    while True:
        curr_data = read(curr)
        if curr_data[0] == 0:
            return
        print(f"{read_str(curr_data[0])}: {read_str(curr_data[1])}")
        curr = curr_data[2]

def read_header(header):
    curr = header_dict    
    while True:
        curr_data = read(curr)

        if curr_data[0] == 0:
            print("Attempted to read header value that doesn't exist!")
            exit()

        if read_str(curr_data[0]) == header:
            return read_str(curr_data[1])

        curr = curr_data[2]

def store_header(header, val):
    if val.startswith("admin"):
        print("Hacking detected!")
        exit()

    curr = header_dict    
    while True:
        curr_data = read(curr)

        if curr_data[0] == 0:
            new_entry = malloc(3)
            write(new_entry, [0, 0, 0])

            header_mem = malloc(strlen(header))
            write(header_mem, header)

            val_mem = malloc(strlen(val))
            write(val_mem, val)

            write(curr, [header_mem, val_mem, new_entry])
            return

        if read_str(curr_data[0]) == header:
            new_val = realloc(curr_data[1], strlen(val))
            zero(new_val)
            write(new_val, val)
            write(curr, [curr_data[0], new_val, curr_data[2]])
            return

        curr = curr_data[2]

def store_url(new_url):
    global url
    url = realloc(url, strlen(new_url))
    zero(url)
    write(url, new_url)

def gen_word(n):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return ''.join(choice(alphabet) for i in range(n))

def randomize_heap(): # simulating many previous requests
    headers = [gen_word(randint(10, 100)) for i in range(100)]
    for i in range(100):
        store_url(gen_word(randint(1, 100)))
        for i in range(randint(1, 10)):
            store_header(choice(headers), gen_word(randint(1, 100)))
        store_header("User", gen_word(randint(1, 20)))

def main():
    while True:
        print("Enter web request below:")
        req_line = input().strip().split()
        if len(req_line) < 2:
            print("Invalid format!")
            continue
        if req_line[0] != 'GET':
            print("Only get requests allowed!")
            continue
        store_url(req_line[1])
        
        header_line = input()
        while header_line != '':
            if len(header_line) > 100:
                print("Header too long!")
                exit()
            header, val, *_ = header_line.split(': ')
            store_header(header, val)
            header_line = input()

        print("Server response:")
        print(process_request())

if __name__ == '__main__':
    print("Getting things set up...")
    url = malloc(4)
    header_dict = malloc(3)
    write(header_dict, [0, 0, 0])

    randomize_heap()
    main()
