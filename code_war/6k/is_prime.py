# https://www.codewars.com/kata/5262119038c0985a5b00029f/train/python

def is_prime(num): 
    if num <= 1:
        return False
    elif num%2 == 0 and num != 2: # 排除非2偶数
        return False
    else:
        for i in range(3, int(num**0.5) + 1, 2): # sqrt(num)缩减循环范围，且只检查奇数
            if num % i == 0:
                return False
    return True

# 225390169
print(is_prime(2))  