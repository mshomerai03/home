# https://www.codewars.com/kata/51e04f6b544cf3f6550000c1/train/python

def beeramid(bonus, price):
    level = 0
    while True:
        level += 1
        if not bonus//price >= level*(level+1)*(2*level+1)/6: # 1^2 + 2^2 + ... + n^2 = n(n+1)(2n+1)/6
            return level - 1
    
print(beeramid(454, 5))