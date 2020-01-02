<h2>PicoCTF18 (SpyFi ,300 pt)</h2>

In this challange they use AES-ECB mode which we know it is quite vulnerable.

If you dont know how AES-ECB works i would suggest to read about first.
[AES-ECB](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Electronic_Codebook_(ECB))

**AES-ECB Encryption and Decryption flow chart**


![alt text](https://github.com/saurabh589/ctf-2018/blob/master/picoctf18/scify/601px-ECB_encryption.svg.png)


![alt text](https://github.com/saurabh589/ctf-2018/blob/master/picoctf18/scify/601px-ECB_decryption.svg.png)

**Now come to the challange**

```python
#!/usr/bin/python2 -u
from Crypto.Cipher import AES

agent_code = """flag"""

def pad(message):
    if len(message) % 16 != 0:
        message = message + '0'*(16 - len(message)%16 )    #block-size = 16
    return message

def encrypt(key, plain):
    cipher = AES.new( key.decode('hex'), AES.MODE_ECB )
    return cipher.encrypt(plain).encode('hex')

welcome = "Welcome, Agent 006!"
print welcome

sitrep = raw_input("Please enter your situation report: ")
message = '''Agent,
Greetings. My situation report is as follows:
{0}                                                     #here is our input message
My agent identifying code is: {1}.                      #flag
Down with the Soviets,
006'''.format(sitrep,agent_code)

message = pad(message)
print encrypt( """key""", message )
```


lets send input message : 
``` AAAAAAAAAAA + BBBBBBBBBBBBBBBB + CCCCCCCCCCCCCCCC  <--   'A'x11 (offset) + 'B'x16 + 'C'x16```

suppose flag is : ```picoCTF{ABCDEFG}```

**Divide message in blocks of 16**

    ```
       'Agent,\nGreetings' <--- 16  (Block 1)
       '. My situation r'  <--- 16  (Block 2)
       'eport is as foll'  <--- 16  (Block 3)
       'ows:\nAAAAAAAAAAA' <--- 16  (Block 4)
       'BBBBBBBBBBBBBBBB'  <--- 16  (Block 5)
       'CCCCCCCCCCCCCCCC'  <--- 16  (Block 6)
       '\nMy agent identi' <--- 16  (Block 7)
       'fying code is:  '  <--- 16  (Block 8)  <---known Block
       'picoCTF{ABCDEFG}'  <--- 16  (Block 9)  <---unknown Block
       '.Down with the S'  <--- 16  (Block 10) <---known Block
    ```
Now if we send input with one less 'C' then blocks is:


    ```
       'Agent,\nGreetings'   <--- 16  (Block 1)
       '. My situation r'    <--- 16  (Block 2)
       'eport is as foll'    <--- 16  (Block 3)
       'ows:\nAAAAAAAAAAA'   <--- 16  (Block 4)
       'BBBBBBBBBBBBBBBB'    <--- 16  (Block 5)
       'CCCCCCCCCCCCCCC\n'   <--- 16  (Block 6)
       'My agent identif'    <--- 16  (Block 7)
       'ying code is:  p'    <--- 16  (Block 8)    <-- Now we know block 8 has our one byte flag but it is encrypted we dont know what the char is.
       'icoCTF{ABCDEFG}.'    <--- 16  (Block 9)    <---unknown block 
       'Down with the So'    <--- 16  (Block 10)   <---known Block
    ```

**Now we know the encryption of block 8 in which last byte is our flag's first byte, to know what byte is we send input like this**


    ```
       'Agent,\nGreetings'    <--- 16  (Block 1)
       '. My situation r'     <--- 16  (Block 2)
       'eport is as foll'     <--- 16  (Block 3)
       'ows:\nAAAAAAAAAAA'    <--- 16  (Block 4)
       'ying code is:  %s'    <--- 16  (Block 5)    <--- replace %s to char in range(32,128)   
       'CCCCCCCCCCCCCCC\n'    <--- 16  (Block 6)
       'My agent identif'     <--- 16  (Block 7)
       'ying code is:  p'     <--- 16  (Block 8)    <--- Now we know block 8 has our one byte flag
       'icoCTF{ABCDEFG}.'     <--- 16  (Block 9)    <--- unknown block 
       'Down with the So'     <--- 16  (Block 10)   <---known Block
    ```

**What we have to do is to check the encryption of block 5 and block 8 over the loop if it is same means the char we send is our first char of flag!! Whooho...!! we just get the 1st byte of unknown block without knowing key, lets repeat again same method with 2 'C' less.**
 
 after 1st loop we know flag starting with  : "p"
 
 **Now for second byte send input like this**
 
 
    ```
       'Agent,\nGreetings'    <--- 16  (Block 1)
       '. My situation r'     <--- 16  (Block 2)
       'eport is as foll'     <--- 16  (Block 3)
       'ows:\nAAAAAAAAAAA'    <--- 16  (Block 4)
       'ing code is: p%s'     <--- 16  (Block 5)    <--- replace %s to char in range(32,128)   
       'CCCCCCCCCCCCCC\nM'    <--- 16  (Block 6)
       'y agent identify'     <--- 16  (Block 7)
       'ing code is:  pi'     <--- 16  (Block 8)    <--- Now we know block 8 has our two byte flag in which one we know i.e "p" and other we have to find out in second loop.
       'coCTF{ABCDEFG}.D'     <--- 16  (Block 9)    <--- unknown block 
       'own with the Sov'     <--- 16  (Block 10)   <--- known Block
    ```
 
 **Repeat process again check encryption of block 5 and block 8 if it same means the second char we send is our flag's second char..!!**
 
 after 2nd loop we know flag starting with : "pi"
 
 **Same process we have to do until we get full flag!!!**
 
 **My Script for this challenge**
 
 ```python
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
            
```
