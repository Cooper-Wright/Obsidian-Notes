![[[CM1210] Series 4 - Object Oriented Programming with Composition & Inheritance and Polymorphism.pdf]]


### What is Composition?
*Composition is the idea that one class is mentioned within another, e.g. if you have a class "Journey", it might include two "Location" classes*

*Composition exhibits a **"has-a"** relationship, as shown by the UML below,*

![[Pasted image 20240224145807.png]]


### What is Inheritance?
*Inheritance is an attempt to avoid duplication and reduce redundancy, where if an existing class has  some code needed by a new class, then derive the new class from the existing one*

*Inheritance exhibits a **"is-a"** relationship.*


#### What Object is at the top of the Hierarchy?

*The **"Object"** class.*


#### How does Inheritance Work?

![[Pasted image 20240224150450.png]]

*Classes in the Lower Hierarchy (Also known as a **Subclass** or **Child**), e.g. Trumpet etc, inherit all the variables and methods from the higher class (Also known as a **Superclass** or **Parent**), Instrument.*

*Each subclass inherits **ALL** variables and methods from its superclass, where the* <em><u>subclass is a "superset" of the superclass</u></em>.


#### How do we Create Classes that use Inheritance in Java?

``` java
class Trumpet extends Instrument {
	...
}
```

*Every subclass has one, and only one, direct superclass (Except for **"Object"** as every class is either a subclass of **Object** or a subclass of another Class).*

![[[CM1210] Series 4 - Object Oriented Programming with Composition & Inheritance and Polymorphism.pdf#page=11]]
![[[CM1210] Series 4 - Object Oriented Programming with Composition & Inheritance and Polymorphism.pdf#page=12]]


#### How does the Java Keyword "this" solve Ambiguity?

```java
this.variable // reference a variable from the class it is used in
```

*There is also the keyword "super", which refers to the parent classes variable or can be used like a function e.g.*

```java
super(method/variable) // references a method/variable from the superclass
```


### What is Polymorphism?
*The word "polymorphism" comes from the Greek words "poly", meaning "many", and "morphos", meaning "form", therefore polymorphism means "many forms"*

*Since a subclass inherits all the superclasses variables and methods, then the subclass could substitute the meanings of methods and variables, such as [[Overriding the toString() Method]] from the **Object** class.* **This is called** <strong><u>Substitutability</u></strong>.


#### What is Upcasting?

![[Pasted image 20240224153119.png]]

*e.g.*
```java
// Java program to demonstrate
// the concept of upcasting
// Animal Class

class Animal {
    String name;

    // A method to print the
    // nature of the class
    void nature()
    {
        System.out.println("Animal");
    }
}

// A Fish class which extends the
// animal class
class Fish extends Animal {
    String color;
    
    // Overriding the method to
    // print the nature of the class
    @Override
    void nature()
    {
        System.out.println("Aquatic Animal");
    }
}

// Demo class to understand
// the concept of upcasting
public class GFG {

    // Driver code
    public static void main(String[] args) {
        // Creating an object to represent
        // Parent p = new Child();
        Animal a = new Fish();

        // The object 'a' has access to
        // only the parent's properties.
        // That is, the colour property
        // cannot be accessed from 'a'
        a.name = "GoldFish";

        // This statement throws
        // a compile-time error
        // a.color = "Orange";
        // Creating an object to represent
        // Child c = new Child();
        Fish f = new Fish();

        // The object 'f' has access to
        // all the parent's properties
        // along with the child's properties.
        // That is, the colour property can
        // also be accessed from 'f'
        f.name = "Whale";
        f.color = "Blue";

        // Printing the 'a' properties
        System.out.println("Object a");
        System.out.println("Name: " + a.name);

        // This statement will not work
        // System.out.println("Fish1 Color" +a.color);
        // Access to child class - overridden method
        // using parent reference
        a.nature();

        // Printing the 'f' properties
        System.out.println("Object f");
        System.out.println("Name: " + f.name);
        System.out.println("Color: " + f.color);
        f.nature();

    }
}
```

![[Pasted image 20240224153623.png]]

![[[CM1210] Series 4 - Object Oriented Programming with Composition & Inheritance and Polymorphism.pdf#page=23]]


#### What is Downcasting?

![[Pasted image 20240224153732.png]]
![[[CM1210] Series 4 - Object Oriented Programming with Composition & Inheritance and Polymorphism.pdf#page=26]]


#### What is an Example Polymorphism?

![[[CM1210] Series 4 - Object Oriented Programming with Composition & Inheritance and Polymorphism.pdf#page=33]]

![[[CM1210] Series 4 - Object Oriented Programming with Composition & Inheritance and Polymorphism.pdf#page=35]]

![[[CM1210] Series 4 - Object Oriented Programming with Composition & Inheritance and Polymorphism.pdf#page=36]]

![[[CM1210] Series 4 - Object Oriented Programming with Composition & Inheritance and Polymorphism.pdf#page=37]]


#### But there is a Problem with the "getArea()" method...

*Since the "Shape" class has not way to work out the area, as each shapes area equation is different, therefore we use an **Abstract Class**.*


![[[CM1210] Series 4 - Object Oriented Programming with Composition & Inheritance and Polymorphism.pdf#page=39]]


### What is an Abstract Class?

*This is a class containing one or more abstract methods, where an abstract class must be declared with a class-modifier abstract.*

![[[CM1210] Series 4 - Object Oriented Programming with Composition & Inheritance and Polymorphism.pdf#page=41]]
![[[CM1210] Series 4 - Object Oriented Programming with Composition & Inheritance and Polymorphism.pdf#page=42]]

*As a summary, an abstract class provides a "template" for further development, and to provide a common interface*


### What is an Interface?

![[[CM1210] Series 4 - Object Oriented Programming with Composition & Inheritance and Polymorphism.pdf#page=46]]

```java
public interface Movable { 
// abstract methods to be implemented by the subclasses 
	public void moveUp();
	public void moveDown();
	public void moveLeft();
	public void moveRight(); 
}
```

*An interface is a 100% abstract class, therefore you do not need to use the "abstract" declaration.*


#### How do Subclasses derive from an Interface Class?

*They use the keyword "implements", as shown below,*

```java
public class SubclassName implements ImplementedSuperclassName {
	...
}
```


#### But, did you know One Subclass can Implement Multiple Interfaces...

```java
public class SubclassName implements ImplementedSuperclassNameOne, ImplementedSuperclassNameTwo, ... {
	...
}
```

![[[CM1210] Series 4 - Object Oriented Programming with Composition & Inheritance and Polymorphism.pdf#page=55]]





