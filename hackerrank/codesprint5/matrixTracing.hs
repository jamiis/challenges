-- number of possible paths in an mxn matrix.
-- start: top-left. end: bottom-right. can only move right and down.
traces :: (Integral a) => a -> a -> a
traces m n = combos `div` repeats
    where rights  = n-1 -- required num of rights
          downs   = m-1 -- required num of downs
          combos  = product [1..(rights+downs)] -- all possible right/down combinations
          repeats = product [1..rights] * product [1..downs] -- quantity of repeats, e.g. R1 R2 D1 == R2 R1 D1

main = do
    contents <- getContents
        -- convert stdin to a list of lists of Ints
    let dimensions = map (map read . words) $ tail $ lines contents :: [[Integer]]
        -- map m x n pairs to trace quantity
        traces' = map (\[m,n] -> traces m n) dimensions
    mapM_ print traces'
