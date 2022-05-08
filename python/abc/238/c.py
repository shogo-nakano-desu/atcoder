N = int(input())


# 分母
m = 998244353

#Nが何桁の数か判断
keta = N//10 + 1
sum_nums = 0
for i in range(keta):
  #実際に使う桁
  k = i+1
  #最後の桁に行く前
  if (k < keta):
    # nums = list(range(1,9*(10**(k-1))+1))
    nums = set([x for x in range(9*(10**(k-1))+1)])
    sum_nums += sum(nums)
    del nums
  #最後の桁の時
  else:
    # nums = list(range(1,N-(10**(keta-1)-2)))
    nums = set([x for x in range(N-(10**(keta-1)-2))])
    sum_nums += sum(nums)
    del nums

print(sum_nums%m)

