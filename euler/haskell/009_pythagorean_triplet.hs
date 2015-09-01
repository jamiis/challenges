main = print $ (\(x,y,z) -> x*y*z) $ head [(a, b, c) | 
    a <- [1..430], 
    b <- [1..a], 
    c <- [sqrt(a^2 + b^2)], 
    a^2 + b^2 == c^2, 
    a + b + c == 1000]
