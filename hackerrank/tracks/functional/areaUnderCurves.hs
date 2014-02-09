import Text.Printf (printf)
import Data.List

-- produces a more standard format for polynomials. e.g. 1 + 2x^3 + 3x^5 should be
-- encoded as [1,0,0,2,3] with the coeffs at the index that corresponds to their power
poly :: (Num a, Integral b) => [a] -> [b] -> [a]
poly cs es = 
        -- deltas helper = head : [elem differences -> x_n+1 - x_n - 1]
    let deltas = head es : (map (subtract 1) $ zipWith (-) (tail es) es)
        -- prefix d-1 zeros, e.g. c=2, d=4 -> [0,0,0,2]
        prefix0s x num = genericReplicate num 0 ++ [x]
    in concat $ zipWith prefix0s cs deltas

-- horner's algo computes polys by breaking them into smaller chunks for efficiency
-- ie. p(x) = ax + bx^2 + cx^3 = (a + (b + (c + x)*x)*x)
horner :: (Num a) => [a] -> a -> a
horner p x = foldr (\coeff acc -> coeff + acc*x) 0 p

--integrate :: (Enum a, Fractional a) => [a] -> [a] -> a
integrate p [left,right] = sum [step * horner p x | x <- interval]
    where interval = [left,(left+step)..right]
          step = 0.1

-- This function should return a list [area, volume].
solve :: [Int] -> [Int] -> [Int] -> [Double]
solve coeffs exps (left:right) = integrate p [left,right]
    where p = poly coeffs exps

main = getContents >>= mapM_ (printf "%.1f\n") . passToSolver . parse
    where passToSolver = (\[coeffs, exps, interval] -> solve(coeffs exps interval))
          parse = map (map read . words) . lines
