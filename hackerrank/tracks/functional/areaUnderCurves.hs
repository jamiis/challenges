import Text.Printf (printf)
import Data.List

-- produces a more standard format for polynomials. e.g. 1 + 2x^3 + 3x^5 should be
-- encoded as [1,0,0,2,3] with the coeffs at the index that corresponds to their power
polyify cs es = 
        -- deltas helper = head : [differences between tail elems]
    let deltas = zipWith subtract (0:es) es
        -- prefix d-1 zeros, e.g. c=2, d=4 -> [0,0,0,2]
        prefix0s x num = genericReplicate (num-1) 0 ++ [x]
    in concat $ zipWith prefix0s cs deltas

-- horners algo computes polys by breaking them into smaller chunks for efficiency
-- ie. p(x) = ax + bx^2 + cx^3 = (a + (b + (c + x)*x)*x)
horner p x = foldr (\coeff acc -> coeff + acc*x) 0 p
