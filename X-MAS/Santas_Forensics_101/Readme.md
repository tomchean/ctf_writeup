# solution

unzip the file given by the problem and observe the output file
```
>> unzip X-MAS_Flag2.zip
>> file X-MAS_Flag2.png
```
find that it turned out to be a zip file so unzip it again and observe output file again
```
>> unzip X-MAS_Flag2.png
>> file hidden_data_dt/logo2.png
```
now, it is really png file
```
>> strings hidden_data_dt/logo2.png
```
get the flag:

**X-MAS{W3lc0m3_t0_th3_N0rth_Pol3}**
