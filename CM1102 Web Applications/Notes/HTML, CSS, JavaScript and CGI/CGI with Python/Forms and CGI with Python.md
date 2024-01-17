
##### What is a Form?
*This is a way of allowing the user to enter data*


##### What are the Input types in HTML?

![[Pasted image 20231120121540.png]]


##### What do the ==method== and ==action== Attributes Do?

*==method==*:
- This specifies the way that form data is sent to the server program which can happen in two ways:
	- **GET**, which appends the data to the URL
	- **POST**, which sends the data in the body of a HTTP message

*==action==*:
- This specifies a server program that processes the form data

*e.g.,*
![[Pasted image 20231120122224.png]]


##### What does the Input element "type='text'" specify?
*It specifies that the type of user input is text*

*e.g.,*
![[Pasted image 20231120122208.png]]

**Name Attribute**:
*Gives an identifier to the input data*

**Size Attribute**:
*Specifies the length of a text input field in characters*

**Value Attribute**:
*specifies an initial value for the input data*


##### What does the < label > tag do?

*This connects an attribute name to the value, **for** attribute provides **id** of associated control*

*e.g.,*
![[Pasted image 20231120122821.png]]


##### What does the Input element "type='checkbox'" specify?
*It specifies that the input type is a checkbox*

**Name Attribute**:
*Defines the set of checkboxes*

**Value Attribute**:
*Identifies the individual checkboxes*

**Checked Attribute**:
*Id the checkbox is checked then then the checked attribute is True*

*e.g.,*
![[Pasted image 20231120123642.png]]


##### What does the Input element "type='radio'" specify?
*It specifies that the input type is a radio buttons*

**Name Attribute**:
*Defines the set of radio buttons*

**Value Attribute**:
*Identifies the individual radio buttons*

**Checked Attribute**:
*Id the radio buttons is checked then then the checked attribute is True*

*e.g.,*
![[Pasted image 20231120123745.png]]


##### What does the Input element "type='button'" specify?
*It specifies that the input type is a button*

**Name Attribute**:
*Defines the button*

**Value Attribute**:
*Defines the label to the button*

**Checked Attribute**:
*Id the checkbox is checked then then the checked attribute is True*

*e.g.,*
![[Pasted image 20231120123951.png]]


##### What does the Input element "type='submit'" and "type='reset'" specify?
*It specifies that the input type is a button*

**type='submit'**:
*clicking this button sends the form data to the program specified in the action attribute of the form*

**type='reset'**:
*clicking this button clears all data entered so far*

*e.g.,*
![[Pasted image 20231120124538.png]]


##### What are some Other Types of Input elements?
![[Pasted image 20231120124625.png]]


##### What is CGI - Common Gateway Interface?
*A method of running programs on the server*

![[Pasted image 20231120125753.png]]


##### CGI with Python

*First make HTML file which has an action attribute with the file name*

![[Pasted image 20231120130342.png]]

*Then make the actual CGI with Python*
![[Pasted image 20231120130415.png]]