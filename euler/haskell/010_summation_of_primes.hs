isPrime :: (Integral a) => a -> [a] -> Bool
isPrime n (x:xs) = (x*x > n) || (n `mod` x /= 0) && (isPrime n xs)

primes = 2 : filter (\x -> isPrime x primes) [3..]

main = print $ sum $ takeWhile (<2000000) primes
