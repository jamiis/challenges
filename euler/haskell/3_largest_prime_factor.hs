isPrime :: (Integral a) => a -> Bool
isPrime n = factors n == [n,1]

factors :: (Integral a) => a -> [a]
factors n = [x | x <- [n,n-1..1], n `mod` x == 0]

primeFactors :: (Integral a) => a -> [a]
primeFactors n = [x | x <- factors n, isPrime x]

maxPrimeFactor :: (Integral a) => a -> a
maxPrimeFactor n = head $ primeFactors n

main = print . maxPrimeFactor 600851475143
