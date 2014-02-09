import Data.List
import Data.Maybe

-- infinite, ascending list of binary numbers, but with 9s in place of 1s
binary9s :: [Int]
binary9s = map binaryBoolsToBinary9s $ binaryBools :: [Int]
          -- an infinite list of lists of Bools representing the 1s and 0s of binary
    where binaryBools = iterate increment [True]
          -- function to increment the binary bool representation by 1 
          increment [] = []
          increment binary@(x:xs)
              | and binary = True : map not binary
              | and xs = map not binary
              | otherwise = x : increment xs
          -- converts list of Bools into binary9s (ie. 9, 90, 99, 900, ...)
          binaryBoolsToBinary9s = read . map (\b -> if b then '9' else '0')

-- list of binary9s multiples
binary9sMultiples :: [Int] -> [Int]
binary9sMultiples = map binary9sMultiple
    where binary9sMultiple n = fromJust $ find (`isMultiple` n) binary9s
          isMultiple x n = x `mod` n == 0

-- format input (first number is dropped), e.g. "3\n5\n7\n1" -> [5,7,1]
parse :: String -> [Int]
parse input = map read (tail $ lines input) :: [Int]

main = interact (unlines . map show . binary9sMultiples . parse)
