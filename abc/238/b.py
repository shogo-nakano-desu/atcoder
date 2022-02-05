# 入力
N = int(input())
A= list(map(int, input().split()))

#どれだけ回した位置を切ったか計算
sum = 0
for i, item in enumerate(A):
  A[i] = sum + item
  sum += item
  #回した位置を360度に収める
  A[i] = A[i]%360

# Aを小さ順で並び替えて、先頭と最後に0と360をたす
A.sort()
A.append(360)
A.insert(0,0)

#2点間の距離を取る
max = 0
for i in range(len(A)-1):
  between = A[i+1]-A[i]
  if (max < between):
    max = between

print(max)