
# input
x1,y1,x2,y2 = map(int, input().split())

one = [[x1+1, y1+2],
[x1+2, y1+1],
[x1+2, y1-1],
[x1+1,y1-2],
[x1-1,y1-2],
[x1-2,y1-1],
[x1-2,y1+1],
[x1-1,y1+2]]

two =[ [x2+1, y2+2],
[x2+2, y2+1],
[x2+2, y2-1],
[x2+1,y2-2],
[x2-1,y2-2],
[x2-2,y2-1],
[x2-2,y2+1],
[x2-1,y2+2]]

counter = 0

for i in one:
  for k in two:
    if i==k:
      print("Yes")
      counter += 1
      break
  if counter != 0:
    break

if counter == 0:
  print("No")