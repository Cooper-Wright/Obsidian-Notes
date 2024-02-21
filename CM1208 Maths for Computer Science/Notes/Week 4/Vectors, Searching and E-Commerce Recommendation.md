
### What is the Scalar Product (aka Dot Product)?

*Where* $$u.v = \sum_{i=1}^n u_i v_i$$
*The Scalar Product takes two vectors and assigns them a real number, this can be **used to find the length of a vector**.*


### What is the Norm of a Vector?

*The length of a vector, v, is called its norm and is notated as,* $||v||$

*To find the Norm we can use **Pythagoras' Theorem**,*
![[Pasted image 20240220135155.png]]

*and can be used as such,*
![[Pasted image 20240220135225.png]]


*Therefore we see that $||v||$ is equal to $\sqrt {v.v}$ meaning that the norm of a vector, v, is equal to the square root of the dot product of v and v.*


### How can we find the Angles between Two Vectors?

![[Pasted image 20240220135632.png]]

*$v.w = ||v||*||w||*cos \theta$*


#### What is an Example of this?

![[Pasted image 20240220140310.png]]
![[Pasted image 20240220140322.png]]

#### What is it Called when the angle between Two Vectors is at a Right Angle?

*It is called an **orthogonal**.*


### How does this Relate to [[Document Matching]]?

*Well we can use the angle between two vectors to determine how similar they are, the smaller $\theta$ is the more similar they are. With this way of comparing vectors we can represent each document with a vector and calculate how similar they are.*

#### What is an Example of this?

![[Pasted image 20240220140617.png]]![[Pasted image 20240220140626.png]]
![[Pasted image 20240220140636.png]]
![[Pasted image 20240220140647.png]]
![[Pasted image 20240220140657.png]]
![[Pasted image 20240220140708.png]]
![[Pasted image 20240220140720.png]]


### How could this be used for Searching?

- *Write the search query as a vector.*
- *1 if the word in the dictionary appears in the query and 0 otherwise.*
- *Find the similarity between the search term vector and each document.*


### How does E-Commerce Recommendation Work?

![[Pasted image 20240220142216.png]]

#### What are the Practical Issues with E-Commerce Recommendations?

- *Scalability: There are millions of customers and million of catalogue items.*
- *Quick Response: Typically the Response time should be under a second.*


#### What are the Two Approaches to Filtering?

1. **[[Vectors, Searching and E-Commerce Recommendation#Traditional Collaborative Filtering|Traditional Collaborative Filtering]]**
2. **[[Vectors, Searching and E-Commerce Recommendation#Item-to-Item Collaborative Filtering|Item-to-Item Collaborative Filtering]]**


### Traditional Collaborative Filtering

*These filtering treats items as words in the dictionaries above and treats a customers behaviour (bought or didn't buy it) as the content of a document.*

*e.g.*

![[Pasted image 20240220143711.png]]
![[Pasted image 20240220143724.png]]

![[Pasted image 20240220143906.png]]

#### What are the Problems with this Filtering?

1. *The online stage is very time consuming.*
2. *It does not scale well with many customers and catalogue items.*

### Item-to-Item Collaborative Filtering
*This is the method used by **Amazon**.*

*This Filtering treats each customer as a word in the dictionary and each item as a vector. Pre-compute the pairwise relation between any two items using similar angle definition. Combine the list of items that have high correlation.*

![[Pasted image 20240220143711.png]]
![[Pasted image 20240220144222.png]]


### What are the Benefits of Item-to-item Collaborative Filtering?

1. *Pairwise relation between items can be pre-computed (offline)*
2. *Online cost is low.*
3. *Has a good Scalability*