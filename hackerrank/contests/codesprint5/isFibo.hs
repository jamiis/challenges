-- infinite list of fibonacci numbers
fibs :: (Num a) => [a]
fibs = map fst $ iterate (\(a,b) -> (b, a+b)) (0,1)

main = do
    contents <- getContents
        -- convert stdin to list of Ints
    let nums = map read $ tail $ lines contents :: [Int]
        -- list of fibonacci numbers upto defined limit
        fibs' = takeWhile (<= 10^10) fibs
        -- nums to list of "IsFibo"/"IsNotFibo" strings
        isFibs = map (\n -> if n `elem` fibs' then "IsFibo" else "IsNotFibo") nums
    mapM_ putStrLn isFibs
