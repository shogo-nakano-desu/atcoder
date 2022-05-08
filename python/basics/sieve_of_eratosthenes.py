# x以下の整数から素数を探す
# 返り値は0-xのT/Fリスト。Trueだったら素数
import math

def sieve(x):
  # initialize
  prime = [True]*(x+1)
  prime[0]=False
  prime[1]=False

  max = math.ceil(x**0.5)

  for p in range(max):
    if prime[p]:
      for i in range(p*p,x+1,p):
        prime[i]=False
  return prime

