
##### What are Use Cases?

*They:*
- *Define how the system behaves from the users' point of view*
- *Capture the users' functional requirements of a system and are developed for their needs. (Useful for requirement gathering and specification)*
- * Describe what the system will do for the user, not how.*


##### What are the Different Types of Use-Case Model?

- *Capturing a Use-Case Model*

![[Pasted image 20231212153451.png]]


##### What are some Key Facts of Use-Case Diagrams?

- *One of the models of UML*
- *Shows a set of use cases and actors including their relationships*
- *Defines clear boundaries of a system*
- *Identifies who or what interacts with the system*
- *Summarises the behaviour of the system*


##### What are the Elements of Use-Case Diagrams?

![[Pasted image 20231212153908.png]]


##### What should Each Use-Case do?

- *Model a dialog between the system and actors*
- *Is coherent unit of functionality provided by a system*
- *Describe the sequence of actions that the system takes to deliver something of value to an actor*


##### What is the Process of Writing Use-Cases?

![[Pasted image 20231212154223.png]]


##### What is an Actor?

*A role that only an **external** human, hardware device or other system can play in relation to the system, where a complete set of actors describes all of the ways in which the users communicate with the system. **AVOID "USER"**, as an actors name.*


##### What Requirements should the Name of the Use-Case fit?

- *Be unique and intuitive*
- *Define clearly the observable result of value gained from the Use Case*
- *Be from the perspective of the actor that triggered the Use Case*
- *Describe the behaviour that the Use Case supports*
- <u><em>Start with a verb and use a simple verb-noun combination</em></u>


##### What is an Example of a Use-Case Example?

*Use Case Diagram:*

![[Pasted image 20231212155631.png]]


*Use Case Text Description:*

![[Pasted image 20231212155729.png]]


##### When Writing the Basic flow of Events how should they be Detailed?

![[Pasted image 20231213112920.png]]


##### How do you Phrase these Steps?

- *Use the Active voice, meaning the subject sounds like they are doing something active.*
	- *e.g. "When the Professor has provided the grades", it should be "The Professor provides the grades for each student"*
- *Say what triggers the step*
	- *e.g. "The use case starts when the Professor chooses to submit grades"*
- *Say who is doing what, using the Actor name*
	- *e.g. "The Student chooses", instead of "The user chooses"*


##### How should the Detail of Alternative Flows be Presented?

![[Pasted image 20231213113323.png]]


##### What are some Tips for writing better Descriptions?

- *Include a detailed specification of the basic flow, these should be written so that they can be validated*
- *Identify possible alternative flows for each, provide a description of their flow of events*
- *State any Pre/Post-conditions for the use case*
- *Do not forget to include any [[Non-Functional Requirements]], constraints or characteristic of the system required by the client, these should be testable*
- *Priority should be indicated using [[MoSCoW|MoSCoW notation]]*


##### Why and How can you Expand Use Cases?

*Where more detail is required the top level use cases should be decomposed and have more detail by using includes, extends and generalisation relationships:*

![[Pasted image 20240103140447.png]]

*Where each expanded top level use case is drawn on a separate diagram, where these diagrams:*
- *Should not show the system*
- *Do not have to include actors*
- *Should be expressed in terms of what the actor wants to be able to do with interaction with the system*


##### Why should you Use an Include Relationship?

*e.g.*
![[Pasted image 20240103141237.png]]


- *To factor behaviour common between multiple use cases*
- *To factor out and encapsulate behaviour from a base use case that is complex or long*


##### Why should you Use an Extend Relationship?

*e.g.*
![[Pasted image 20240103141353.png]]

*If the extension point is True then the "flow" follows the extra loop*


##### Why should you Use an Extend Relationship?

*e.g.*
![[Pasted image 20240103141609.png]]

*Generalisation is basically inheritance for use cases*


##### What is an Example of a Use Case Diagram?

*e.g.*
![[Pasted image 20240103141713.png]]

![[Pasted image 20240103141734.png]]

