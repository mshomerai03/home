import re

# Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
# Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"

def to_jaden_case(string):
    if not string:
        return string
    string = string[0].upper() + string[1:].lower()
    # return re.sub(r'\s([a-z])', lambda m: m.group(1).upper(), string)
    # ?<=：正向后行断言，判断字符（这里是\s）不会被匹配到结果里，匹配 空格+a-z
    # ?=：正向前瞻，判断字符不会被匹配到结果里，匹配a+z+空格
    return re.sub(r'(?<=\s)[a-z]', lambda m: m.group(0).upper(), string)
