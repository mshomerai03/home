# https://www.codewars.com/kata/526571aae218b8ee490006f4/train/python

def count_bits(n):
    c = 0
    while n > 1:
        c += n % 2
        n = n // 2
    return c + n

print(count_bits(7))