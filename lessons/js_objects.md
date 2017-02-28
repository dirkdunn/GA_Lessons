# JS Objects
- Describe what an object is and how it differs from an array
- Describe what a key-value store is and why it is valuable as a data structure
- Define what object properties and methods are
- Contrast the JS object dot notation with bracket notation
- Explain what JSON is, what purpose it serves, and how it differs from Javascript object literals
- Explain the .hasOwnProperty method and why it is useful in iterating through object properties
- Explain Javascript 'context' and what the value of the 'this' keyword refers to
- Initialize an empty object using the object literal syntax
- Add properties to an existing object using the dot notation
- Add properties to an existing object using the bracket notation
- Create a JS object method inside an object literal
- Retrieve value from a property of an object using the dot notation
- Retrieve value from a property of an object using the bracket notation
- Use a for..in loop to iterate through the properties of an object

**What is an object? (5 min)**  
An object in JS is a data structure that is similar to a function that has things and can do things.

The parts that **do** things are called **methods** and the parts that **know** things are called attributes.

Objects are like functions in some ways in that they allow us to encapsulate our code in a more organized fashion

**Key Value Store**  
Objects use key's and  values to store their properties and methods.

Why is this valuable as a data structure?  It allows us to model things in real life and things with many things about them.


**Activity (5 min)**  
Think of anything, create a two split table and list the things that it does, and the things it has.

**Dot notation vs bracket notation**  
Two ways to access object properties, object.key and object["key"]

**Object Context "this"**  
JS "this" context refers to a keyword that is used inside of objects in order to refer to the object itself.

**Activity**
Let's make a calculator out of an object

**Object Literals**
Object literals are objects that don't need to be instantiated.

``` Javascript
var obj = {};
```

**for(i in obj**  
```Javascript
// still the foo from above
for(var i in foo) {
    if ( foo.hasOwnProperty(i) ) {
        console.log(i);
    }
}
```

**.hasOwnProperty**  
We need to use hasOwnProperty because it makes our code more stable, and prevent us from accessing

**What is JSON**  
Javascript Object notation, we can think of it as a way to transfer our objects from point A to point B.

**Public Vs Private Methods**

**Getters/Setters**

**Final Activity**  
Let's modify our game from our homework and convet it to using objects.

objects: Start, GameOver, Rooms, Player
