# 1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
# 5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)

def add_binary(a,b):
    return bin(a + b)[2:] # 0b is the prefix for binary literals, so we slice it off with [2:]
