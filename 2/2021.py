bids = {}
for i in range(int(input())):
  name = input()
  bid = int(input())
  bids[name] = bid
highest = bids[max(bids)]
for i in bids:
  if bids[i] == highest:
    print(i)
    break
