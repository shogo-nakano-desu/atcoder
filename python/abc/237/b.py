# input
H, W = map(int, input().split())
l = [list(map(int, input().split())) for l in range(H)]

new_l = [list(x) for x in zip(*l)]

for i in new_l:
    print(*i)
