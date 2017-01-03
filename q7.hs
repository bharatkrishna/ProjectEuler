{-
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
-}
primes = 2 : filter (\n -> not (any (\p -> n `mod` p == 0) (takeWhile (\p -> p*p <= n) primes))) [3..]
	
ans = primes !! 10000