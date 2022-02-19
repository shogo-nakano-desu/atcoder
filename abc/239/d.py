prime = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199]


# input
A,B,C,D = map(int, input().split())

taka_list = list(range(A,B+1))
ao_list = list(range(C,D+1))
done = False
for i in taka_list:
  count = 0
  for k in ao_list:
    if i+k in prime:
      count += 1
      break
  if count == 0:
    print("Takahashi")
    done = True
    break

if done == False:
  print("Aoki")