# Complete the solution so that the function will break up camel casing, using a space between words.
# Example
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""

# test.assert_equals(solution("helloWorld"), "hello World")
# test.assert_equals(solution("camelCase"), "camel Case")
# test.assert_equals(solution("breakCamelCase"), "break Camel Case")


def solution(s):
    l = list(s)
    l1 = []
    for i in l:
        if i.istitle(): l1.append(' ')
        l1.append(i)
    return ''.join(l1)



# with regex:
import re
def solution(s):
    return re.sub('([A-Z])', r' \1', s)

# in one line:
def solution(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)
