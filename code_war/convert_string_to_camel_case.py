# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"
# "The_Stealth-Warrior" gets converted to "TheStealthWarrior"

import re

def to_camel_case(text):
    return re.sub(r'[-_](.)', lambda m: m.group(1).upper(), text)