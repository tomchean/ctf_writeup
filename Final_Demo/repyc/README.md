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

Let's moving on. In the following several lines, we can see a function:






