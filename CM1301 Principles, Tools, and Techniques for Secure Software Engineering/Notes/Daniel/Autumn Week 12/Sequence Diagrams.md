
##### What is a Sequence Diagram?

- *An Interaction Diagram, which is one of the **fourteen** provided diagrams of UML, that emphasises the **time order of messages**.*
- *Typically captures the **behaviour** of a **single scenario**, decomposition of the whole system*
- *Shows **multiple sample objects** and the **messages passed** between two objects within the **use case***
- *It models **objects-actors** and **objects-objects** interactions*


##### What is an Example of a Sequence Diagram?

*Below is an Example of a Sequence Diagram:*

![[Pasted image 20240117140452.png]]

*Another more detailed Sequence Diagram is below:*

![[Pasted image 20240117140836.png]]
*sometimes an object may not expect/need a return message*


##### What is Control?

*This can be thought of as **token** that is **passed among objects** and allows them to **perform the tasks** necessary, this can be thought of as "the speaking ..." where whoever is holding the item is allowed to talk. Therefore since **one object holds the token at a time**, the other **objects must wait for it to be passed** back to continue with their activity.*


##### What is Conditional Behaviour?

*A message that is only executed when certain conditions are true. This is shown in a Sequence Diagram inside a rectangle labelled "opt", or optional.*

An Example of this is shown below:

![[Pasted image 20240117145431.png]]
*the red text shows the conditional behaviour, in this case if the dog is "good", they get a treat.*