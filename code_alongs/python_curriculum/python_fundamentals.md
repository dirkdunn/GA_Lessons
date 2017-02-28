# Python Fundamentals

#### Learning Objectives  
**By the end of this lesson you will be able to:**  
- Identify the differences between Javascript syntax and Python syntax
- Identify the differences between datatypes in Javascript, and datatypes in Python
- Use logical operators in Python
- Explain differences between strings, lists, and tuples in Python
- Use, and understand the basic methods of strings, lists, and tuples
- Use Conditionals when writing Python code
- Use loops when writing python code

#### Brief History Of Python
Python was created by the Dutch programmer **Guido van Rossum**, who currently works at Dropbox.

**Why the name "Python"?**  
The name of the language has no inherent meaning, it was simply named "Python" because the founder, Guido Van Rossum, was a fan of the BBC comedy series Monty Python's Flying Circus.
![Monty Python](https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcRPYnoh1HfeiYuwKn53vPm9ItARJLkG_KnkX4pDcCmyRnNfMsRB1w)


#### Why use Python?
- It's a easy and intuitive language, and just as powerful as it's major competitors
- It's open source, so anyone can contribute to its development
- It's made to be understandable as plain English
- It's suitable for everyday tasks, allowing for short development times

Python has grown to become a popular programming language. As of November 2011, it was the 3rd most popular language on the GitHub.

#### Python Versions  
There are two versions of python, Python 2, and Python 3.

