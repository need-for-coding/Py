# Write a function toWeirdCase (weirdcase in Ruby) that accepts a string, and returns the same string 
# with all even indexed characters in each word upper cased, and all odd indexed characters in each word lower cased. 
# The indexing just explained is zero based, so the zero-ith index is even, therefore that character 
# should be upper cased and you need to start over for each word.

# The passed in string will only consist of alphabetical characters and spaces(' '). 
# Spaces will only be present if there are multiple words. Words will be separated by a single space(' ').

# Examples:
# to_weird_case('String'); # => returns 'StRiNg'
# to_weird_case('Weird string case') # => returns 'WeIrD StRiNg CaSe'

# My solution:
def to_weird_case(string):
    arr = string.split()
    newArr = []
    for i in arr:
        s = ''
        for j in range(len(i)):
            if j % 2 == 0:
                s += i[j].upper()
            else:
                s += i[j].lower()
        newArr.append(s)
    return ' '.join(newArr)
  
#Smarte ways:
def to_weird_case(string):
    recase = lambda s: "".join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(s)])
    return " ".join([recase(word) for word in string.split(" ")])

def to_weird_case(string):
    return ' '.join([''.join([y.lower() if i%2 else y.upper() for i, y in enumerate(x)]) for x in string.split()])
    
