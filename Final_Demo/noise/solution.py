from os import urandom

def getrandbits(bit):
    return int.from_bytes(urandom(bit>>3), 'big')

secret = getrandbits(1024) # 128 bytes
noise = getrandbits(1000)

answer = 0
times = 0

_min = 0
_max = (1 << 1)
i = _min
while True:
    times += 1
    num = int(i << 1023) + answer
    ans = (num + noise) % secret
    if len(bin(ans)) == len(bin(num+noise)):
        _min = i
        i = int((_max + i)/2)
    elif len(bin(ans)) != len(bin(num+noise)):
        _max = i
        i = int((_min + i) / 2)
    if _max - _min <= 1 :
        answer += _min << 1023
        break

solve_num = 1
while solve_num < 1002:
    times += 1
    shift_num = solve_num -1
    tmp = int(answer << shift_num) + (int('1'*23, 2) << 1000)
    noise = getrandbits(1000)
    ans= (tmp + noise) % secret
    a = ((int('1'*23, 2)- (ans >> (125*8))) >> 1) << 1
    answer += (a) << 1024 - solve_num -23
    solve_num += 22

left = 1024 - solve_num
shift_num = solve_num - (24-left)
tmp = int(answer << shift_num) + (int('1'*left, 2) << 1000)
noise = getrandbits(1000)
ans= (tmp + noise) % secret
a = ((int('1'*left, 2)- (ans >> (125*8))) >> 1) << 1
answer += a 
times += 1

print(secret - answer)
print(secret - (answer+1))
print('times', times)
