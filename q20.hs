{-
n! means n  (n  1)  ...  3  2  1
For example, 10! = 10  9  ...  3  2  1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
-}

fact n = fact' n 1
	where 
		fact' 0 a = a
		fact' n a = fact' (n-1) (n*a)
		
digits 0 = [0]
digits n = digits' n []
  where digits' 0 ds = ds
        digits' n ds = let (q,r) = quotRem n 10
                       in digits' q (r:ds)

sumOfDigits = sum . digits
