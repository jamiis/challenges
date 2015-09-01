main = print $ maximum [xy 
    | x <- [900..999]
    , y <- [x..999]
    , let xy = x*y
    , show xy == reverse(show xy)]
