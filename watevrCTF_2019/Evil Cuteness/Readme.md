# Evil Cuteness
---
## Solution
1. first use 'binwalk -e kitty.jpg', we can see there's a zip file in it.
```
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.01
382           0x17E           Copyright string: "Copyright (c) 1998 Hewlett-Packard Company"
21639         0x5487          Zip archive data, at least v2.0 to extract, compressed size: 40, uncompressed size: 42, name: abc
21813         0x5535          End of Zip archive
```
2. just goto the extract file and 'cat abc', we can see the flag 'watevr{7h475_4c7u4lly_r34lly_cu73_7h0u6h}'
