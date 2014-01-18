-- number of possible paths in an mxn matrix.
-- start: top-left. end: bottom-right. can only move right and down.
traces :: (Integral a) => a -> a -> a
traces m n = product [bigger+1..moves] `div` product [1..smaller]
    where rights = n-1 -- required num of rights
          downs  = m-1 -- required num of downs
          moves  = rights + downs -- total number of moves required
          -- find the bigger dimension to speedup division above
          (bigger, smaller) = if rights > downs then (rights,downs) else (downs,rights)

-- special mod. only happens if x > n.
mod' :: (Integral a) => a -> a -> a
x `mod'` n
    | x > n     = x `mod` n
    | otherwise = x

main = do
    contents <- getContents
        -- convert stdin to a list of lists of Ints
    let dimensions = map (map read . words) $ tail $ lines contents :: [[Integer]]
        -- map m x n pairs to trace quantity
        traces' = map (\[m,n] -> (traces m n) `mod'` (10^9+7)) dimensions
    mapM_ print traces'
