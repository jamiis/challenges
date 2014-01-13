import Data.List
import Data.Char

main = do number <- readFile "8_number.txt"
          let ints = map digitToInt $ concat $ lines number
          print $ maximum $ map (product . take 5) $ tails ints
