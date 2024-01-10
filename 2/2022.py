n = int(input())
total = []
gold = 0
for i in range(n):
  scored = int(input())
  fouls = int(input())
  total.append(scored*5-fouls*3)
for i in total:
  if i > 40:
    gold+=1
if gold==len(total):
  print(str(gold)+"+")
else:
  print(gold)
