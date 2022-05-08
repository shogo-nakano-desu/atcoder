name = input()
a, b = map(int, input().split())

# ----------------------------------------------------------------
# name = "chokudai"
# a = 3
# b = 5
# ----------------------------------------------------------------
a -= 1
b -= 1
name = list(name)

temp = name[a]
name[a] = name[b]
name[b] = temp
name = "".join(name)

print(name)
