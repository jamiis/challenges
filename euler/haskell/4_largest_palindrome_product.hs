palindromes = [xy | x <- [100..999] , y <- [x..999] , let xy = x*y , reverse(show xy) == show xy]
main = print $ foldl max 0 palindromes
