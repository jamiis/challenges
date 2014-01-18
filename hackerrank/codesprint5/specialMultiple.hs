import Data.List
import Data.Maybe

-- increment the binary bool representation by 1 
increment [] = []
increment binary@(x:xs)
    | and binary = True : map not binary
    | and xs = map not binary
    | otherwise = x : increment xs

-- an infinite list of lists of Bools representing the 1s and 0s of binary
binaryBools :: [[Bool]]
binaryBools = iterate increment [True]

-- converts doubly-nested list of Bools into "9"s and "0"s
nineify :: [[Bool]] -> [[Char]]
nineify = map (map (\b -> if b then '9' else '0'))

main = do
    contents <- getContents
        -- parse stdin to Int list
    let ns = map read . tail $ lines contents :: [Int]
        -- infinite, ascending list of binary numbers, but with 9s in place of 1s
        ninearys = map read . nineify $ binaryBools :: [Int]
        -- find nineary number that is a multiple of n
        ninearyMultiple n = fromJust $ find (\x -> x `mod` n == 0) ninearys
    mapM_ print (map ninearyMultiple ns) 

