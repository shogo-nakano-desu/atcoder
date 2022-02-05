# 入力
N = int(input())
A= list(map(int, input().split()))

start=0
end=360

size = [start, end]

size = A + size
size.sort()
print(size)