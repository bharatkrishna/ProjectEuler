'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.'''

from math import sqrt

def isPrime(n):
    if n == 1: return False
    elif n < 4: return True # this would be only 2 & 3
    elif n%2==0: return False
    elif n<9: return True # based on the above
    elif n%3==0: return False
    else:
        r= round(sqrt(n)) # any number n can have only 1 prime factor > sqrt(n)
        f=5 # starting to check from 5 onwards
        while f<=r:
            if n%f==0: return False
            if n%(f+2)==0: return False
            f=f+6 
    return True

sum=0
for i in range(2000000):
    if (isPrime(i)):sum=sum+i
    
print sum

'''
Answer: 142913828922
'''   