##### What are the different Attributes?
- *Core Attributes: Including the class, id, style, and title attributes*
- *Internationalization attributes: e.g. dir or lang attributes*
- *Accessibility attributes: e.g. accesskey and tabindex*


##### What are the Four Core Attributes?
- ***id attribute:***
	- *This uses a string e.g. ```id = "string"``` to individually and uniquely identify any element in a [[HTML Background|HTML]] page to be used in the [[CSS Background|CSS Style]] or the [[JavaScript|JavaScript Program]]*.
	- e.g. ```<p id="accounts">This paragraph explains the role of the accounts department.</p>```
	- The rules for the id attribute is that it must start with a letter then can be followed with any digit, hyphen, underscore, colon or period


 - ***class attribute:***
	- *This uses a string e.g. ```class = "string"``` to  uniquely identify a set of elements in a [[HTML Background|HTML]] page to be used in the [[CSS Background|CSS Style]] or the [[JavaScript|JavaScript Program]]*.
	- e.g. ```<p class="summary">Summary goes here</p>``` or ```class="className1 className2 className3"```
	- The rules for the id attribute is that it must start with a letter then can be followed with any digit, hyphen, underscore, colon or period



 - ***title attribute:***
	- *This uses a name for a title e.g. ```title = "string"``` and has a range of functions depending on the element such as a tooltip*.
	- e.g. ```<img scr = "www.aimageyoufoundoftheweb.com" title = "a image i dont own">```


 - ***style attribute:***
	- *This uses a certain [[CSS Background|CSS Style]] e.g. ```style="font-family:arial"``` to  change a certain aspect of the tag it is within e.g. the font or colour (used as "color") etc*.
	- e.g. ```<p style="font-family:arial; color:#FF0000;">Some text.</p>```
	- The rules for the id attribute is that it must start with a letter then can be followed with any digit, hyphen, underscore, colon or period


##### Why do we need to Internationalize our Webpages?
*Since there is a range of languages we, as programmers, need to customise our HTML to diversify the webpages accessibility*

*There are two common internationalization attributes:*
- *dir*
- *lang*


##### What does the "dir" Attribute do?
*The dir value only defines the way the the document should be read.*

| Value | Meaning                           |
| ----- | --------------------------------- |
| ltr   | Left to right (the default value) |
| rtl      | Right to left (for languages such as Hebrew or Arabic that are read right to left)                                   |


##### What does the "lang" Attribute do?
*The lang value only defines the main language of a document. For example:*

| Value | Meaning      |
| ----- | ------------ |
| ar    | Arabic       |
| en    | English      |
| en-us | U.S. English |
| zh    | Chinese      |


