-- special mod. only happens if x > n.
mod' :: (Integral a) => a -> a -> a
x `mod'` n
    | x > n     = x `mod` n
    | otherwise = x

-- take all even indices of a list. utility fcn for parsing stdin.
evens [] = []
evens l@(x:xs)
    | even $ length l = evens xs
    | otherwise = x : evens xs

-- get list of all cells in hyperrectangle
-- e.g. [2,2] outputs [ [1,1], [1,2], [2,1], [2,2] ]
cells :: (Integral a) => [a] -> [[a]]
cells = mapM (enumFromTo 1)

-- finds the gcd of each cell, then sums all gcds
sumGcds :: (Integral a) => [[a]] -> a
sumGcds = sum . map (foldl1 gcd)

main = do
    contents <- getContents
        -- parse stdin to list of hyperrectangle dimensions, e.g. [ [2,2], [3,3,4], [20,1] ]
    let rects = map (map read . words) . evens . tail $ lines contents :: [[Integer]]
        -- list of each hyperrectangle's summed gcds
        gcdsums = map (sumGcds . cells) rects
    mapM_ print gcdsums
