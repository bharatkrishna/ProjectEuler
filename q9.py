'''A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,
a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
# Not so efficiant way:

for m in range(0,1000,2):
    for n in range(1,1000,2):
        a= m**2 - n**2
        b = 2*m*n
        c=  m**2 + n**2
        if (a+b+c==1000 and a>0 and b>0 and c>0):
            print a,b,c
            print a*b*c