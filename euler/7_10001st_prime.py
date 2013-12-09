'''
used sieve of eratosthenes technique

not sure how I could guarantee limit > some n-th prime, 
but in this special case I'm sure limit > 10,001st prime
'''

from collections import defaultdict

primes = []
is_composite = defaultdict(lambda: False)

# the 10,001st prime is less than limit
limit = pow(500,2)

i = 1
while len(primes) < 10001:
    # continue until next prime
    i = i + 1
    if is_composite[i]: continue

    # found a prime
    primes.append(i)

    # mark multiples of prime as composite
    multiple = i + i
    while multiple < limit:
        is_composite[multiple] = True
        multiple = multiple + i

print primes[-1]
