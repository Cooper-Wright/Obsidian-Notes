
##### What does it mean to Model a Programs Behaviour?

- *Describe how groups of objects collaborate in some behaviour*
- *Show interaction consisting of a set of objects and their relationships, including any message that are sent among objects*


##### What are the Two Forms of Interaction diagrams that [[Modelling with UML|UML]] provides?

- *[[Sequence Diagrams]]*
- *[[Collaboration or Activity Diagrams]]*


##### What Motivates these New Diagrams of UML?

*Lets take the basic example of the relationship between a dog and a stick:*

![[Pasted image 20240117133402.png| 100x300]]

*Now the diagram mentions:*
- *What a dog is.*
- *What a stick is.*
- *What the relationship between the dog and the stick is.*

*What it does not mention is the behaviour when the dog fetches the stick. **Now how would we model this behaviour**?*


##### Why is Collaboration between Objects Necessary for the an Object to be Useful?

*Objects by themselves are essentially useless, <u>as they cannot carry out all tasks needed by the system alone,</u> but by having multiple objects that can interact with one another, <u>through messages</u>, the objects can work as <q>as cogs in a system</q>.*


##### How can we allow Objects to Interact with Message?

*Now that we have established that a system is made from multiple objects, we need to know how to allow these objects to communicate, through messages.*

<em><u>A message shows how one object asks another object to perform some activity.</u></em>

![[Pasted image 20240117134703.png|400]]

One example in code would be:

``` python
class Keyboard:

	def __init__(self, ...):
		...

	def pressesKey(self, keypressed):
		Screen.displayKey(keypressed)


class Screen:

	def __init__(self, ...):
		...

	def displayKey(keypressed):
		print(keypressed)
```
*although this is a very basic example, and would not work, it shows the idea that a message between objects is done through object 1 calling a function of object 2.*