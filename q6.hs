-- Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

sumsq = foldr (+)0 $ map (**2)[1..100]
sqsum = (foldr (+)0 [1..100])**2

diff = sqsum-sumsq