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


###### TUPLES #######
####################

# Let's create a Tuple
myTuple = (1,2,3,4,5,5,5,'hello','tuples', True)

# Activity 1
print myTuple[0]
# Type here what you see

# Activity 2
# myTuple[0] = 'change the value of the first item'
print myTuple
# Type here what you see (Should be an error, what are we getting this error?)

# Activity 3
print myTuple.count(5)
# Type here what you see

# Activity 4
print myTuple.index('hello')
# Type here what you see

# Activity 5
print myTuple.index(5)
# Type here what you see

# Activity 6
print len(myTuple)
# Type here what you see


# A string with the value hello python!
myString = 'hello python!'

# Activity 1
myString[0]
print myString
# Type here what you see

# Activity 2
# myString[0] = 'B'
print myString
# Type here what you see, Did an error occur? What does this have in common with tuples?

# Activity 3
print myString.find('python')
# Type here what you see

# Activity 4
print myString.title()
# Type here what you see

# Activity 5
print myString.replace('python','anaconda')
# Type here what you see

# Activity 6
print myString.count('python')
# Type here what you see

# Activity 7
wood = 'How much wood could a woodchuck chuck if a woodchuck could chuck wood?'.count('wood')
chuck = 'How much wood could a woodchuck chuck if a woodchuck could chuck wood?'.count('chuck')

print wood == chuck
# Type here what you see, what is happening?
