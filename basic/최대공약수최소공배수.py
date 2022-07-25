import math

print(math.gcd(21,14))

def lcm(a,b):
    return (a*b)//math.gcd(a,b)

print(lcm(21,14))
