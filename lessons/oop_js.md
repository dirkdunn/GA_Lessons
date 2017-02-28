# OOP in Javascript Lesson

**Write on board**
- Reviewing objects, how they clean up the code
- Why not just type our code out like we have been already?
- Reviewing constructor functions
- Introducing Prototypes
- Separating & Organizing our code effectively
- Let's create some modules
- Namespacing, how does it work and why do it?
- Introducing some ES6

**Round 1**
- Reiterate the basic principles of OOP, and how they can help to clean up code
- Describe the drawbacks of spaghetti code/jQuery soup, and how to fix it
- Explain constructor functions & how to instantiate them
- Describe what prototypal inheritance is
- Describe what prototype chains are, and what is at the top of every chain

**Round 2**
- Convert a constructor to prototype
- Explain how separation of concerns applies to Javascript
- Organize JS code modularly into multiple files that rely on one another
- Namespace an application and objects properly
- ES6: 'class' keyword
- ES6: Inheritance with the 'extends' keyword

**Round 3**
- Review key concepts
- Open Q& A
- End Activity

**The entire lesson is done in an editor, hands on,  with each activity being to finish something that we are doing**

## Round 1

### Reviewing objects, how they clean up the code
- Review object literals, and why we use them
- Why do we use objects again?

### Why not just type our code out like we have been already?
- What is "Spaghetti Code"?
- How can we change this with objects?
- Let's visualize a new way to write javascript  
> Draw a diagram w/ modules & objects

### Reviewing constructor functions  
- Review constructor syntax & initialization
- Why use constructors over literals?  

Apply the KISS principle (Keep it simple, stupid). If you don't need anything beyond a simple container of data, go with a literal.

If you want to add behavior to your object, you can go with a constructor and add methods to the object during construction or give your class a prototype.

``` Javascript
function MyData(email, password, passwordConfirmation) {
    this.email = email;
    this.password = password;
    this.passwordConfirmation = passwordConfirmation;

    this.verify = function(){
        return this.password === this.passwordConfirmation;
    };

    this.validateEmail = function(){
      // TEST FORM
    };

    this.validatePassword = function(){
      // TEST FORM
    };

    this.signup = function(){
      // AJAX POST
    };
}
```

### Introducing Prototypes  
- What does "Inheritance" mean?

```Javascript
rabbit.__proto__ = animal 
```
- How do objects work with the prototypal inheritance chain?
Constructor objects have a prototype 

- What's the difference between 'this' and using prototype?
- Relating this back to datatype methods

## Round 2

### Let's convert this object to a prototype
- Take an existing object and convert everything besides instantiated properties to prototype.

### Separating & Organizing our code effectively
- How to approach making a program in an OOP fashion  

> Draw out each piece of your application  

### Namespacing, how does it work and why do it?
- What is namespacing, what is the window object?

Everything we have been defining so far has been defined under the window object.

By namespacing, we keep certain things private, so we don't have to overwrite over other peoples code.

### Let's create some modules
- What is a module?
- Why create them?
It helps organize our code further by seperating it into larger componenets, it also helps namespace

``` Javascript
var mod = (function(){
  return {
    //API
  };
})();
```

### Introducing some ES6

How can we write an object in ES6?

```javascript
class User  extends class{
  constructor(name, email, password, verifyPassword) {
    this.name = name
    this.email = email
    this.password = password;
    this.verifyPassword = verifyPassword
  }

  verify(){
    return this.password === this.verifyPassword
  }

  // Doesn't need to be instantiated
  static logSomething() {
    console.log('I can call this method without instantiating it.');
  }
}

```

## Round 3
- Review Key Concepts
- Open Q & A
- End Activity
