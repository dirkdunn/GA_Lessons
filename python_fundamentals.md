# Python Fundamentals

#### Learning Objectives
- Set up their development environment for python
- Compare and contrast datatypes
- Compare and contrast logical operators
- Data Structures
- Conditionals
- Loops

#### Brief History Of Python

Python was created by the Dutch programmer **Guido van Rossum**, who currently works at Dropbox.

In 1999, Van Rossum submitted a funding proposal to DARPA(Defense Advanced Research Projects Agency) called Computer Programming for Everybody, in which he further defined his goals for Python:

- an easy and intuitive language just as powerful as major competitors
- open source, so anyone can contribute to its development
- code that is as understandable as plain English
- suitability for everyday tasks, allowing for short development times

Python has grown to become a popular programming language. As of November 2011, it was the 3rd most popular language on the GitHub

#### Setting up our environment
There are two version of python, Python 2, and Python 3.

For this class we will be using **python version 2.7**
[Python Version Usage Statistics](https://hynek.me/articles/python3-2016/)

Check your python version by typing
``` bash
python --version
```

You should get a response like such:
``` bash
Python 2.7.13
```

If this is not the case, [you may download Python 2.7 here](https://www.python.org/downloads/)


**PIP**
For python package management , we use the PIP command line tool (PIP stands for Pip Installs Python or PIP Installs Packages), we can install it as such:

``` bash
sudo easy_install pip
```

#### Datatypes & Expressions
The datatypes & expressions in python will mostly be the same as in Javascript, let's do some translations:

**Comments**  
```python
# Single line comments are w/ a hashtag
''' We can do multi-line comments within triple quotes (DOCSTRINGS) '''
```

**Expressions**
```python
# Arithmatic
1 + 2
3 - 2
4 / 1
2 * 3

# Modulus
5 % 2

# Square
5**2
```

**Logical Operators**
On the left is JS, the right is the Python equivalent
```
&& = and
|| = or
!variableName = not(variableName)
```

#### Data Structures  

**Do we remember what a data structure is?**  
a data structure is a particular way of organizing data in a computer so that it can be used efficiently

There are X built in data structures in python:  

**Lists**: A mutable, indexed collection of data  

```python
# Let's create a list.
myList = [1,2,3,4,5,6]

# Add a value to the end of a list
myList.append(99)
>>> [1,2,3,4,5,6,99]

# Pop the first value off of the list
firstItem = myList.pop(0)
# firstItem is now 1

# Pop takes the last item by default
lastItem = myList.pop();
# lastItem is now 99

# Insert the number 33 at the 0th index (the beginning)
myList.insert(0,33)
# myList is now [33,1,2,3,4...]

# Sorting, this works numerically and alphabetically
alphaList = ['a','booboo','baaa']
# ['a', 'booboo', 'baaa']

alphaList.sort()
# ['a', 'baaa', 'booboo']

# Reversing simply reverses the list
alphaList.reverse() 

# Remove an item from a list
alphaList.remove('a')
# ['booboo','baaa']
```

**Tuples**: A immutable, indexed collection of data
``` python

```  
**Sets**: A mutable, unordered collection of unique data  
``` python
```  
**Frozen Sets**: A immutable, unordered collection of unique data  
``` python
```  
**Strings**: A immutable, indexed collection of data
``` python
```  

#### Conditionals
IF conditions in python are written like such:

``` python
if 4 > 2:
  print 'true story!'

# You can use parenthesis, but they are not necessary.
if (4 > 2):
  print 'true story!'

```

#### Loops
FOR Loops
``` python
# Count up to ten
for i in range(1,10):
  print i
```

While Loops
``` python
number = 1
while number < 10:
  print number
  number++
```


#### Functions

Unlike javascript, which uses the ```function``` keyword, python uses ```def```, which stands for **define**, as in define a function.

``` python
def adder(a,b):
  return a + b
```

Notice the indentations? This is considered **pythonic syntax**

**WARNING**
Make sure all of your indentations are the same amount of spaces, for this reason, we will want to use the **TAB** key. If you do not make all of your indentations the same amount of spaces, you will get an error like such:

``` bash
IndentationError: unexpected indent
```

An **IndentationError** occurs in python when the amount of spaces aren't all the same, you may have as many spaces as you wish, as long as they are all the same
