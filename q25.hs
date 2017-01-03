fibs = 0:1:(zipWith (+) fibs (tail fibs))
t = 10^999
 
problem_25 = length w
    where
      w = takeWhile (< t) fibs