For this class we will be using **python version 2.7**  
We are using Python 2.7 because it is currently used significantly more than Python 3.
[Python Version Usage Statistics](https://hynek.me/articles/python3-2016/)


#### Datatypes
The datatypes in python will mostly be the same as in Javascript, let's do some comparisons.

**Basic Primitive Datatypes**  
Primitive datatypes are the most basic forms of data in a programming language.

> "Prim" is a word part which derives from the latin word "primus", meaning first.

**Primitive datatypes in Python**  
**String** - An indexed collection of characters  
**Integers** - Whole numbers  
**Floats** - Floating point, or decimal number  
**Booleans** - A True or False value  
**None** - A representation of having no value, **this is the equivalent of "null" in javascript**

In the table below, we have the datatype name to the left, and two examples of the datatype to the right.

|     Datatype Name   | Example Usage    |     Example Usage        |
|:--------------:|-----------------------|-----------------------|
|     Strings    | 'Single quote string' | "Double quote string" |
| Booleans       | True                  | False                 |
| Integers       | 1      |             777          |
| Floating Point | 4.5       |          7.777             |
| None | None      |                       |

---
**Identifying differences in datatypes (5-10 minutes)**  
Do we see any differences here between what we remember from Javascript, and what we see here with Python?
**Is there anything missing?
Do any of the values look slightly different?**

Let's take a moment to write down at least difference that we notice before moving on and reviewing.
&nbsp;  
---
&nbsp;  
&nbsp;  
---
&nbsp;  
&nbsp;  
---

**Printing: Hello Python**  
``` python
print 'Hello, Python!'
print "Hello, double quotes! Same thing."
print 123
print True
print False
print "Hello, %s, any value: %r, and digits: %d" % ('string interpolation', True, 77)
print "s is for %s, r is for %r, and d is for digits: %d" % ('string', 'any value', 1)
```

**Comments**
```python
# Single line comments are w/ a hashtag
# Python doesn't read me!

''' We can do multi-line comments within triple quotes,
this is called a DOCSTRING
Python doesn't read me either!'''

docstr = '''We can also do
multi-line strings with docstrings'''

print docstr
```

**Variables**

```python
# Hello python
helloPy = 'Hello, python!'

# Printing variables
print helloPy

# Arithmatic
onePlusTwo = 1 + 2
print onePlusTwo

threeMinusTwo = 3 - 2
print threeMinusTwo

fourDivOne = 4 / 1
print fourDivOne

twoTimesThree = 2 * 3
print twoTimesThree

# Modulus
fiveModTwo = 5 % 2
print fiveModTwo

# Powering
fiveToTheSecondPower = 5**2
print fiveToTheSecondPower

threeToTheFourthPower = 3**4
print threeToTheFourthPower
```

**Logical Operators**  
Logical operators are how we are able to make decisions in a programming language.

Let's compare basic Python operators to Javascripts basic operators
You'll notice that some of these are the same, and some are different

**On the left is JavaScript, on the right is the Python equivalent.**

These are the basic logical operators of Python compared to Javascript, **Javascript is on the left, Python is on the right**, they are separted by a colon **:**

#### Javascript : Python


AND
&& : and
Javascript Example:
```javascript
var example = true && false;
```

Python Example:
``` python
example = True and False
```
OR
|| : or
Javascript Example:
```javascript
var example = true || false;
```
Python Example:
``` python
example = True or False
```
NOT
!something : not(something)
Javascript Example:
```javascript
var example = !true;
```

Python Example:
``` python
example = not(True)
```
Greater Than
\> : >
Javascript Example:
```javascript
var example = 5 > 4;
```
Python Example:
``` python
example = 5 > 4
```
Greater Than Or Equal To
\>== or >= : >=
Javascript Example:
```javascript
var example = 5 >== 4;
```
Python Example:
``` python
example = 5 >= 4
```

Less Than
< : <
Javascript Example:
```javascript
var example = 5 < 4;
```
Python Example:
``` python
example = 5 < 4
```
Less Than Or Equal To
<= or <== : <=

Javascript Example:
```javascript
var example = 5 <== 4;
```
Python Example:
``` python
example = 5 <= 4
```
Equal To
=== or == : ==
Javascript Example:
```javascript
var example = 5 === 4;
```
Python Example:
``` python
example = 5 == 4
```
Not Equal To
!== or != : !=
Javascript Example:
```javascript
var example = 5 !== 4;
```
Python Example:
``` python
example = 5 != 4
```


---
**Using Logical Operators In Python (15 minutes)**  
In the above block of code, we compare the logical operators of Javascript side by side with the equivalent logical operators of Python.

Based on the information above, let's write the Python code equivalent for each problem, set it to a variable, and then print it.

**Example Problem**
Five is greater than or equal to 7

**You will write in python code**
``` python
# Declare a variable with the correct logical operators, for this example we have "Five is greater than or equal to 7"
exampleVariable = 5 >= 7

# Once we do this, print the variable to the screen as such, and observe.
print exampleVariable
```

**Example Problem 2**
"hi" is equal to "hello"

**You will write in python code**
```python
stringComparison = "hi" == "hello"
print stringComparison
```

**Problem Set**
1. Six is greater than 7
2. 8 is greater than or equal to 6
3. 9 is less than or equal to 7
4. "hello" is equal to "hello"
5. "1" is equal to 1
6. 1 is equal to 1
7. "foo" is not equal to "bar"
8. Not True
9. Not False
10. True and False
11. True and True
12. False and False
13. True or False
14. False or False
15. True and Not True
16. Not False and Not False
---

#### Data Structures

**Do we remember what a data structure is?**
a data structure is a particular way of organizing data in a computer so that it can be used efficiently
&nbsp;  
---
&nbsp;  
&nbsp;  
---
&nbsp;  

**There are 6 built in data structures in python:**
In this lesson, we will be learning about **Strings, Tuples, and Lists**  
- **Lists** -  A mutable, indexed collection of data
- **Tuples** - A immutable, indexed collection of data
- **Strings** - A immutable, indexed collection of data
- Dictionaries
- Sets
- Frozen Sets

> We will be covering dictionaries later in the Python unit. We will not be covering Sets and Frozen sets this unit because they are not commonly used. However, if you are interested in learning more about sets and frozensets, you can refer to the Python documentation here for sets: https://docs.python.org/2/library/sets.html and here for frozen sets: https://docs.python.org/2.4/lib/types-set.html

&nbsp;

---
**Diving into data structures (25 minutes)**  
For this exercise, we will be typing in the code below into your REPL, and then typing into a comment what we observe for each problem.

**Example Problem**  
You type in the following code , and under it, in place of the "Type what you see" comment, you will type what you see.
``` python
# Let's create a list.
myList = [1,2,3,4,5,6]

# Activity 1
print myList[0]
# I see a '1' print in the console, this is because I am getting the first item out of the list, mind blowing!
```

**Lists**: A mutable, indexed collection of data

```python
# Let's create a list.
myList = [1,2,3,4,5,6]

# Activity 1
print myList[0]
# Type here what you see

# Activity 2
myList[0] = 'new value'
print myList
# Type here what you see

# Activity 3
myList.append(99)
print myList
# Type here what you see

# Activity 4
firstItem = myList.pop(0)
print firstItem
print myList
# Type here what you see

# Activity 5
lastItem = myList.pop();
print lastItem
print myList
# Type here what you see

# Activity 6
myList.insert(0,33)
print myList
# Type here what you see

# Activity 6.5
# Let's make another list
alphaList = ['a','booboo','baaa']

# Activity 7
alphaList.sort()
print alphaList
# Type here what you see

# Activity 8
alphaList.reverse()
print alphaList
# Type here what you see

# Activity 9
alphaList.remove('a')
print alphaList
# Type here what you see

# Activity 10
print len(alphaList)
# Type here what you see, what do you think "len" stands for?

```

**Tuples**: A immutable, indexed collection of data
``` python
# Let's create a Tuple
myTuple = (1,2,3,4,5,5,5,'hello','tuples', True)

# Activity 1
print myTuple[0]
# Type here what you see

# Activity 2
myTuple[0] = 'change the value of the first item'
# Type here what you see (Should be an error, what are we getting this error?)

# Activity 3
myTuple.count(5)
# Type here what you see

# Activity 4
myTuple.index('hello')
# Type here what you see

# Activity 5
myTuple.index(5)
# Type here what you see

# Activity 6
print len(myTuple)
# Type here what you see

```

**Strings**: A immutable, indexed collection of data
``` python
# A string with the value hello python!
myString = 'hello python!'

# Activity 1
myString[0]
print myString
# Type here what you see

# Activity 2
myString[0] = 'B'
# Type here what you see, Did an error occur? What does this have in common with tuples?

# Activity 3
myString.find('python')
# Type here what you see

# Activity 4
myString.title()
# Type here what you see

# Activity 5
myString.replace('python','anaconda')
# Type here what you see

# Activity 6
myString.count('python')
# Type here what you see

# Activity 7
wood = 'How much wood could a woodchuck chuck if a woodchuck could chuck wood?'.count('wood')
chuck = 'How much wood could a woodchuck chuck if a woodchuck could chuck wood?'.count('chuck')

print wood == chuck
# Type here what you see, what is happening?

```

#### Conditionals
Just like Javascript, Python also contains Coditional statements and loops, however, the syntax is different.

> Notice that there is no switch statement below, Python does not have a switch statement.

Let's type in the following code together into our REPL and observe what is happening.

``` python
if 4 > 2:
  print 'true story!'

# You can use parenthesis, but they are not necessary.
if (4 > 2):
  print 'true story!'
 ```
 Notice the indentations? This is called **pythonic syntax**

**WARNING**
Make sure all of your indentations are the same amount of spaces, for this reason, we will want to use the **TAB** key. If you do not make all of your indentations the same amount of spaces, you will get an error like such:

``` python
# If, Else If, and Else
if not(True):
    print 'Does If print?'
elif True:
    print 'Does else-if print?'
else:
    print 'Does else print?'

myList = [1,2,3,4]
myTuple = (1,2,3,4)

# What is "in"? What does it do?
if 1 in myList:
    print 'Do I print???'

if 4 in myTuple:
    print 'Does this one print too?'

if 5 not in myTuple:
    print 'Does this one print?'

```

``` bash
IndentationError: unexpected indent
```

An **IndentationError** occurs in python when the amount of spaces aren't all the same, you may have as many spaces as you wish, as long as they are all the same

#### Loops
FOR Loops
``` python
# Count up to ten
for i in range(1,10):
  print i
```

```enumerate()```

While Loops
``` python
number = 1
while number < 10:
  print number
  number++
```

---
**Final Activity: List Zipper (20 minutes)**
Type this code into your REPL:
``` python
listOne = [1,2,3,4,5,6]
listTwo = [6,5,4,3,3,1]
zippedList = []
```

For this problem, we will write some Python code to "zipper" the values from listOne and listTwo into zippedList, so that our zipped list will look as such:

``` python
print zippedArray
# [1,6,2,5,3,4,4,3,5,3,6,1]
```
