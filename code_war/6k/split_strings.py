# https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/train/python

def solution(s):
    r = []
    for n in range(0, len(s)//2*2, 2):
        r.append(s[n:n+2])
    if len(s) % 2:
        r.append(s[-1]+'_')
    return r

print(solution('asdfads'))