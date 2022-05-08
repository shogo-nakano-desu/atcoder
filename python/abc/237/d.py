# タイムオーバー

N = int(input())
S = input()

A_list = [0]
S_list = list(S)

i = 1
index = 0

for str in S_list:
    if str == "L":
        A_list.insert(index, i)
        i += 1
    else:
        A_list.insert(index+1, i)
        index += 1
        i += 1

for i in range(N-1):
    print(o)
    A_list.append(A_dict[i])
print(*A_list)
