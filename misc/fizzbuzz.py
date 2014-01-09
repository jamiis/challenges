#!/usr/bin/python

def fizzbuzz(n):
    '''Print out numbers 1 to n inclusive. If the number is
    divisible by 3, print "Fizz" instead of the number.
    If the number is divisible by 5, print "Buzz" instead of
    the number. If divisible by 3 and 5, print "FizzBuzz".
    '''
    assert type(n) is int
    assert n > 1
    # accumulate terms to be printed into a list
    printlist = []
    for num in xrange(1, n+1):
        # if conditions are met, build "FizzBuzz" string
        msg = ""
        if num % 3 == 0: msg += "Fizz"
        if num % 5 == 0: msg += "Buzz"
        # add fizzbuzz to printlist if truthy, else append the number
        printlist.append(msg or str(num))
    # output: "1, 2, Fizz, 4, Buzz, ... `n`"
    print ", ".join(printlist)

if __name__ == "__main__":
    fizzbuzz(100)
