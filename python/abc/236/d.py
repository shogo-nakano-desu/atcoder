# 入力を受け取る
N = int(input())
# 二次元配列で入ってくる
rate = [list(map(int, input().split())) for _ in range(N*2-1)]


ans = 0

# rowは何段目か、iが要素
for row, i in enumerate(rate):
    max_i = max(i)
    max_i_index = i.index(max_i)
    # これを各列に対して行う
    row += 1
    while row < len(rate):
        if(row == row+max_i_index+1):
            row += 1
            continue
        for item in rate[row]:
            if(max_i + item > ans):
                ans = max_i+item
        row += 1

print(ans)
