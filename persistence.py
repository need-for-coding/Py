# Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

# For example (Input --> Output):

# 39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
# 999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
# 4 --> 0 (because 4 is already a one-digit number)

My solution:
def persistence(n):
    counter = 0
    arr = list(str(n))
    while True:
        x = 1
        if len(arr) > 1:
            for i in arr:
                x *= int(i)
            counter += 1
            arr = list(str(x))
            print(arr)
        else:
            return counter
          
 # Best practices:
import operator
def persistence(n):
    i = 0
    while n>=10:
        n=reduce(operator.mul,[int(x) for x in str(n)],1)
        i+=1
    return i
