# Repyc
## Introduction

This is the reversing challenge in watevrCTF 2019.(147 pts)

## Analysis

At first, we will get a pyc file called ```3nohtyp.pyc```. Let's decompile it to get the original .py file by typing ```uncompyle6 -o repyc.py 3nohtyp.pyc``` 

![image](https://github.com/tomchean/ctf_writeup/blob/master/Final_Demo/repyc/img/decompile.png)

Let's open the original .py file([repyc.py](https://github.com/tomchean/ctf_writeup/blob/master/Final_Demo/repyc/src/original_repyc.py)). And we can see some strange characters in the first three line:
```python
佤 = 0
侰 = ~佤 * ~佤
俴 = 侰 + 侰
```
It's really annoying and hard to understand the code, so let's change them to some common characters:

```python
A = 0
B = ~A * ~A
C = B + B
```
And do some calculations:

```python
A = 0
B = 1
C = 2
```

Let's moving on. In the following several lines, we can see a function(the below code is just a part of the function):

```python
def 䯂(䵦):
    굴 = 佤
    굿 = 佤
    괠 = [佤] * 俴 ** (俴 * 俴)
    궓 = [佤] * 100
    괣 = []
    while 䵦[굴][佤] != '듃':
        굸 = 䵦[굴][佤].lower()
        亀 = 䵦[굴][侰:]
        if 굸 == '뉃':
            괠[亀[佤]] = 괠[亀[侰]] + 괠[亀[俴]]
        elif 굸 == '렀':
            괠[亀[佤]] = 괠[亀[侰]] ^ 괠[亀[俴]]
```

It's the only function in this .py file, so let's rename it to ```main_funtion```

And the function's input(```䵦```) is a list, so let's rename it to ```input_list```. After doing some calculation and rename some variable, the function become more readable.

```python
def main_function(input_list):
    var1 = 0
    var2 = 0
    _16list = [0] * 16
    _100list = [0] * 100
    buff = []
    while input_list[var1][0] != '듃':
        _arg = input_list[var1][0].lower()
        info_list = input_list[var1][1:]
        if _arg == '뉃':
            _16list[info_list[0]] = _16list[info_list[1]] + _16list[info_list[2]]
        elif _arg == '렀':
            _16list[info_list[0]] = _16list[info_list[1]] ^ _16list[info_list[2]]
```
Below the function, we can see that the program calls the ```main_function``` once, and we can know how ```input_list``` looks like(the below code is just a part of the ```input_list```):

```python
main_function([
 [
  '꼖', 0, '0uthenti20tion token: '],
 [
  '꽺', 0, 0],
 [
  '꼖', 6, 'á×äÓâæíäàßåÉÛãåäÉÖÓÉäàÓÉÖÓåäÉÓÚÕæïèäßÙÚÉÛÓäàÙÔÉÓâæÉàÓÚÕÓÒÙæäàÉäàßåÉßåÉäàÓÉÚÓáÉ·Ôâ×ÚÕÓÔÉ³ÚÕæïèäßÙÚÉÅä×ÚÔ×æÔÉ×Úïá×ïåÉßÉÔÙÚäÉæÓ×ÜÜïÉà×âÓÉ×ÉÑÙÙÔÉâßÔÉÖãäÉßÉæÓ×ÜÜïÉÓÚÞÙïÉäàßåÉåÙÚÑÉßÉàÙèÓÉïÙãÉáßÜÜÉÓÚÞÙïÉßäÉ×åáÓÜÜ\x97ÉïÙãäãÖÓ\x90ÕÙÛ\x99á×äÕà©â«³£ï²ÕÔÈ·±â¨ë'],
 [
  '꼖', 2, 2 ** (3 * 2 + 1) - 2 ** (2 + 1)],
 [
  '꼖', 4, 15],
 ```
 
After more inspection, we know that the ```main_function``` will do the corresponding action, according to the first character of the sub list in ```input_size```.

So I interpret the actions according to  the sub lists in ```input_size```:

```python
main_function([
 [  # assign the first element of _16list to 'Authentication token: '
  '꼖', 0, 'Authentication token: '],   
 [  # print 'Authentication token: ' on the command line. and assign the first element of _100list to what user type
  '꽺', 0, 0],  
 [  # assign the seventh element of _16list to the string below
  '꼖', 6, 'á×äÓâæíäàßåÉÛãåäÉÖÓÉäàÓÉÖÓåäÉÓÚÕæïèäßÙÚÉÛÓäàÙÔÉÓâæÉàÓÚÕÓÒÙæäàÉäàßåÉßåÉäàÓÉÚÓáÉ·Ôâ×ÚÕÓÔÉ³ÚÕæïèäßÙÚÉÅä×ÚÔ×æÔÉ×Úïá×ïåÉßÉÔÙÚäÉæÓ×ÜÜïÉà×âÓÉ×ÉÑÙÙÔÉâßÔÉÖãäÉßÉæÓ×ÜÜïÉÓÚÞÙïÉäàßåÉåÙÚÑÉßÉàÙèÓÉïÙãÉáßÜÜÉÓÚÞÙïÉßäÉ×åáÓÜÜ\097ÉïÙãäãÖÓ\09aÕÙÛ\099á×äÕà©â«³£ï²ÕÔÈ·±â¨ë'],
 [  # assign the third element of _16list to 120
  '꼖', 2, 2 ** (3 * 2 + 1) - 2 ** (2 + 1)],
 [  # assign the fifth element of _16list to 15
  '꼖', 4, 15],
 [  # assign the fourth element of _16list to 1
  '꼖', 3, 1],
 [  # assign the third element of _16list to 120*1
  '냃', 2, 2, 3],
 [  # assign the third element of _16list to 120+15
  '뉃', 2, 2, 4],
 [  # no effect
  '괡', 0, 2],
 [  # assign the fourth element of _16list to 0
  '댒', 3],
 [  # convert the seventh element of _16list to something
  '꾮', 6, 3],
 [  # assign the first element of _16list to 'Thanks.'
  '꼖', 0, 'Thanks.'],
 [  # assign the second element of _16list to 'Authori2ing access...'
  '꼖', 1, 'Authori2ing access...'],
 [  # print the first element of _16list ('Thanks.')
  '돯', 0],
 [  # assign the first element( what user previously input ) of _100list to the first element of _16list 
  '딓', 0, 0],
 [  # convert the user's input to something (user string ^ 135)
  '꾮', 0, 2],  
 [  # convert the user's input to something (user string - 15)
  '꿚', 0, 4],
 [  # assign the sixth element of _16list to 19
  '꼖', 5, 19],
 [  # string comparison
  '꽲', 0, 6, 5],
 [  # print the first element of _16list (user input after conversion)
  '돯', 1],
 [  # function end
  '듃'],
 [  
  '꼖', 1, 'Access denied!'],
 [
  '돯', 1],
 [
  '듃']])
  ```
In the middle part of the file, we can see

```python
elif _arg == '꾮':
    tmp_string = ''
    for i in range(len(_16list[info_list[0]])):
        tmp_string += chr(ord(_16list[info_list[0]][i]) ^ _16list[info_list[1]])

    _16list[info_list[0]] = tmp_string
elif _arg == '꿚':
    tmp_string = ''
    for i in range(len(_16list[info_list[0]])):
        tmp_string += chr(ord(_16list[info_list[0]][i]) - _16list[info_list[1]])

    _16list[info_list[0]] = tmp_string
```

Which is used to convert user's input string to a string, and


```python
elif _arg == '꽲': 
    _16list[7] = 0
    for i in range(len(_16list[info_list[0]])):
        if _16list[info_list[0]] != _16list[info_list[1]]: # compare user's input and the s string
            _16list[7] = 1
            var1 = _16list[info_list[2]] 
            buff.append(var1)
```

which is used to compare the converted user input and the string(```á×äÓâæíäàßåÉÛãåäÉÖÓÉäàÓÉÖÓåäÉÓÚÕæïèäßÙÚÉÛÓäàÙÔÉÓâæÉàÓÚÕÓÒÙæäàÉäàßåÉßåÉäàÓÉÚÓáÉ·Ôâ×ÚÕÓÔÉ³ÚÕæïèäßÙÚÉÅä×ÚÔ×æÔÉ×Úïá×ïåÉßÉÔÙÚäÉæÓ×ÜÜïÉà×âÓÉ×ÉÑÙÙÔÉâßÔÉÖãäÉßÉæÓ×ÜÜïÉÓÚÞÙïÉäàßåÉåÙÚÑÉßÉàÙèÓÉïÙãÉáßÜÜÉÓÚÞÙïÉßäÉ×åáÓÜÜ\097ÉïÙãäãÖÓ\09aÕÙÛ\099á×äÕà©â«³£ï²ÕÔÈ·±â¨ë```)

And I noticed that some part(line67~111) of the ```main_function``` is wrong intented, so I did some correction of the code.

Now everything is clear, we need to reverse the operations, which are done on user's input, on the string(```á×äÓâæíäàßåÉÛãåäÉÖÓÉäàÓÉÖÓåäÉÓÚÕæïèäßÙÚÉÛÓäàÙÔÉÓâæÉàÓÚÕÓÒÙæäàÉäàßåÉßåÉäàÓÉÚÓáÉ·Ôâ×ÚÕÓÔÉ³ÚÕæïèäßÙÚÉÅä×ÚÔ×æÔÉ×Úïá×ïåÉßÉÔÙÚäÉæÓ×ÜÜïÉà×âÓÉ×ÉÑÙÙÔÉâßÔÉÖãäÉßÉæÓ×ÜÜïÉÓÚÞÙïÉäàßåÉåÙÚÑÉßÉàÙèÓÉïÙãÉáßÜÜÉÓÚÞÙïÉßäÉ×åáÓÜÜ\097ÉïÙãäãÖÓ\09aÕÙÛ\099á×äÕà©â«³£ï²ÕÔÈ·±â¨ë```)
 
 ## Solution
 
 The python3 code below is my solution to this challenge.
 ```python
 def convert1_str(s):
    result = ''
    for i in range(len(s)):
        result += chr(ord(s[i]) + 15)

    return result

def convert2_str(s):
    result = ''
    for i in range(len(s)):
        result += chr(ord(s[i]) ^ 135)

    return result

if __name__ == "__main__":
    s = 'á×äÓâæíäàßåÉÛãåäÉÖÓÉäàÓÉÖÓåäÉÓÚÕæïèäßÙÚÉÛÓäàÙÔÉÓâæÉàÓÚÕÓÒÙæäàÉäàßåÉßåÉäàÓÉÚÓáÉ·Ôâ×ÚÕÓÔÉ³ÚÕæïèäßÙÚÉÅä×ÚÔ×æÔÉ×Úïá×ïåÉßÉÔÙÚäÉæÓ×ÜÜïÉà×âÓÉ×ÉÑÙÙÔÉâßÔÉÖãäÉßÉæÓ×ÜÜïÉÓÚÞÙïÉäàßåÉåÙÚÑÉßÉàÙèÓÉïÙãÉáßÜÜÉÓÚÞÙïÉßäÉ×åáÓÜÜ\x97ÉïÙãäãÖÓ\x9aÕÙÛ\x99á×äÕà©â«³£ï²ÕÔÈ·±â¨ë'
    flag = convert2_str( convert1_str(s) )

    print(flag)
```

## Flag

```watevr{this_must_be_the_best_encryption_method_evr_henceforth_this_is_the_new_Advanced_Encryption_Standard_anyways_i_dont_really_have_a_good_vid_but_i_really_enjoy_this_song_i_hope_you_will_enjoy_it_aswell!_youtube.com/watch?v=E5yFcdPAGv0}```
 
## Reproducibility
TA
