sumThreeOrFive xs = sum [x | x <- xs, x `mod` 3 == 0 || x `mod` 5 == 0]
main = print (sumThreeOrFive [1..999])
