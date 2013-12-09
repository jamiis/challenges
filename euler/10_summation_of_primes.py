from collections import defaultdict

primes = []
is_composite = defaultdict(lambda: False)
limit = 2000000

i = 1
while i < limit:
    # continue until next prime
    i = i + 1
    if is_composite[i]: continue

    # found a prime
    print i
    primes.append(i)

    # mark multiples of prime as composite
    multiple = i + i
    while multiple <= limit:
        is_composite[multiple] = True
        multiple = multiple + i

print sum(primes)
