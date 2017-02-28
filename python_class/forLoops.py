aList = ['apples','oranges','pineapples']

# What does the range function do?
whatIsRange = range(1,10)
whatIsRangeAgain = range(20,30)

print whatIsRange
print whatIsRangeAgain
# Type what you see here

# Count up to ten
for i in range(0,10):
  print i

# Looping through a list
for i in range(len(aList)):
    print 'value is %s' % aList[i]

# Looping through a list, another way
for index, value in enumerate(aList):
    print 'the index is %d' % index
    print 'the value is %s' % value
