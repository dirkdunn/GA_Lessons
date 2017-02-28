from sys import argv

fibLength = None
fileName, fibLength = argv

print fibLength

def fib(n,start=[1,1]):
    return start if n <= 0 else fib(n-1, start+[start[len(start)-1]+start[len(start)-2]])

print fib(int(fibLength) if fibLength != None else 50)
