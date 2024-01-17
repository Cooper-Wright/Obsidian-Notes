
##### How are Plain Text Files converted so that a computer may understand it?

**The steps are:**
1. Separate the letters, spaces, enters (*\\n*) and punctuation into a list of characters
2. Convert each character into ASCII character encoding


##### What are New Line Conventions and what are they in each Main Operating System?

*New Line Conventions are the symbols to show a new line*

- **UNIX / Linux: LF**
- **DOS / Windows: CR + LF**
-  **Apple Mac (to OS-9): CR**


##### What are the 8-bit Character Encodings: the ISO 8859 Standards?

*Since ASCII is 7-bit code thus only has enough space for English characters, thus the ISO 8859 was made.*

ISO 8859 basically is a modified ASCII where the first 128 (0-127) values give the ASCII output and the last 128 (128-255) will output additional characters for the needed non-English language. 

\*Although values 0-31 and 128-159 are non-printable control characters.*

![[Pasted image 20231031121124.png]]


##### What are the advantages and disadvantages of ISO 8859?

***Advantages:***
- Does not require any additional space since ASCII does not use the 8th bit anyway
- It is relatively simple to implement

***Disadvantages:***
- What if the same page needs several languages? How does it store the characters if it does not have room for them?
- What languages with more than 128 special characters?


##### What is Unicode?

First off it assigns one unique number to each character, also known as a "code point", where the first 256 characters are the ISO 8859 character set.

Also by itself, Unicode does not know how to encode things on the byte level*.


##### What are the different types of Unicode and there Advantages and Disadvantages?

**UCS-2:**
*a version which uses 2 bytes for each code-point, instead of the one ASCII / ISO 8859 uses*

***Disadvantages***:
- It is not backward compatible with ASCII
- Unicode now has more that 65t code points ??
- It is generally considered obsolete

**UTF-8**:
*uses 1 byte if it is an ASCII character and multiple bytes if not.*

***Advantages:***
- It can handle backwards compatibility with ASCII
- It can handle all Unicode code points
- It is becoming the standard on the web


###### Example of UTF-8:

![[Pasted image 20231031122402.png]]


##### What happens when a character is not found in ISO-8859-1 (version one) versus UTF-8?

***ISO-8859-1***:
*This character encoding would cause a problem that leave the displayed code with 2 new characters*

e.g.
![[Pasted image 20231031122708.png]]

***UTF-8***:
*This character encoding would display the entered text without the characters it does not know*

e.g.
![[Pasted image 20231031122851.png]]

*Or there is another example to convert [[Converting from Binary to Unicode UTF8|Hexadecimal to Unicode UTF8]]*

##### How can you recognise the Character encoding?
1. Guessing based on the statistical analysis of the file contents
2. "Byte Order Mark" at the beginning of the file
3. In the HTPP/S header:
	- ```Content-Type: text/html; charset=utf-8```
4. In the [[HTML Background]] file itself:
	- ```<meta charset=utf-8>```


##### What do Plain Text Files not Encode?

It does not encode:
- *Any particular font*
- *Any particular font size*
- *Any special formatting (e.g. **bold**)*
- *Any particular colouring scheme*


##### How does [[HTML Background]] have special formatting if it uses plain text files?
*because of markup, as [[HTML Background]] uses markup tags which indicate the structure or special formatting*




