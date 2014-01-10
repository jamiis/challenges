fibs :: (Num a) => [a]
fibs = map fst $ iterate (\(a,b) -> (b, a+b)) (0,1)

main = print . sum . filter even . takeWhile (<= 4000000) $ fibs
