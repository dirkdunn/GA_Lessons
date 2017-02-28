import sys

# name = raw_input('name input? > ')
#
# print 'Your name is: %s!' % name


# String splitting
print 'Hey there'[:-3]


print [1,2,3,4,5][-1]


print "interpolate this float %.1f" % .5

# reading / writing

test_file = open('file_to_read.txt','r+')

print test_file.mode
print test_file.read()

test_file.write('booga booga')
# test_file.write(bytes('blah blah blah', 'UTF-8'))
#
# print test_file.read()

# print 'hello sir'.replace(/hello/,'sir')
# print(age > 21 or age < 20)
# print('hola', ' sir', end="")
