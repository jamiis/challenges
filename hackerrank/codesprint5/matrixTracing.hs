-- special mod. only happens if x > n.
mod' :: (Integral a) => a -> a -> a
x `mod'` n
    | x > n     = x `mod` n
    | otherwise = x

-- n choose k
choose n 0 = 1
choose 0 k = 0
choose n k = choose (n-1) (k-1) * n `div` k

-- number of traces in a matrix equals n-choose-k combinations
traces m n = choose n' k' 
    where n' = (m-1) + (n-1) -- required number of down moves and right moves
          k' =  m-1          -- required number of down moves

main = do
    contents <- getContents
        -- convert stdin to a list of [m,n] dimensions
    let dimensions = map (map read . words) $ tail $ lines contents :: [[Integer]]
        -- calculate number of traces for each dimension in list
        traces' = map (\[m,n] -> traces m n `mod'` outputLimit) dimensions
            where outputLimit = 10^9+7
    mapM_ print traces'
