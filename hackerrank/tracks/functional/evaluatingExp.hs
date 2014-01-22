-- factorial
fact :: (Enum a, Eq a, Num a) => a -> a
fact x
    | x == 0    = 1
    | otherwise = product [1..x]

-- exp(x), calculated using taylor series expanded to numterms
exponential :: Real a => a -> Int -> Double
exponential x numterms = sum . take numterms $ taylorSeries :: Double
          -- infinite list of e^x taylor series terms
    where taylorSeries = map (\i -> realToFrac(x)^i / realToFrac(fact i)) [0..]

main = getContents >>= mapM_ print . map (\x -> exponential x 10) . parse
    where parse = map (read::String->Double) . tail . words
