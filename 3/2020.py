n = int(input())
cords = []
arrX = []
arrY = []
for i in range(n):
  cords.append(input().split(","))
for i in cords:
  arrX.append(int(i[0]))
  arrY.append(int(i[1]))
maxX = max(arrX) + 1
maxY = max(arrY) + 1
minX = min(arrX) - 1
minY = min(arrY) - 1
print(str(minX) + "," + str(minY))
print(str(maxX) + "," + str(maxY))
