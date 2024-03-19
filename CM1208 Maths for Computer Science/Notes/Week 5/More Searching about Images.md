
### What is a Better way of of finding the Similarity between two Documents (than [[Searching and Trigonometric Functions]])? 

*What we can realise is that, when $\cos\theta = 0$ the two documents have no similarities, as $\theta = 90$, but when $\cos\theta = 1$ then the documents are identical, $\theta=0$. The closer $\cos\theta$ is to $0$ then the less similar the documents are.*

*This means that you can automate finding the similarity between two documents.*


### What are the Pros and Cons of using $\cos\theta$ Automatically?

**Pros**:
- *Can be fully automated.*
- *Can handle complex search queries.*
- *Gives similarity, thus allowing ranking of relevance.*

**Cons**:
- *Must have "exact" or nearly exact match to search terms.*
- *Does not consider semantics (meaning).*

*Yet this does not mean that this is enough for a page rank system.*


### What are some Definitions for Information Retrieval?

![[Pasted image 20240227184934.png]]
<sup>corpus, goal, query</sup>


### What is Query Expansion?

*The process of reformulating a given query in order to improve the performance of information retrieval, using such techniques as:*

1. *Finding synonyms of words and searching for these as well*
2. *Neutralising different morphological forms of words by stemming or lemmatising e.g. changing good to good/better/best*
3. *Fixed Spelling errors and automatically searching for the corrected forms*


### What is Indexing?

![[Pasted image 20240227191600.png]]


### What is the Inverted Index?
*A data structure use to store a mapping from content to its location in a document/documents*

![[Pasted image 20240227191711.png]]


### What are Stopwords?

*If every word in a corpus is indexed, then the index will increase in size, and the larger the index the slower the search therefore not all words should be stored as they are not all equally useful e.g. a, it, the etc*

*The Stopword list is a set of words which are not searchable such as a, it and the*

![[Pasted image 20240227191919.png]]


### What is Term Frequency?
*The relative importance of a word increases proportionally to the number of times it appears in a document, this includes the frequency a word is used in one specific document and in multiple documents*

#### What is Minimum Term Frequency?

*If a word fewer than $n$, specified by the algorithm, times then the word will not appear in the inverted index, where the idea is that if a word only appears once in a document it is not likely to be a useful source of information on that topic.*

### What is TF-IDF (Term Frequency-Inverse Document Frequency)?

1. ***TF** is as mentioned [[More Searching about Images#What is Term Frequency?|above]], but basically it is the idea that the relative importance of a word increases proportionally to the number of times it appears in the document.*

2. ***IDF** is the idea that the relative importance of a word decreases proportionally to the number of times it appears in the whole corpus of documents*

**TF is for one document and IDF is for multiple documents**.

**TF-DFI is**:
- *Highest when a word occurs many times within a small number of documents*
- *lower when the term occurs fewer times in a document, or occurs in many documents*
- *lowest when the term occurs in virtually all documents e.g. a, it, the*


#### What is the Algorithm for finding the weighting of a word, using TF-IDF?

$t = term$
$d = document$
$N =$ *total number of documents in the corpus*
$TF_{t,d} =$ *term frequency of $t$ in $d$*
$DF_t =$ *number of documents that contain $t$*
$TF-IDF_{t,d} = TF_{t,d}*log\frac{n}{DF_{t}}$ *Where the base of the log can be 10*


#### What is an Example of TF-IDF?

![[Pasted image 20240227193248.png]]![[Pasted image 20240227193258.png]]


### How do we Evaluate an Information Retrieval system?

![[Pasted image 20240227193439.png]]


#### What are the Measures of a Good IR system?

![[Pasted image 20240227193520.png]]
<sup>true positives, true negatives, false positives, false negatives</sup>


#### How can we Calculate the Precision and Recall of an IR system?

***Precision** is the fraction of retrieved documents that are relevant*
$$P = \frac{TP}{TP+FP}$$

***Recall** is the fraction of relevant documents that are retrieved*
$$R=\frac{TP}{TP+FN}$$

#### F-measure: Precision vs Recall...

- *Recall is a non-decreasing function of the number of documents retrieved, where you recall is high (and precision is low), by retrieving all the documents for all queries.*
- *Precision usually decreases as either the number of documents retrieved (or recall) increases, this is a result from strong empirical confirmation*

***F-measure**: is a combined measure that assesses the precision and recall trade off using a harmonic mean:*
$$F = \frac{2*P*R}{P+R}$$


### How do we Evaluate Large Search Engines?

![[Pasted image 20240227195646.png]]


### How does Google's Page Rank work?

![[Pasted image 20240227195718.png]]