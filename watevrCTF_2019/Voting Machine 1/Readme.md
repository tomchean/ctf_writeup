# Voting Machine 1
---
## solution
1. first use 'objdump -d -M intel kamikize', we can see in 0x0000000000400807 there's a spuer secret function
2. Use gdb, we can see that the return address is 0x10 after the address of our input variable, thus we can use buffer overflow attack
