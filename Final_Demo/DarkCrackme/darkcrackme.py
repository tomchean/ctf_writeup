import numpy as np
import math

def find_idx(idx_binary_arr):
    for idx in range(16):
        binary_array = binary_generator(idx)
        if ( check_binary_array(idx_binary_arr, binary_array) ):
            return idx

def binary_generator(idx): # sub_401201
    binary_array = np.ones(4)
    v4 = 3
    while idx > 0 :
        if idx & 1: # odd
            binary_array[v4] = 0
        else:       # even
            binary_array[v4] = 1
        v4 -= 1
        idx = math.floor(idx / 2)

    return binary_array

def check_binary_array(a1, a2):
    length = 4
    for i in range(length):
        if a1[i] != a2[i]:
            return False
    return True

if __name__ == "__main__":
    username = '1_4m_th3_wh1t3r0s3'
    check_even_str = 'ADGJLQETUOZCBM10'
    check_odd_str = 'sfhkwryipxvn5238'
    # convert username to binary code
    binary_username = [ bin(ord(ch))[2:].zfill(8) for ch in username ]
    '''
    binary_username:
    ['00110001', '01011111', '00110100', '01101101', '01011111', 
     '01110100', '01101000', '00110011', '01011111', '01110111', 
     '01101000', '00110001', '01110100', '00110011', '01110010', 
     '00110000', '01110011', '00110011']
    '''
    # split binary_username
    even_idx_binary_arr, odd_idx_binary_arr = np.zeros((18, 4)), np.zeros((18, 4))
    for i in range(18):
        for j in range(4):
            even_idx_binary_arr[i][j] = binary_username[i][2*j]
            odd_idx_binary_arr[i][j] = binary_username[i][2*j+1]

    # solve password
    password = ''
    for i in range(18):
        even = check_even_str[find_idx(even_idx_binary_arr[i])]
        password += even
        odd = check_odd_str[find_idx(odd_idx_binary_arr[i])]
        password += odd
    
    print(password)

    
