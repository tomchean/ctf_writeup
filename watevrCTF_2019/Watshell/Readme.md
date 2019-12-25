# Solution

```
$ nc 13.48.42.211 50000
Welcome to watshell, we ofcourse use our own super secure cryptographic functions to ensure user privacy!
Command:
```

We can give up to 0x20 values to the program. It calculates the following formula for each value:
```
output = pow(input, 113, 143)
```
So you can find that d = 113 and n = 143.

The server wants us to enter the encrypted message of "give_me_the_flag_please"
```
import gmpy2
import sympy

n = 143
d = 113
def totient(n):
    factors = sympy.factorint(n)
    phi = 1
    for i,j in factors.items():
        phi *= (pow(i,j) - pow(i,j-1))
    return phi
phi = totient(n)
e = gmpy2.invert(d, phi)

plaintext = b'give_me_the_flag_please'
cipher= []
for c in plain:
    cipher.append(pow(c, e, p*q))
print(cipher)
```

Get the encrypted message and send it to the server
```
$ nc 13.48.42.211 50000
Welcome to watshell, we ofcourse use our own super secure cryptographic functions to ensure user privacy!
Command: 38 118 79 95 127 109 95 127 129 91 95 127 20 114 15 38 127 73 114 95 15 124 95
Alright, alright watevr{oops_1_f0rg0t_to_use_r4ndom_k3ys!_youtube.com/watch?v=BaACrT6Ydik}
```

Get the Flag:

**watevr{oops_1_f0rg0t_to_use_r4ndom_k3ys!_youtube.com/watch?v=BaACrT6Ydik}**
