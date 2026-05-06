# https://www.codewars.com/kata/51b6249c4612257ac0000005/train/python

import re

roman_pattern_map = [
        # "",     # 0
        "0",    # 1
        "00",   # 2
        "000",  # 3
        "01",   # 4
        "1",    # 5
        "10",   # 6
        "100",  # 7
        "1000", # 8
        "02"    # 9
    ]
roman_pattern_map_kv = {
        # "",     # 0
        "0": 1,    # 1
        "00": 2,   # 2
        "000": 3,  # 3
        "1": 5,    # 5
        "01": 4,   # 4
        "10": 6,   # 6
        "100": 7,  # 7
        "1000": 8, # 8
        "02": 9    # 9
}
roman_unit_map = [
    ['I', 'V', 'X'], # 1
    ['X', 'L', 'C'], # 10
    ['C', 'D', 'M'], # 100
    ['M', 'T', 'T'], # 1000
]

# digit2roman
def convert_digit2roman(p: int, i: int) -> str:
    pattern = roman_pattern_map[i]
    unit_map = roman_unit_map[p]
    result = []
    for char in pattern:
        result.append(unit_map[int(char)])
    return "".join(result)
def solution_digit2roman(n):
    thousands = n // 1000
    hundreds = (n % 1000) // 100
    tens = (n % 100) // 10
    units = n % 10
    return convert_digit2roman(3, thousands)+convert_digit2roman(2, hundreds)+convert_digit2roman(1, tens)+convert_digit2roman(0, units)

def solution_roman2digit(n):
    digit = 0

    def contains_result(token: str, roman: str, idx: int) -> bool:
        if token not in {"C", "X", "M"}:
            return bool(re.search(re.escape(token), roman)) # re.escape() 纯字面匹配，防止特殊字符被误解为正则表达式的特殊字符
        prev = re.escape(roman_unit_map[idx - 1][0])
        return bool(re.search(fr'(?<!{prev}){re.escape(token)}', roman)) # TODO：解释？

    for i, ru in enumerate(roman_unit_map):
        multi = 10 ** i
        for rp, v in reversed(list(roman_pattern_map_kv.items())):
            result = ''
            for char in rp:
                index = int(char)
                result += ru[index]
            if contains_result(result, n, i):
                digit += v * multi
                break
    return digit

# print(solution("XC")) # Bug 190, Actual 90
# print(solution("CMLXXXIV")) # Bug 1984， Actual 984

def solution_roman2digit_bp(roman):
    symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = max_n = 0
    for c in reversed(roman):
        n = symbols[c]
        result += n if n >= max_n else -n # 
        max_n = max(max_n, n)
    return result

solution_roman2digit_bp("XC")