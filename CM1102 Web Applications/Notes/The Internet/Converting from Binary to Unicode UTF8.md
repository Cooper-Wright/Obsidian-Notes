
Suppose we are opening a particular text file with a binary editor, which gives you the hexadecimal encoding of each byte, plus its associated ASCII character (or ? when the byte does not correspond with any ASCII character). How does that work? 

*Well a fragment is shown below:*


| 4f | 77 | 61 | 69 | 6e | 20 | 47 | 6c | 79 | 6e | 64 | c5 | b5 | 72 |
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
| O | w | a | i | n | | G | l | y | n | d | ? | ? | r |


How do you identify the non-ASCII character encoded by c5 and b5? 
Well we start with converting c5 b5 from hexadecimal to binary:

***11000101 10110101***


This binary representation coincides with what we would expect a 2-byte UTF8 encoded character to look like. In particular, the first byte starts with *"110"* (which means it's the first byte of a 2-byte character) and the second byte starts with *"10"* (which means it's a follow-up byte).

*So we actually have:*

***[110]00101 [10]110101***


*This means that the bits that carry the actual information are:*

***00101 110101***


*If we convert this from binary to hexadecimal we obtain:*

***0x175***


*Or, to use Unicode notation:*

***U+0175***

Which is equal to *ŵ*