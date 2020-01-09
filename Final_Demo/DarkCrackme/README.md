# Dark Crackme
## Introduction

This is the reversing challenge in inferno CTF 2019.(377 pts)

## Analysis

At first, we will get a file called ```darkcrackme```. We can execute it on bash and see what will happen.

![image](https://github.com/tomchean/ctf_writeup/blob/master/Final_Demo/DarkCrackme/execute.png)

We randomly type something to ```username``` and ```password```, but nothing happen:(( 

We can use ```file darkcrackme``` to see the info of file.

![image](https://github.com/tomchean/ctf_writeup/blob/master/Final_Demo/DarkCrackme/file_darkcrackme.png)

We can know it is an ELF 64-bit executable file. Let's dig into it by using IDA Pro.

main(c code):

![image](https://github.com/tomchean/ctf_writeup/blob/master/Final_Demo/DarkCrackme/main.png)

We can see in line 32, we must type ```1_4m_th3_wh1t3r0s3``` as our username to let the program print the flag.

And then in line 34, we can see that it calls a function called ```sub_4013F9```, whose inputs are the string which user types to ```username``` and ```password```. Let's dig into it.

sub_4013F9(c code)

![image](https://github.com/tomchean/ctf_writeup/blob/master/Final_Demo/DarkCrackme/sub_4013F9.png)

In line 9, we know the input string length of ```username``` and ```password``` can not be greater than 40.

In line 11, we know the input string length of ```password``` is two times of that of ```username```. So the input string length of ```password``` must be ```36```. If the conditons above are satisfied, the program will call ```sub_401291```, whose input is the input string of ```password```. Let's dig into it.

sub_401291(c code)

![image](https://github.com/tomchean/ctf_writeup/blob/master/Final_Demo/DarkCrackme/sub_401291.png)

In line 29 - 33, it calls ```sub_4011A7``` and ```sub_401201```. We only know that in the for loop, ```sub_4011A7``` takes two password's char(one with the even index and the other with the odd index) each time and do something with two string(```aAdgjlqetuozcbm``` and ```aSfhkwryipxvn52```). And ```sub_401201``` takes the output of ```sub_4011A7``` as input and do something. So let's dig into these two functions to see what happen.

sub_4011A7(c code)

![image](https://github.com/tomchean/ctf_writeup/blob/master/Final_Demo/DarkCrackme/sub_4011A7.png)

we know that in sub_4011A7, it checks that whether the password's character(with even/odd index) is in  ```aAdgjlqetuozcbm``` / ```aSfhkwryipxvn52```. If the answer is yes, and then it will return the index of that character.

sub_401201(c code)

![image](https://github.com/tomchean/ctf_writeup/blob/master/Final_Demo/DarkCrackme/sub_401201.png)

In sub_401201, we know that it first creates an array whose length is 4 and assigns each element with value 1. Then it edits the value of element with odd or even index, depending on the input(```v2```). The final output of this function is an array whose element value is 0 or 1.

Let's go back to ```sub_401291``` to see what it has done.

![image](https://github.com/tomchean/ctf_writeup/blob/master/Final_Demo/DarkCrackme/sub_401291.png)

So, we know that it first check whether the password's characters are in ```aAdgjlqetuozcbm``` and ```aSfhkwryipxvn52```. And then it create two binary arrays(one from the founded character with even index and the other from that with odd index). And it combines the two strings into one. Repeat the above steps 18 times to convert all the characters to binary arrays and gather all arrays and store it into a large array, whose size is ```8*18```.

Finally, it will compare the binary array of the string of ```username``` and that of ```password```. If two binary array are the same, then it will print the flag.

Let's all! We finally finish analyzing the working flow of this executable file. What we can do is to reverse these steps to get the password.

## Solution

We only know the username, which is ```1_4m_th3_wh1t3r0s3```, thus we can use it as clue to find password.

Convert it to binary array first, which is:
```['00110001', '01011111', '00110100', '01101101', '01011111', '01110100', '01101000', '00110011', '01011111', '01110111', '01101000', '00110001', '01110100', '00110011', '01110010', '00110000', '01110011', '00110011']```

Each 8 bits binary code represents a charactor of ```1_4m_th3_wh1t3r0s3```.

Second step, split the binary array into two sub arrays according to the index. 

Take the first element ```'00110001'``` of the above binary array for example, After splitting, the bits with even index will gather to a sub array, which is ```0100```. And the bits with odd index will gather to a sub array, which is ```0101```.

Repeat the steps above 18 times to split all the binary code into two sub arrays.

Final step, we should know the origin of the binary sub array. That is, we should know that the binary sub array belongs to which character in ```aAdgjlqetuozcbm``` and ```aSfhkwryipxvn52```. 

Thus, we can use iterative method to find the character and gather them into a string, which is exactly what we want---```password```

Now we have the exact string of ```username``` and ```password```, we can execute the executable file again and type the string of username and password to get the flag.

Here is the result:

![image](https://github.com/tomchean/ctf_writeup/blob/master/Final_Demo/DarkCrackme/flag.png)

## Flag

```infernoCTF{CvBsCxOwBsCfOiZvBsZsOiCvCfZvZkCnZhZv}```

## Reproducibility

The python3 code below is my solution to this challenge. The code whose filename is ```darkcrackme.py``` is in the same directory with ```README.md```. TAs can simply run this file by typing ```python3 darkcrackme.py``` on the command line, and the password will be printed. 

Then execute the executable file ```darkcrackme```(which is also in the same directory) and type the string(```1_4m_th3_wh1t3r0s3```) to  username and type the password you get from the code below to password. And you will get the flag.

```python
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
```
