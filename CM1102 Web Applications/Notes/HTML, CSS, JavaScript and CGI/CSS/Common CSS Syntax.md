
##### What are the CSS Style Rules?

A Style rule has a **selector**, *this specifies what HTML element the style should be applied to,* and a **set of declarations**, *specify how the element should be changed,* e.g. 

![[Pasted image 20231106121653.png]]

Each Declarations consists of a property and a value.


##### Where can you put the CSS Style:
- *Inline, in an individual element, e.g.*
	![[Pasted image 20231106122004.png]]

- *In an internal style sheet, inside the ```<style>``` tags, inside the ```<head>``` tags*
	![[Pasted image 20231106122138.png]]

- *In an external style sheet, in a separate file referenced by the ```<link>``` element*
	![[Pasted image 20231106122229.png]]
- This is done through the element:
	![[Pasted image 20231106122354.png]]
	***or can be done through an import:***
	```@import url("mystyles.css")```
	
- within the HTML file, where each of the variables specify a different thing.


##### What are the most useful Selectors in CSS?

| Name                | Example |
| ------------------- | ------- |
| [[Type selector]]     | p       |
| [[Class selector]]     | .blah   |
| [[ID selector]]         | # blah   |
| [[Child selector]]      | p > em  |
| [[Descendant selector]] | p span  |
| [[Adjacent sibling]]    | h1 + p  |
| [[General sibling]]     | h1 ~ p  |


##### What are the different CSS Properties and Values?

- ***Fonts:***
	- **font-family**: ```<family name> [<generic family>]```
	- **font-style**: normal | italic | oblique
	- **font-weight**: normal | bold| bolder | lighter
	- **font-size**: small | medium | large | smaller | larger

- ***Colours and backgrounds for text:***
	- **color**: ```<value>``` <sub><em>(uses American spelling)</em></sub>
	- **background-color**: ```<value>``` | transparent <sub><em>(uses American spelling)</em></sub>
	- **background-image**: URL | none

- ***Text:***
	- **text-decoration**: none | underline | overline | line-through
	- **text-transformation**: none | capitalize | uppercase | lowercase
	- **text-align**: left | right | center | justify <sub><em>(uses American spelling)</em></sub>
	- **text-indent**: length | percentage

- ***CSS Box Model:***
![[Pasted image 20231106124234.png|400]]

- **margin**: width (e.g. 5px or 5%) margin*-top, margin-right, margin-left, margin-bottom*
- **padding**: width (e.g. 5px or 5%)
- **border-width**: thin | thick | medium (or width units)
- **border-color**: colour name or hex/rgb values <sub><em>(uses American spelling)</em></sub>
- **border-style**: none | dotted | dashed | solid | double | groove | ridge | inset | outset
<sub><em><strong>*All of these values have top/bottom/left/right variants*</strong></em></sub>


##### What are the Size Units for Width?

- **px**: *pixels (e.g. 5px)*
- **em**: *related to font size (so 1em=12pt if the current font size is 12pt)*
- **ex**:* related to font size(height of lowercase x)*
- **pt**: *points (1/72 inch)● pc: pica (12 points)*
- **%:*** percentage of the entire box width*


##### What is the Shorthand names for Box Widths?

- **1 value: all edges**
	- *margin: 10px;*
- **2 values: top+bottom, left+right**
	- *border-width: 10px 15px;*
- **3 values:**
	- *top, left+right, bottompadding: 4px 8px 10px;*
- **4 values:**
	- *top, right, bottom, left(so clockwise from top)border: 2px 4px 6px 8px;*


##### What are some List Styles?

- **The bullets or counters can be set with:**
	- *list-style-type: disc | circle | square | decimal | lower-alpha | upper-alpha | lower-roman | upper-roman*
- **To use your own image for the bullets or marker:**
	- *list-style-image: url(“mybullet.png”);*
- **To remove bullets or counter entirely:**
	- *list-style: none;*


##### What are CSS Event Pseudo-Classes and What are some Examples?

- *They are events that can detect mouse events such as:*
	1. Not yet visited is:
		- *a:link { color: blue; }* <sub><em>(uses American spelling)</em></sub>
	2. Already visited:
		- *a:visited { color: purple; }* <sub><em>(uses American spelling)</em></sub>
	3. Mouse goes over element:
		- *a:hover { color: green; }*
	4. *Element is being clicked:*
		- *a:active { color: red; }*


##### How do you add Colour to an Element?

*First off colours can be added in different ways such as Hexadecimal, RGB colour codes and textual names.*

```<body style="background-color:#d2691e">``` - *This is a Hexadecimal colour code.*
```<h1 style="colour:rgb(210, 105, 30)">``` - *This is a RGB colour code.*
```<body style="bockground-color:gray; colour:black;">``` - *This is a Textual name for a colour*


##### If you have Multiple Stylesheets, which ones take Priority?

**If they are External Stylesheets:**
*The later the stylesheet is defined, the higher priority the stylesheet has*

**If they are a Mix:**
*The inline styles have the highest priorities then the internal stylesheets then external style sheets*

**If there are Multiple Rules in a Individual Stylesheet:**
*The latest one takes precedence.*


##### Instead of applying styles to an element itself, How can we apply Styles to a Larger and Smaller Set of Elements?

**Larger would mean including multiple elements and this would be done using:**
*The ```<div>``` tag, which is used to apply CSS styles to multiple elements within the <em><u>division</u></em> tags

![[Pasted image 20231108112434.png|250]]


**Smaller would mean including less than an element, such as a piece of text, this would be done using:**
*The  ```<span>``` tag, which is used to apply CSS styles to a select few words or characters within the <u><em>span</em></u> tags*

![[Pasted image 20231108112504.png|250]]


##### What are the Different types of Positioning in CSS and What do they do?

- **Absolute Positioning:**
	- *The values of <u><em>left</em></u> and <u><em>top</em></u> are distances from the top left corner of the containing element.*

![[Pasted image 20231108112739.png|450]]

- **Relative Positioning:**
	- *The values are relative to the top left of where the element would have been placed otherwise*
	- *To do this the parent element of this child, e.g. the ```<body>``` tags, should have the CSS style of ```{position: relative;}```*

![[Pasted image 20231108113024.png|450]]


##### How do Layers work in Webpages?

*The browsers maintains a stack of layers each containing text, images etc*

*As we know there is the x and y axis which are left to right and down to up respectively but there is also a z axis (also known as the **z-index**). This z-index specifies the order of an element in the stack if layers. **Where the higher the number the element is the higher on the stack it is.***

![[Pasted image 20231108161657.png]]


##### What are :*nth-child* and :*nth-of-type* pseudo-classes? How do they work?

- ```:nth-child(n)``` - Selects the nth child of the specified type to occur within any parent element 
- ```p:nth-child(2)``` - Selects a ```<p>``` element within any immediate parent, if it is the second child element of that parent
- ```p:nth-of-type(2)``` - Selects the second ```<p>``` element within any immediate parent
	- *e.g. ```p:nth-of-type(2n)``` - Selects every other ```<p>``` child of a parent element, starting at 2 (since it is "2n", works the same with "even" too)*


##### What are :*before* and :*after* pseudo elements? How do they work?

- ```p:before``` - Inserts specified content at the beginning of the specified element
	- *e.g. ```p:before {content: "Cooper:";}``` adds "Cooper" to the start of all ```<p>``` elements*
- ```:after``` - Is the same as ```:before``` but does it after the specified element



