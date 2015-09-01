isPrime :: (Integral a) => a -> [a] -> Bool
isPrime n (x:xs) = (x*x > n) || (n `mod` x /= 0) && (isPrime n xs)

main = print $ primes !! 10001
    where primes = 2 : filter (\x -> isPrime x primes) [3..]
