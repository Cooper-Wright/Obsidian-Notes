
##### What do Web Search Engines do?

*They rank the websites from the users search with documents that are relevant or have been "Paid for inclusion" or "Pay by click".*


##### How does the Engine work with the User?

![[Pasted image 20240103155208.png]]


##### How does the Search Engine find these Documents?

- *It uses a "crawler/spider 'robots'" to find web pages across the internet*
- *It then creates an index of found web documents (websites) with those that are advertised at the paid for position*
- *Then when given a query (something is searched), it uses the index to find docs that match the query terms*
- *Then ranks the found documents*


##### How does the "Crawler" find the Documents?

1. *It starts with a "seed" URLs*
2. It visits a URL
	- *Parse text / find hyperlinks*
	- *Place the found URLs on the queue to be visited (**URL Frontier**)*
- Repeat step 2 until there are no more unseen URLs


##### What is the URL Frontier?

![[Pasted image 20240103155812.png]]

*It is the space between the seen (easily accessed pages) and the unseen (private pages) of the web and links the two*


##### What are the issues with Crawling?

**Issues with Crawlers doing their job properly on the web:**
- *It is a massive task, needing multiple computers*
- *"Crawlers" need to be able not to get stuck in loops, both accidental and malicious*
- *There are websites with junk, meaning malicious links etc*
- *Duplicate pages*
- *How deeply should the pages be accessed?*
- *The web is continuously changing and thus these crawlers need to be constantly crawling*

**Issues with the Crawlers and their politeness:**
- *Obey the robots exclusion standards*
- *Do not hog a websites resources*


##### What is a Summary for the Crawling Process?

![[Pasted image 20240104123824.png]]


##### How should the Information in a page be Indexed?

- *Using all the words in the page*
- *Using relevant information from offset*

This can all be done with Inverted Index.


##### What is Inverted Index?

*Using a dictionary, when a word is search find all the documents that word, or an imprecise match (run -> run{ning}), occurs in.* 


##### What is an Example of Inverted Index?

*simple example:*
![[Pasted image 20240104124441.png]]

*example with word offsets:*
![[Pasted image 20240104124537.png]]


##### How are the Dictionaries Formatted?

![[Pasted image 20240104124713.png]]
*bare in mind the dictionaries values are normally alphabetical*


##### How is the index Constructed?

![[Pasted image 20240104124817.png]]

*In reality this index is **HUGE** and thus is stored across many machines, also there may be multiple versions of the index*


##### How are the Results from a Query Ranked?

*Although we do not officially know for each browser, as it would lead to abuse to get a page to the top, there is some idea of what it could be:*

![[Pasted image 20240104125241.png]]


##### What is the Importance of Linking and the "PageRank Algorithm"?

*It is the idea that the relevance of a page can be judged by **meta information**, which is the idea that the page of most importance is probably linked to the most over other websites*

![[Pasted image 20240104125700.png]]
![[Pasted image 20240104125746.png]]
![[Pasted image 20240104125835.png]]


##### What are the "Spam technologies" which try to Manipulate Rankings?

- *Cloaking:*
	- There are two versions of the document, the one for everyone and one just for the Search engine Spider. The one given to the Spider increases its ranking using many methods that may not look appealing to everyone.

- *Doorway Pages:*
	- Pages are optimised for a single keyword and then redirect the user to the real page, which usually is a commercial page.

- *Keyword Spam:*
	- These pages have excessive repetition of a term which are engineered "anchor text" and are hidden within the background colours

- *Link Spamming/Farms:*
	- These are multiple pages which point to one target thus increasing its ranking