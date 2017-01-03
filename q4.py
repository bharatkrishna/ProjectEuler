'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91*99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''
def reverse(n):
    reversed = 0
    while n > 0:
        reversed = 10*reversed + n % 10
        n = n/10
    return reversed

def isPalindrome(n):
    return n == reverse(n)

largestPalindrome = 0
a = 999
while a >= 100:
    b = 999
    while b >= a:
        if a*b <= largestPalindrome:
            break #Since a*b is always going to be too small
        if isPalindrome(a*b):
            largestPalindrome = a*b
        b = b-1
    a = a-1
        
print largestPalindrome