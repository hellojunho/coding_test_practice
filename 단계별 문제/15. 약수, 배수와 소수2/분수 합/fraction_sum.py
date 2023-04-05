import sys
import math

a1, a2 = map(int, sys.stdin.readline().split())
b1, b2 = map(int, sys.stdin.readline().split())

re1 = a1*b2 + b1*a2
re2 = a2*b2

result = math.gcd(re1, re2)

re1 //= result
re2 //= result

print(re1, re2)