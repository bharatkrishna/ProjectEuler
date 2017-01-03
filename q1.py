'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''

n = 1000

nums = [i for i in range (1,n)]

'''
n2 = sum([number for number in nums if number % 3 == 0 or number % 5 == 0]) # using list comprehension
print n2
'''

m3 = filter(lambda x:x%3==0 or x%5==0, nums)

sums = reduce(lambda x,y:x+y, m3)

print sums