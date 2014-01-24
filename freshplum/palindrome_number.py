# resources:
#   python documentations http://docs.python.org/2/library/itertools.html#itertools.permutations

from itertools import permutations

def next_palindrome_num(num):
    ret = num
    while True:
        ret = ret + 1
        if tuple(str(ret)) in permutations(str(num)):
            return ret

# test
print next_palindrome_num(38276)

