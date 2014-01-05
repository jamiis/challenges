import Data.List
main = print $ find (isDivisibleByOneThrough 20) [1..]
    where isDivisibleByOneThrough m x = all (\a -> x `mod` a == 0) [1..m]
