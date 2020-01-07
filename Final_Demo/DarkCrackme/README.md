# Dark Crackme

This is the reversing challenge in inferno CTF 2019.

At first, we will get a file called ```darkcrackme```. We can execute it on bash and see what will happen.

![image](https://github.com/tomchean/ctf_writeup/blob/master/Final_Demo/DarkCrackme/execute.png)

We randomly type something to ```username``` and ```password```, but nothing happen:(( 

We can use ```file darkcrackme``` to see the info of file.

![image](https://github.com/tomchean/ctf_writeup/blob/master/Final_Demo/DarkCrackme/file_darkcrackme.png)

We can know it is an ELF 64-bit executable file. Let's dig into it by using IDA Pro.

main(c code):
![image](https://github.com/tomchean/ctf_writeup/blob/master/Final_Demo/DarkCrackme/main.png)

We can see in line 31, we must type ```1_4m_th3_wh1t3r0s3``` as our username to let the program print the flag.

And then in line 34, we can see that it calls a function called ```sub_4013F9```, whose inputs are the string which user types to ```username``` and ```password```. Let's dig into it.

sub_4013F9(c code)
![image](https://github.com/tomchean/ctf_writeup/blob/master/Final_Demo/DarkCrackme/sub_4013F9.png)

In line 9, we know the input string length of ```username``` and ```password``` can not be greater than 40.
In line 11, we know the input string length of ```password``` is two times of that of ```username```. So the input string length of ```password``` must be ```36```. If the conditons above are satisfied, the program will call ```sub_401291```, whose input is the input string of ```password```. Let's dig into it.

sub_401291(c code)
![image](https://github.com/tomchean/ctf_writeup/blob/master/Final_Demo/DarkCrackme/sub_401291.png)





