'''
Addition of two numbers with high precision: input is a string in the format of "A+B" where A and B are 
float numbers with high precision (e.g., 1.234567890123456789012345678901234567890...). 
Output is a string that represents the result.

NOTE: IMO this was a poor solution but I want to preserve how I implemented it.
      If I had another chance I would have figured out a way to not have to make the
      float-strings the same length. that was dumb and time consuming.
'''
# resources
#   replicate string: http://stackoverflow.com/a/19934971/939971
#   forgot how to use reverse: http://stackoverflow.com/a/3705676/939971

def same_len(A, B):
    ''' format A and B to equal length on both sides of the decimal '''
    
    def add_zeros(A,B, prepend=False):
        ''' helper fcn that returns equal length A and B by appending or prepending 0s to the shorter parameter'''
        diff = len(A) - len(B)
        if diff < 0:
            A = A + "0"*(-diff) if not prepend else "0"*(-diff) + A
        if diff > 0:
            B = B + "0"*diff if not prepend else "0"*diff + B
        return A,B
    
    zipped = zip(A.split("."), B.split("."))
    A = B = ""
    # rebuild A and B after making the before and after decimal segments the same length
    for a,b in [add_zeros(*zipped[0],prepend=True), (".","."), add_zeros(*zipped[1])]:
        A = A + a
        B = B + b
    return A,B
    
def add(A,B):
    sum = ""
    carry = "0"
    A,B = same_len(A,B)
    
    # iterate through in reverse because we add from right to left
    for a,b in zip(A,B)[::-1]:
        if a == ".":
            sum = sum + "."
            continue
        
        # add together digits and the amount carried
        added = str(int(a) + int(b) + int(carry))
        
        # do we need to carry a value?
        if len(added) > 1:
            carry = added[0]
            added = added[1]
        else:
            carry = "0"
        
        # append new decimal place to sum
        sum = sum + str(added)
    
    # re-reverse sum before returning
    return sum[::-1]
    
# test
print add(A="1.55", B="10.5")
print add(A=".55",  B="10.5")
print add(A="1.0",  B="1.5001")
print add(A="1.",   B="1.50")
