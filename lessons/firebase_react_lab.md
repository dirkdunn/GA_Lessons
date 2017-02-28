# Firebase React Lab

**Let's extend our todo list by adding more functionality, and making it look better.**

**There's a couple things we will do to improve it's functionality and look:**

**1. Guard input against sending nothing**

As of right now, when we submit our form, we are automatically pushing the todo to our firebase.

What if instead of just pushing the todo to firebase, we wrapped it in an **IF** statement? What would that condition need to be?

**2. Add a time to the list item**  
Right now we are pushing our TODO list with two things: the list item, and the delete button. Let's add a third thing, the date when we added it.

``` javascript
// What is this? Check out the date object on W3schools
new Date().toLocaleString()
```

If using regular javascript for the date functionality seems irritating, or if you would like it formatted nicer, check out the **moment.js** library

Check out [moment.js](http://momentjs.com/)

**3. Add update functionality (optional)**  
So far we have the ability to add and delete items from our todo app what about including an update functionality?

Here is the method used to update a particular value:
``` javascript
firebase.ref.child('key').set('New value')
```

Insead of .remove() attached to our delete button, we attach .set() to set the data snapshot to a new value, on a new update button.


**HINT**
You'll need an input form somewhere on the screen that only shows up when you click the update button, you can show / hide this input in react when the update button is clicked

Check out this stack overflow post for reference:
[Hide / Show a component](http://stackoverflow.com/questions/24502898/show-or-hide-element)


**4. Add CSS / Bootstrap**  
Right now, the world's best todo list has some visual impediments. Let's prettify it with CSS!

Remember, with ReactJS, we include our CSS within the component , like such:

``` javascript
import './cssFile.css';
```

**Happy Hacking!**
