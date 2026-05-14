# https://www.codewars.com/kata/55f2b110f61eb01779000053/train/python

def get_sum(a,b):
    n = abs(a - b) + 1
    if a == b:
        return a
    else:
        return n*(n+1)//2 + (min(a, b) - 1)*n # 1+2+3+4...+n = n*(n+1)//2

print(get_sum(0, -1))