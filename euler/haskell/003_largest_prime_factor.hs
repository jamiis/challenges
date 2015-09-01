import Data.List

isPrime :: (Integral a) => a -> Bool
isPrime n = factors n == [n,1]

factors :: (Integral a) => a -> [a]
factors n = reverse. sort $ concat [[d, n `div` d] | d <- [1..square], n `mod` d == 0]
    where square = round . sqrt $ fromIntegral n

primeFactors :: (Integral a) => a -> [a]
primeFactors n = [x | x <- factors n, isPrime x]

maxPrimeFactor :: (Integral a) => a -> a
maxPrimeFactor n = head $ primeFactors n

main = print $ maxPrimeFactor 600851475143
