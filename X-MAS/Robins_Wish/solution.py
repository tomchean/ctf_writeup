import sympy
import gmpy2

def decryption(a, p, q):
    n = p * q
    r, s = 0, 0
    # find sqrt
    # for p
    if p % 4 == 3:
        r = sqrt_p_3_mod_4(a, p)
    elif p % 8 == 5:
        r = sqrt_p_5_mod_8(a, p)
    # for q
    if q % 4 == 3:
        s = sqrt_p_3_mod_4(a, q)
    elif q % 8 == 5:
        s = sqrt_p_5_mod_8(a, q)

    gcd, c, d = egcd(p, q)
    x = (r * d * q + s * c * p) % n
    y = (r * d * q - s * c * p) % n
    lst = [x, n - x, y, n - y]
    plaintext = choose(lst)
    string = bin(plaintext)
    string = string[:-16]
    plaintext = int(string, 2)

    return plaintext


# decide which answer to choose
def choose(lst):
    for i in lst:
        binary = bin(i)
        append = binary[-16:]   # take the last 16 bits
        binary = binary[:-16]   # remove the last 16 bits
        if append == binary[-16:]:
            return i
    return

# Find SQROOT in Zp where p = 3 mod 4
def sqrt_p_3_mod_4(a, p):
    r = pow(a, (p + 1) // 4, p)
    return r

# Find SQROOT in Zp where p = 5 mod 8
def sqrt_p_5_mod_8(a, p):
    d = pow(a, (p - 1) // 4, p)
    r =0
    if d == 1:
        r = pow(a, (p + 3) // 8, p)
    elif d == p - 1:
        r = 2 * a * pow(4 * a, (p - 5) // 8, p) % p

    return r

def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, y, x = egcd(b % a, a)
        return gcd, x - (b // a) * y, y

cipher = 5246714854725113346502630730554686769362460460024400516326377174582640581617340710826138679480295436331234207963461529282935208997428624889011546696260124285562972903578214766887742626982299066940742233276099045101758754159876941858460523496511762589246629169421146451313958152520373812386003438537883174073207043740529956867073333127369639805390764236392611481831378501794578225519437884851468056175989860754859991595520574160634748280117377466913600749771441057921368040518728100659821105472644679642632075853735222383344108215588801856832216683298621306263529594333455011123877122301231151688000552994875142333423
n = 17150948086006853589591993610767711903029749167719666894975279147137565458158322238156960171902445590052801235253045792984069360111140927413022122124794074712372666903008787076313652986830735891457266804676322092444602549744787142273336096470832931113698218899620404912992099097015038863714351384075897287966440984446042594077540591489657561322101444523900312965276873402643875552954061610698504308548301539759131150366661281651087532807818489741520557925049746199503634928208501195328273501508911193754334803125090416259379171809642283452935819219835361791073290320084884025929676790915171638558685021113076310785793
factors = sympy.factor(n)
factor = []
for i,j in factors.items():
    factor.append(i)
p = factor[0]
q = factor[1]
plaintext = decryption(cipher, p, q)
plaintext = str(hex(plaintext))[2:]
plaintext = bytearray.fromhex(plaintext).decode()
print(plaintext)