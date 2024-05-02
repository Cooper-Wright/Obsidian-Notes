*A set of statements to solve some subproblem should be coded as a method.*

![[Pasted image 20240207180506.png]]
<sup>Now let's write this in repeating part (DRY) into a method</sup>

### First, What is the General form of a Static Method?

![[Pasted image 20240207180830.png]]


### What are the Different types of Static Methods?

![[Pasted image 20240207180715.png]]


### What happens to Primitive Variables that are Changed within Methods?

**NOTHING, as it is out of the scope of the prior method so therefore the primitive value does not change.**

``` java
public class PrimitiveArguments {

   public static void main( String[] args ) {

      int i = 0;

      System.out.println( "Before someMethod i = " + i );

      someMethod( i );

      System.out.println( "After someMethod i = " + i );

   }

  

   static void someMethod( int a ) {

      System.out.println( "   In someMethod a = " + a );

      a++;

      System.out.println( "   In someMethod a = " + a );

   }

}
```
******
```
Before someMethod i = 0
   In someMethod a = 0
   In someMethod a = 1
After someMethod i = 0
```


### What happens if you Change an Object Value and if you try to return a variable with the same Name but Different Value?

``` java
public class ReferenceArguments {

   public static void main( String[] args ) {

      java.awt.Point p = new java.awt.Point( 20, 20 );

      System.out.println( "Before someMethod p = " + p );

      someMethod( p );

      System.out.println( "After someMethod p = " + p );

      someOtherMethod( p );

      System.out.println( "After someOtherMethod p = " + p );

   }

  

   static void someMethod( java.awt.Point q ) {

      System.out.println( "   On entering someMethod q = " + q );

      q.translate( 10, 10 );

      System.out.println( "   On leaving someMethod q = " + q );

   }

  

   static void someOtherMethod( java.awt.Point q ) {

      System.out.println( "   On entering someOtherMethod q = " + q );

      q = new java.awt.Point( 50, 50 );

      System.out.println( "   In someOtherMethod q = " + q );

      q.translate( 10, 10 );

      System.out.println( "   On leaving someOtherMethod q = " + q );

   }

}
```
******
```
Before someMethod p = java.awt.Point[x=20,y=20]
   On entering someMethod q = java.awt.Point[x=20,y=20]
   On leaving someMethod q = java.awt.Point[x=30,y=30]
After someMethod p = java.awt.Point[x=30,y=30]
   On entering someOtherMethod q = java.awt.Point[x=30,y=30]
   In someOtherMethod q = java.awt.Point[x=50,y=50]
   On leaving someOtherMethod q = java.awt.Point[x=60,y=60]
After someOtherMethod p = java.awt.Point[x=30,y=30]
```

