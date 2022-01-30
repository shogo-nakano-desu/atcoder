L = []
R = []
N = int(input())
S = input()
for i, c in enumerate(S):
    if c == 'L':
        R.append(i)
    else:
        L.append(i)
print(*(L+[N]+R[::-1]))
