
### What are the Strings?
*A collection of bytes or words, which have 9 instructions which can be performed on them, e.g. copying, comparing etc*


### What are some Special Registers used in String Operations?

**ECX:**
- *A special instruction called the "repeat prefix" can be used to copy, compare or scan operations.*
- *Register ECX has an assigned role in this process. It contains the repeat count necessary for the repeat prefix.*
- *ECX is decremented during the string operation, which terminates when ECX reaches zero.*

**ESI and EDI:**
- *The processor assumes that the ESI register points to the first element of the Source string. Similarly, it assumes EDI points to the first element of the Destination.*
- *A special flag called the "Direction Flag" is used to control the way the ESI and EDI are adjusted during a string instruction e.g. incremented or decremented based on the condition of the flag.*

**Additional Material:**
- *In the original Real-Mode addressing, the string primitives used SI and DI in conjunction with the segment registers SI is an offset of DS and DI was an offset of ES.*
- *However, from our viewpoint using the flat memory model (Protected Mode) we do not need to worry about this and use ESI and EDI registers that are both fixed.*

*e.g. Real Mode (NO LONGER USED):*

![[Pasted image 20240316164426.png]]


*e.g. Move 10 bytes from string1 to string2*

![[Pasted image 20240316164458.png]]

![[Pasted image 20240316164752.png]]


### What is Initialisation?
*Before we can use any string we must set up the ESI and EDI registers.*

![[Pasted image 20240316164835.png]]


### What are Direction Flags?

*The Direction Flag is used to select the direction in which the various string functions operate on the EDI and ESI registers, where if it is set to 1 then the operation is auto decremented and the opposite if set to 0.*

*There are two instructions used to set this flag:*
- *CLD (Clear Direction Flag) which clears the direction flag i.e. sets it to 0 meaning it auto increments it*
- *SLD (Set Direction Flag) which sets the direction flag i.e. set it to 1 meaning it auto decrements it.*


### What are the Nine String Instructions?
1. *$REP$ - Repeat*
2. *$REPE$ $(REPZ)$ - Repeat while equal*
3. *$REPNE$ $(REPNZ)$ - Repeat while not equal*
4. *$MOVS$ - Move byte or word string*
5. *$MOVSB$ $(MOVSW)$ - Move byte string (word string)*
6. *$CMPS$ - Compare byte or word string*
7. *$SCAS$ - Scan byte or word string*
8. *$LODS$ - Load byte or word string*
9. *$STOS$ - Store byte or word string*


### $REP/REPE/REPZ/REPNE/REPNZ$...

![[Pasted image 20240317165009.png]]

#### $REP$...
![[Pasted image 20240317165034.png]]

#### $REPE/REPZ/REPNE/REPNZ$...
![[Pasted image 20240317165111.png]]


### $MOVS/MOVSB/MOVSW$...

#### $MOVS$...
![[Pasted image 20240317165208.png]]

#### $MOVSB/MOVWS$...
![[Pasted image 20240317165236.png]]

```Assembly
.data
	shopper db “SHOPPER”
	copyLoc db 100 DUP(0)

main proc
	MOV ECX,LENGTHOF shopper ;COUNT FOR REPEAT
	MOV ESI, OFFSET shopper ;SOURCE ADDRESS
	MOV EDI, OFFSET copyLoc ;DESTINATION ADDRESS
	
	CLD ;AUTO-INCREMENT CLEAR
		;DIRECTION FLAG
	
	REP MOVSB ;REPEAT WHILE ECX <>0
			  ;COPY STRING
```


### $CMPS$...
![[Pasted image 20240317165415.png]]

```Assembly
MATCH PROC
	MOV ESI,LINE ;Address of LINE
	MOV EDI,TABLE ;Address of TABLE
	CLD ;auto-increment
	MOV ECX,10 ;counter
	REPE CMPSB ;search
RET
MATCH ENDP
```

*If ECX = zero when proc returns then strings are the same else they do not match.*


### $SCAS$...
![[Pasted image 20240317165530.png]]

```Assembly
	MOV EDI,BLOCK ;ADDRESS OF DATA
	CLD ;AUTO-INCREMENT
	MOV ECX,100 ;COUNTER
	MOV AL,’A’
	REPNE SCASB ;SEARCH
```


### $LODS$...
![[Pasted image 20240317165626.png]]


### $STOS$...
![[Pasted image 20240317165649.png]]

*Example:*
![[Pasted image 20240317165706.png]]

```Assembly
MOV ESI, OFFSET FIRST_BLOCK ;SOURCE ADDRESS, no need to provide
MOV EDI, OFFSET FIRST_BLOCK +8 ;DESTINATION ADDRESS
CLD ;AUTO-INCREMENT CLEAR DIRECTION FLAG
MOV AX, 4D20H ;CODE FOR BLANK 20H AND M 4DH
STOSW ;STORE WORD
MOV AX, 4C41H ;CODE FOR LETTERS AL 41H and 4CH
STOSW
MOV AX,0D4CH ;CODE FOR L AND CR 4CH and 0DH
STOSW
```

*We loaded the AX register with each byte in reverse (Byte Swapped). Remember the processor will take care of reversing the values in memory.*


#### Using $STOS$ to Clear a block of Memory...

```Assembly
MOV EDI,BUFFER ;get buffer address
MOV ECX,10 ;load counter
CLD ;select auto-increment
MOV AL,0 ;Clear AL
REP STOSB ;Clear buffer
```

#### Using $STOS$ to Clear a Buffer...

```Assembly
MOV EDI,BUFFER ;get buffer address
MOV ECX,5 ;Load counter
CLD ;select auto-increment
MOV AX,0 ;clear AX
REP STOSW ;clear buffer
```
