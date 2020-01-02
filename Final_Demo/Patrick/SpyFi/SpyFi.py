from pwn import *
import socket
import string
import re
from multiprocessing.pool import ThreadPool
charset = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ '
def attempt(tag, payload, block_number=0):
    s = remote('2018shell.picoctf.com', 33893)
    # retrieve char
    while True:
        data = s.recv(4096)
        data = data.decode()
        if not data:
            continue
        if 'Welcome, Agent 006!' in data:
            pass
        elif 'Please enter your situation report:' in data:
            s.sendline(payload.encode())
        else:
            s.close()
            return (tag, data[block_number * 32 : block_number * 32 + 32])
def main(progress='', block_number=0):
    # My agent identifying code is: 
    block = 'A' * 16
    assert len(block) == 16
    for skip in range(16):
        padding = "x" * (96-53-31)
        prefix = padding + block[skip+1:]
        _, aim = attempt('', prefix, block_number)
        pool = ThreadPool(processes=10)
        async_results = []
        # Then enter 16 characters changing the last one until you get the
        # same result as with 15 characters for the first 16 encoded bytes
        for ch in charset:
            # dummy to duplicate the uncontrolled blocks
            # 96 bytes rounded up from 84 bytes provided
            dummy = '\nMy agent identifying code is: '.replace('\n', 'n') # server can't receive newline
            payload = prefix + dummy + progress + ch
            async_result = pool.apply_async(attempt, (ch, payload, block_number))
            async_results.append(async_result)
        # That 16th character is the first character of your secret. 
        # You can then repeat the process by putting 14 characters and then
        # finding the second secret characters with the same thechnique.
        for async_result in async_results:
            ch, result = async_result.get()
            if result == aim:
                progress += ch
                if ch == '}':
                    print(f"Success! {progress}")
                    quit()
                break

        print(f"Progress (Block {block_number} of index {skip}): {progress}")
    main(progress, block_number + 1)

if __name__ == '__main__':
    # choose the block_number, progress, and skip in appropriate value
    # ex: if already run picoCTF{@g3nt6_1$
    # set block_number=7, progress='picoCTF{@g3nt6_1$', and skip start with range(1, 16)
    main(block_number=6)
    flag = 'picoCTF{@g3nt6_1$_th3_c00l3$t_6081670}'