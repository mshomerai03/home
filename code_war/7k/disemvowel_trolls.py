# This website is for losers LOL! -> Ths wbst s fr lsrs LL!

# 删除字符串中aeiouAEIOU
def disemvowel(string_):
    # str.maketrans
    # 第一个参数 ''：要替换的字符（空，表示不替换任何字符）# 第二个参数 ''：替换后的字符（空，与第一个参数对应）
    # 第三个参数 'aeiouAEIOU'：要删除的字符集
    return string_.translate(str.maketrans('', '', 'aeiouAEIOU'))