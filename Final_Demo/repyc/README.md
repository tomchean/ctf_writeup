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

And the function's input(```䵦```) is a list, so let's rename it to ```input_list```. After doing some calculation and rename some variable, the function become readable.

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









