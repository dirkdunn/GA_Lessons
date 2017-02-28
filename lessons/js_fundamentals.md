# Javascript Fundamentals

-	Explain what a programming language is
-	Explain what JavaScript is and how it fits into front end web development
-	Explain what variables are and why they are useful in a program.
-	 Create a variable and assign a value to it
-	Use common operators with variables and literals for arithmetic, string concatenation, and assigning values to variables
-	Explain the difference between expressions and statements
-	Explain what arrays are and why they’re are needed
-	List some useful array helper methods
-	Explain what functions are and why they are useful in a program
-	Describe the role of the ‘return’ keyword and it’s importance to functions.
-	Describe what arguments and parameters are, and their importance to functions.
-	Declare a named function and a return value
-	Call a named function and store a value in a variable
-	Use console.log() to debug information

### I DO

**Set up HTML file, include javascript**

**What is a programming language, and how do they work?**  (5 min)  
A special language programmers use to develop programs on the computer. It provides instructions to the computer to execute.

**What is JavaScript? What role does it play in web development** (5 min)  
Javascript is the programming language of the web. It's what defines the behavior and handles the interactions of our web apps.

**What are primitive data types?**  (5 min)  
Primitive data types are the types of data that come built into the programming language, these include.
(Go over each primitive data types).

- Boolean
- Null
- Undefined
- Number (Integers & Floats)
- String

### WE DO

**Variables** (15 min)  
Variables are simply a name for something in our code. We use them to make our code read more like english, and to avoid typing the same thing multiple times.

```Javascript
/*
Multi line
comment
*/

// Single line comment , you can't read me
var helloWorld = "Hello, World!";
var ten = 10;
var sixPlusFive = 6 + 5;
var sixGtFive = 6 > 5;
var n = null;
var und = undefined;

console.log(helloWorld);
console.log(ten);
console.log(sixPlusFive);
console.log(sixGTFive);
console.log(n);
console.log(und);
```

**You can use operators to do things with variables.**  (25  min)
``` Javascript
console.log("hi" === "hi");
console.log(1 === 1);
console.log(1 !== 1);
console.log(1 === 2);
console.log(5 < 7);
console.log(7 <= 7);
console.log(9 >= 9);
console.log("This is string " + "concatenation");
console.log("adding " + "multiple " + "string " + "together");
console.log(5 - 4);
console.log(6 / 3)
console.log(6 / 4);

// Modulus
console.log(6 % 2);
console.log(6 % 2 === 0);
console.log(6 % 4);
console.log(6 % 4 === 1);

// The OR operator
console.log( 5+5 === 10 || 5+5 === 9);

// The AND operator
console.log( 5+5 === 10 && 5+5 === 9);

> Explain Camel Case

```
Let's learn logic

**Activity**  
Let's practice basic logic (15 minutes)

**TRUE AND TRUE === ?**  
**TRUE AND FALSE**  
**FALSE AND FALSE**  
**TRUE OR TRUE**  
**TRUE OR FALSE**  
**FALSE OR TRUE**  
**FALSE OR FALSE**

**Break (10 min)**

### Arrays & Array Methods (30 minutes)
An array is a data type that can hold multiple pieces of information.

``` Javascript
var arr = [1,2,3,4,5];
var names = ["Joey","James","Peter"];

// accessing information from arrays
console.log("My name is " + names[1]);

```

**Array Methods**
- push
- pop
- concat
- shift
- unshift
- concat
- slice
- splice

**Write JS methods with arrays**


### Expressions VS statements (10 min)
Expressions produce a value, it is evaluated into something else.  

``` Javascript
// Expressions
5 * 3
6 % 2 == 0
// etc..
```  
Statements perform an action, it is essentially a set of instructions to carry something out.
``` Javascript
var statement = 'I have performed the action of creating a variable';
var arr = ["I", "have created", "an array", 5, 'Hoorah!'];
```

**Break (10 min)**

### Functions  
Functions are a way to take code we write and encapsulate it into something that we can refer to.

``` Javascript
function tenPlusFive(){
  var ten = 10;
  var five = 5;
  console.log(ten + 5);
}
```

** Returning Values & Arguments**
``` Javascript
function adder(first, second){
  return first + second;
}

console.log(adder(1,3));
```
**Arguments**  
Arguments are things that we can provide to our functions that it can manipulate.

Because of arguments we can create functions like adder that can take any two numbers, instead of having to write a seperate function.

**Why return things?**  
When we build programs it is always a good idea to seperate what we want to do into functions that do and return something.  

What will eventually happen is functions will communicate with other functions, so that we don't have a huge pile of code into one place.


**What is DRY?**

### YOU DO (Filler Final)  
Let's group in teams create a calculator page with multiple functions that do different things that can be called. We created an adder function earlier, let's make other functions that do calculations.
