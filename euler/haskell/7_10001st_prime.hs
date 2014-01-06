primes = 2 : sieve [3,5..]
  where
    sieve (p:xs) = p : sieve [x | x <- xs, x `rem` p /= 0]
main = print $ primes!!10001
