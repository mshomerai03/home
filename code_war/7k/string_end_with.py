# Inputs: "abc", "bc"
# Output: true

# Inputs: "abc", "d"
# Output: false

def solution(text, ending):
    return text.endswith(ending)