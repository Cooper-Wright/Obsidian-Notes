### What is the Purpose of Image Compression?
*To lower the memory required to store an item, ideally without loss of quality*


### How would Image Compression work if you were to "Zoom out" or Downsampling?

![[Pasted image 20240329140113.png]]


### What are some problems with Downsampling?

![[Pasted image 20240329140231.png]]


### What is Run-Length Encoding?

*A ‘run’ is a set of (horizontally) adjacentpixels with the same value*

*e.g.*
![[Pasted image 20240329140401.png]]

*But it does not always work well, e.g.*

![[Pasted image 20240329140443.png]]

*becomes*

![[Pasted image 20240329140456.png]]


### When does Run-Length Encoding work well?
- *Simple images*
- *Line drawings*
- *Icons*
- *etc*

*Whereas if the runs are too short, it can increase file size*


### Objects in the (Euclidean) Plane...

*Instead of looking at an image as a matrix of pixels we could consider each pixel as occupying a point in a 2D Euclidean Plane. This would allow us to perform more operations on the image.*

*e.g. Map an image onto a coordinate plane, where each pixel has a unique coordinate.*

![[Pasted image 20240402161134.png]]
![[Pasted image 20240402161144.png]]![[Pasted image 20240402161152.png]]

![[Pasted image 20240402161206.png]]
![[Pasted image 20240402161215.png]]

*If we think of our coordinates as a matrix $[^x_y]$ or a 2D column vector, then we can describe each of those transformations as a matrix, where we can multiply $[^x_y]$ by the transformation matrix to get the new coordinate $[^{x'}_{y'}]$.*

![[Pasted image 20240402161427.png]]

*If we multiply $[^a_b] * [^{0\;-1}_{1\; 0}]$ then we get:*

$(0)(a) + (-1)(b) = -b$
$(1)(a) + (0)(b) = a$
$= [^{-b}_a]$

![[Pasted image 20240402161909.png]]

*e.g.*
![[Pasted image 20240402161942.png]]


### How do you find the Matrix for Transformation?

![[Pasted image 20240402162023.png]]


### Linear Transformations...

*Each of these operations are called "linear transformations from* 
![[Pasted image 20240402162139.png]]

#### What does that Mean?

*Well ![[Pasted image 20240402162207.png]] is the real plane, aka the Euclidean Plane, which is a 2D space where each point is represented by $(x, y)$, which are both real numbers*


*Linear Transformations are a transformations by mapping one set to another set, e.g.*

$x$ $->$ $2x$  or $f(x) = 2x$

#### What are the Two Properties a Linear Transformation Satisfies?

$f(x + y) = f(x) + f(y)$ 
$f(ax) = af(x)$

*e.g.*
![[Pasted image 20240402162540.png]]


### How do we Multiply Larger Matrices?

*You extend the algorithm, which is done as follows:*

![[Pasted image 20240402162716.png]]![[Pasted image 20240402162722.png]]


#### What Must the Two Matrices follow to be able to Multiply?

*Their inner dimensions must match e.g.*

![[Pasted image 20240402162829.png]]

*The first matrices row must match the second matrices column*

#### Why does Order matter?

*For example a $2X3$ and a $3X5$ matrices can be multiplied but, the other way round they cannot as the row length of 2 does not match the column of 5*

*Basically if both matrices share a number for the length of a side, they can be multiplied.*


### The Identity Matrix...

*The Identity matrix is a Transformation that does not affect the original matrix and has ones in the diagonal from the top left to the bottom right and zeros in the other spaces*

*e.g.*
![[Pasted image 20240402163451.png]]![[Pasted image 20240402163509.png]]


### Properties of Matrix Multiplication...

![[Pasted image 20240402163558.png]]