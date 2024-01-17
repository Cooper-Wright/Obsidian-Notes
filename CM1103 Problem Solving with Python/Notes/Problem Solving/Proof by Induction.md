
##### What is a Propositional function?
*A function P(x) that returns either true or false depending on the parameter x*


##### What is Mathematical induction (weak)?
*To prove a Propositional function P(n) is true for all positive integers n,*

**This is done in two steps:**
1. **Basic step:** *Show that one value of n is true, e.g. P(1) is true etc*
2. **Inductive step:** *Show that P(k) is true if P(k-1) is true*


##### What is an Example of this?
*The sum of the first n odd numbers is,* $$n^2$$
 *Let P(x) be the proposition that the sum of the first x odd numbers be equal to x^2 (for x >= 1)*
 
 **Basic step:** 
*P(1) is true as,*
$$1 = 1^2$$

**Inductive step:**
***Assume P(k-1) is true**, therefore the sum of the first k-1 odd numbers is equal to (k-1)^2.*

*The kth odd number is 2k-1 (nth odd number is 2n-1), therefore the sum for the kth odd numbers is,*

$$1+3+...+(2(k-1)-1)+(2k-1)$$

*Due to our previous assumption, we can assume all the odd numbers before and including k-1 are equal to,* $$(k-1)^2$$
*Therefore the sum for the kth odd numbers is,* $$= (k-1)^2 + (2k-1)$$ $$= k^2 - 2k + 1 + 2k - 1$$
$$=k^2$$


##### What is another example of this?
*Prove by Induction that,* $$P(n) = (1+2+3+...+n) = n(n+1)/2$$
**Basic step:**
$$P(1) = 1 = 1(1+1)/2 = 2/2 = 1$$
**Inductive step:**
*==Assume P(k-1) is true,== therefore,* $$P(k-1) = (1+2+3+...+(k-1)) = ((k-1)(k-1+1))/2$$
*Expand the brackets fully on the right side*
$$P(k-1) = (1+2+3+...+k-1) = (k^2 - k)/2$$
*Therefore, P(k) is,* $$P(k) = (1+2+3+...+k-1+k) = k(k+1)/2 = (k^2+k)/2$$
*Now since we can "take out" P(k-1) it becomes,* $$P(k) = (k^2-k)/2+k = (k^2+k)/2$$
$$P(k) = (k^2-k + 2k)/2 = (k^2+k)/2 = (k^2+k)/2$$
*Therefore P(k) is true.*