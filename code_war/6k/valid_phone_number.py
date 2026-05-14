# https://www.codewars.com/kata/525f47c79f2f25a4db000025/train/python

import re

def valid_phone_number(phone_number):
    # (nnn) nnn-nnnn
    pattern = r'^\(\d{3}\) \d{3}-\d{4}$'
    return bool(re.match(pattern, phone_number))