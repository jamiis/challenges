import Data.List (find)

factors :: (Integral a) => a -> [a]
factors n = concat [[d, n `div` d] | d <- [1..square], n `mod` d == 0]
    where square = round . sqrt $ fromIntegral n

triangles :: [Int]
triangles = scanl (+) 1 [2..]

main = print $ find (\x -> length (factors x) > 500) triangles
