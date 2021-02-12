#Program to find simple intrest
def simple_interest(p, t, r):
    print('The rate of intrest is',p)
    print('The time period is', t)
    print('The rate of interest is', r)
    si = (p * t * r) / 100
    print('The Simple Interest is', si)
    return si
simple_interest(12,6,8)


