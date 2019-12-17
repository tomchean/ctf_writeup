# Cookie Store
---
## solution
1. To get the flag, we must buy the flag cookie, and in the web site cookie, we can see there's a string 'eyJtb25leSI6IDUwLCAiaGlzdG9yeSI6IFtdfQ==', after decoding in base64, we get '{“money”: 50, “history”: []}.'
2. use '{“money”: 100, “history”: []}.' to encode and set the cookie value, then we can buy the flag cookie.
