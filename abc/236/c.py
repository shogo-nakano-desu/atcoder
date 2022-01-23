# 入力
start, end = map(int, input().split())
S = input().split()  # 鈍行
T = input().split()  # 急行

# 最初と最後の駅は問答無用でYes
print("Yes")

# SとTから最初と最後の文字列を落とす
S.pop(-1)
S.pop(0)
T.pop(-1)
T.pop(0)

s_now = 0
t_now = 0
# loopを回していく
while (s_now < len(S) and t_now < len(T)):
    if (S[s_now] == T[t_now]):
        print("Yes")
        s_now += 1
        t_now += 1
    else:
        print("No")
        s_now += 1
else:
    while (s_now < len(S)):
        print("No")
        s_now += 1


print("Yes")
