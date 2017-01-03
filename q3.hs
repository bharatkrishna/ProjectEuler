{-
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
-}

lpfact n = lpfact' n 2 where
	lpfact' n f | n == f 			= f 
				| n `mod` f == 0 	= lpfact' (n `div` f) f
				| otherwise 		= lpfact' n (succ f) 