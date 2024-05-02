
### What are Pixels and Pointillism?

***Pixels** are a minute area of illumination on a display screen, one of many from which an image is composed.* 

***Pointillism** is a method of painting using tiny dots of various pure colours, which become blended in the viewer's eye.*


### What are Pixels on a screen Arranged in?
*A Matrix, or in python a 2D array*


### How are Uncompressed Grayscale Images Stored in a Matrix?

![[Pasted image 20240227201920.png]]


### How do we use the Idea above for Colour?

*The idea is that each pixel can be represented by a different strength/combination of red, green and blue, which can result in any colour.*

![[Pasted image 20240227202057.png]]


### How do we Load and Display Images in Python?

*Using the matplotlib library we can read and write to image files*

![[Pasted image 20240227202207.png]]


### How are Different Types of Images Represented?

![[Pasted image 20240227202312.png]]


### How can we Overlay one Image on top of Another?

![[Pasted image 20240227202448.png]]
<sup>where T = an empty space, putting the first image on top of the second one</sup>


### What about if we want the Images to have Equal Transparency?

![[Pasted image 20240227202614.png]]


### What about if we want the Images to have Different Transparencies?

![[Pasted image 20240227202712.png]]


### How could we use Subtraction and Two Images to tell if There is an Intruder in a Locked Room?

![[Pasted image 20240227202840.png]]


### But how does Subtraction work?

![[Pasted image 20240227202908.png]]


### But How do we know if it is an Actual person or not?

*We add a threshold, $T$ where if the difference is greater than T it should be recognised.*
$$|frame_i(x,y)-frame_{i-1}(x,y)|>T$$

### How could we Apply this to add Effects to a Web-cam Image?

![[Pasted image 20240227202943.png]]

