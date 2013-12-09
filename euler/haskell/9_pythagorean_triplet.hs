-- *very* slow implementation. 
-- need ... learn ... more ... haskell!
triplet = [[a, b, c] | c <- [1..430], b <- [1..c], a <- [1..b],
    a^2 + b^2 == c^2,  -- pythagorean theorem
    a + b + c == 1000] -- special condition
main = print( product( head triplet ) )
