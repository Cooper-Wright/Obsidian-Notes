##### How do you use comments in HTML?

```<!-- this is a HTML comment -->```


```
<!-- this is a
multiple line
HTML comment --> 
```


##### How do you use Paragraphs in HTML?
```<p> I went to YOUR mum's House. </p>```
*Result:* "I went to YOUR mum's House."


##### How do you use Line Breaks in HTML?
```<p> I went to YOUR <br/> mum's House. </p>```
*Result:* "I went to YOUR
mum's House."


##### How do you use Horizontal Lines in HTML?
```<p> I went to YOUR <hr/> mum's House. </p>```
*Result:* "I went to YOUR
***
mum's House."

***WARNING:***
*To be safe define <hr/> in CSS*


##### How do you use Headings in HTML?
```<h5> I went to YOUR mum's House. </h5>```
*Result:* 
##### "I went to YOUR mum's House."

```<h6> I went to YOUR mum's House. </h6>```
*Result:* 
###### "I went to YOUR mum's House."

*Headings are also important as search engines use the headings to index the structure and contents of your page and users skim read the headings in your page to find what they need*
**Headings are not used for displaying something in BOLD**


##### How do you use Unordered Lists in HTML?
```
<ul>
	<li> I went to </li>
	<li> YOUR </li>
	<li> mum's House.  </li>
</ul>
```

*Result:* 
- I went to
- YOUR
- mum's House.


##### How do you use Ordered Lists in HTML?
```
<ol>
	<li> I went to </li>
	<li> YOUR </li>
	<li> mum's House.  </li>
</ol>
```

*Result:* 
1. I went to
2. YOUR
3. mum's House.


##### How do you use Description Lists in HTML?
```
<dl>
	<dt> Where'd you go? </dt>
		<dd> YOUR mum's House. </dd>
	<dt> Why? </dt>
		<dd> She THICC. </dd>
</dl>
```

*Result:* 
- Where'd you go?
	- YOUR mum's House.
- Why?
	- She THICC.


##### How do you use Nested Lists in HTML?
```
<ol>
	<li> I went to </li>
		<ul>
			<li> YOUR </li>
		</ul>
	<li> mum's House.  </li>
</ol>
```

*Result:* 
1. I went to
	- YOUR
2. mum's House.


##### How do you use Images in HTML?
*Since the <img/> tag is empty element it requires no closing tag*

```
<img src="https://www.rd.com/wp-content/uploads/2019/05/4651445a-1.jpg" alt="MEOW MEOW"/>
```

![MEOW MEOW](http://upload.wikimedia.org/wikipedia/commons/6/68/Orange_tabby_cat_sitting_on_fallen_leaves-Hisashi-01A.jpg)


*The src attribute specifies the file containing the image and the alt attribute specifies the text to be displayed if the image is not there*

*Changing the size of the image using the width and height attributes*:

```
<img src="https://www.rd.com/wp-content/uploads/2019/05/4651445a-1.jpg" alt="MEOW MEOW" height="100" width="100"/>
```

![MEOW MEOW| 100 x 100](http://upload.wikimedia.org/wikipedia/commons/6/68/Orange_tabby_cat_sitting_on_fallen_leaves-Hisashi-01A.jpg)

This is a good idea since the browser then knows how much space to allocate to the image.


##### How do you use Links in HTML?
*The anchor element ```<a>...<a/> ``` provides a hyper text link between different documents or different parts of the same document*
```
<p> Big CAT
<a href = "http://upload.wikimedia.org/wikipedia/commons/6/68/Orange_tabby_cat_sitting_on_fallen_leaves-Hisashi-01A.jpg"> IS HERE </a>
</p>
```

*Result*: Big CAT [IS HERE](http://upload.wikimedia.org/wikipedia/commons/6/68/Orange_tabby_cat_sitting_on_fallen_leaves-Hisashi-01A.jpg)