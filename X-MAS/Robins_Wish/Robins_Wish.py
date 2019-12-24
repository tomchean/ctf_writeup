from pwn import *
import gmpy2
import sympy

r = remote('challs.xmas.htsp.ro', 10005)
menu = r.recv()
menu = menu.decode()
#print(menu)

r.sendline('1337')
cipher = r.recvline()
cipher = int(cipher.decode().split(' ')[-1])
#cipher = 5246714854725113346502630730554686769362460460024400516326377174582640581617340710826138679480295436331234207963461529282935208997428624889011546696260124285562972903578214766887742626982299066940742233276099045101758754159876941858460523496511762589246629169421146451313958152520373812386003438537883174073207043740529956867073333127369639805390764236392611481831378501794578225519437884851468056175989860754859991595520574160634748280117377466913600749771441057921368040518728100659821105472644679642632075853735222383344108215588801856832216683298621306263529594333455011123877122301231151688000552994875142333423
r.recv()

high = gmpy2.mpz(10**309)
low = gmpy2.mpz(10**308)
while high > low:
    mid = (high+low) // 2
    r.sendline('2')
    r.recv()
    r.sendline(str(mid))
    tmp = r.recvline()
    r.recv()

    tmp = tmp.decode()
    tmp = tmp.split(' ')
    encypt = int(tmp[-1])

    if gmpy2.square(mid) == encypt:
        low = mid
    else:
        high = mid
    
    n = mid

print('cipher: ', cipher)
print('n: ', n)

r.close()