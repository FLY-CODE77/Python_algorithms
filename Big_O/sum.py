# problem 
# Take an input of n and return the sum of the numbers from 0 to n

def sum1(n):
    final = 0
    for i in range(n+1):
       final = final + i
    return final

def sum2(n):
    return (n*(n+1))/2

# which code is better?? how do i compare them.
# first time check
import timeit

def timecheck(n):
    start = timeit.default_timer()
    for i in range(n*1000):
        sum1(5)
    stop = timeit.default_timer()
    print(stop - start)
timecheck(100)


def timecheck(n):
    start = timeit.default_timer()
    for i in range(n*1000):
        sum2(5)
    stop = timeit.default_timer()
    print(stop - start)
timecheck(100)

