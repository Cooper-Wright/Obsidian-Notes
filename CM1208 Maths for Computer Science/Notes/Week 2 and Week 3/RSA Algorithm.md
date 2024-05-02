*Rivest, Shamir, Adleman*


### What was the Motivation for Creating the RSA Method?
*If the receiver has to know my key, then what happens if the code is learnt whilst in transportation to the person.*

*This is where the **Public key** (encodes the message) and **Private key** (decodes the message) come in. This leads to a reversible process that is not symmetric.*

![[Pasted image 20240207173255.png]]


### What is an Example of RSA being used?

1. *If Sean wants to send a message to Seamus*
2. *Seamus gives Sean his public key.*
3. *Sean uses the public key to encrypt the message, then sends it to Seamus*
	- *The message can only be decrypted with Seamus' private key*
4. *Seamus uses his private key to decrypt the message*


### How would this be Done?

![[Pasted image 20240212211622.png]]


### What is an Example of This?

![[Pasted image 20240212211647.png]]
![[Pasted image 20240212211700.png]]
![[Pasted image 20240212211710.png]]
![[Pasted image 20240212211721.png]]


### What are the Equations to Remember?

*Text to Cipher Text $= M^r$ $mod$ $n$*
*Cipher Text to Text $= C^d$ $mod$ $n$*


### How to do This in Python?

![[Pasted image 20240212212252.png]]


### Why does RSA Work?

- *For any proper message M, it can alwRays be recovered from C.*
- *For proper p, q and r ... d exists and serves as the modular multiplicative inverse.*
- *It is extremely difficult to get from d from r as well as $n = pq$*


### What happens if M is too Big?

*As when M is too large, it is split into smaller messages.*


### How Big is Classified as Large?

*How long at most the checking of each number from 1 to $\sqrt[]{n}$*


### How can the Receiver know when the Message is from the Sender?

*Use RSA to Digitally Sign, which is done by using the opposite of RSA e.g. use a private key to encrypt something, then use the corresponding public key to decrypt it.*

![[Pasted image 20240212213618.png]]


### What is the Difference between Symmetric and Asymmetric Ciphers?

**Symmetric:**
- *Use the same key for encryption and decryption*
- *Include our previous simple ciphers*
- *Practical algorithms are more complicated*

![[Pasted image 20240212213745.png]]


**Asymmetric:**
- *e.g. RSA*
- *Keep Private key secret and public key available.*


![[Pasted image 20240212214014.png]]


