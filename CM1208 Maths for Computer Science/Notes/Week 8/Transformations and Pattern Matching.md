---
"Creation:": 2024-04-21 14:55
Modified: 2024-04-21 14:55
tags: Transformations and Pattern Matching
---
### Topic: Transforming Objects
#### Overview: 
*Brief overview of Transforming Objects*

### Definitions:



#### Subtopic 1 - How can we Transform Objects?

*Images can be transformed by applying the transformation to every point in the image.*

*Now to be able to rotate by $\theta^o$ anti-clockwise, the Transformation matrix is,*
![[Pasted image 20240421152314.png]]

*But how did we get that? Where the coordinates before transformation are $[^a_b]$ after rotations move along $x'$ by $a$ and move $y'$ by $b$.*

*$a'$: $a\cos\theta - b\sin\theta$*
*$b'$: $a\sin\theta + b\cos\theta$*

![[Pasted image 20240421152621.png]]

![[Pasted image 20240421152628.png]]

#### Subtopic 2 - What is a Horizontal Shear?

*This stretches the object horizontally, therefore the Transformation Matrix is,$[^{1 \text{ } m}_{0 \text{ } \text{ } 1}]$ *

![[Pasted image 20240421153232.png]]

*What is really happening?*
*$[1 \text{ } m]$ keeps the x and adds a multiple of y to it, where Shear is affected by where the point is vertically. Points high on the image will move a lot to the right, as they have a large y-value, and points close to the x-axis will only move a little bit, as they have a small y-value, and points below the x-axis will move to the left, as they have a negative y-value.*

*$[0\text{ } 1]$ keeps the y-value exactly the same*

*Shear can be used to show perspective, as shown below in the cube.*
![[Pasted image 20240421154634.png]]
*The top, bottom and sides of the cube are squares that have been sheared.*

#### Subtopic 3 - What is a Vertical Squeeze?

*It squishes the object towards the x-axis, thus making it "bulge out" (horizontally) and the Transformation Matrix is $[^{k \text{ } \text{ } 0}_{0 \text{ } \text{ } \frac{1}{k}}]$.*

![[Pasted image 20240421154916.png]]

*What is happening?*
*$[k \text{ }0]$ amplifies the x-value and ignores the y-value this is what causes the "bulge" effect.*

*$[0\text{ } \frac{1}{k}]$ shrinks the y-value and ignores the x-value and this is what causes the "squeeze" effect*

---

### Topic: Projection
#### Overview: 
*Brief overview of projection of an object*

### Definitions:



#### Subtopic 1 - What is Projection?

*Imagine shining a light onto your object, the object would cast a shadow onto the opposite side of where the light is coming from.*

#### Subtopic 2 - How do you Project onto a Certain axis?

*For projection onto the x or y axis, we only want to keep that type of axis and ignore the other.*

***

### Topic: Pattern Matching
#### Overview: 
*Brief overview of Pattern Matching*

### Definitions:



#### Subtopic 1 - How does Pattern Matching allow us to identity Fingerprints?

*We all know everyone has unique fingerprints, since even identical twins have different prints.*

*But Fingerprints do not match exactly, even from the same person, but there are distinct fingerprint "types" (you have a tented arch) where some fingerprint matching does not look ay the whole print, as it uses "minutiae" which is the places where the fingerprint ridges end, diverge etc.*

![[Pasted image 20240421170654.png]]

#### Subtopic 2 - How is Fingerprint Matched?

1. *Identify the/a minutiae pattern*
2. *Compare it to a potential match*
3. *Check relative positions*
4. *Forensics often use a point system, where 12 or more matched minutiae means a matched print*

***

### Topic: Facial Recognition
#### Overview: 
*Facial Recognition and how it works*

### Definitions:



#### Subtopic 1 - What makes a Face a Face?

*Although humans are good at recognising faces, our brains can sometimes make mistakes...*

![[Pasted image 20240421215241.png]]

![[Pasted image 20240421215251.png]]
*This is the Thatcher effect.*

#### Subtopic 2 - How does Facial Recognition on a Computer work?

*What features would a computer identify on a face? What problems might you have identifying each feature? How might you address these problems?*

*People can be individually recognised by using face shape, features such as spacing and size etc.*

#### Subtopic 3 - What are the Challenges of Facial Recognition?

- *If the person is in a profile?*
- *If someone grows facial hair?*
- *If someone gains or loses weight?*
- *Changes in facial expression?*
- *What if the picture is the wrong way round?*
- *What if the picture is a different size?*
- *What if the lighting is different?*

***

### Topic: Pattern Matching
#### Overview: 
*How do you identify the same object in two different images?*

### Definitions:



#### Subtopic 1 - How does Pattern Matching work, Step-by-Step?

1. *Identify the Potential Matches, this is the hardest part*
2. *Adjust the orientation and size*

#### Subtopic 2 - What is Template Matching?

*One approach of template matching is:*
1. *Start with a template of the object*
2. *Move it across the image, e.g. check how well it matches the image at each point.*
3. *Pick the best match*
*This only works if there is minimal variation between images.*

*Another approach is to look for features of the object e.g. the edges and corners of the object.*

***