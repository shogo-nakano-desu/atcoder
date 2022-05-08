# 入力文字列
# n = input()
n = "aaaaaaaphp"

reverse_n_list = list(reversed(n))
# 逆の文字列
reverse_n = ''.join(list(reversed(n)))

# reverse文字列の先頭についたaを取り除く
not_a_n_re = reverse_n.lstrip('a*')

# オリジナルの末についたaを取り除く
not_a_n_origin = n.rstrip('a*')

# 元から回文
if n == reverse_n:
    print("Yes")
elif not_a_n_origin == not_a_n_re:
    print("Yes")
else:
    print("No")
