# i: Increment the value
# d: Decrement the value
# s: Square the value
# o: Output the value to a result array

# Program "iiisdoso" should return numbers [8, 64].
# Program "iiisdosodddddiso" should return numbers [8, 64, 3600].

def parse(data):
    df = 0
    result = []
    for char in data:
        if char == 'i':
            df += 1
        elif char == 'd':
            df -= 1
        elif char == 's':
            df *= df
        elif char == 'o':
            result.append(df)
    return result