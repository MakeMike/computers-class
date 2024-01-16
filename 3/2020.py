n = int(input())
arrX = []
arrY = []
for i in range(n):
  arrX.append(input().split(",")[0])
  arrX.append(input().split(",")[1])
maxX = max(arrX) + 1
maxY = max(arrY) + 1
minX = min(arrX) - 1
minY = min(arrY) - 1
print(str(minX) + "," + str(minY))
print(str(maxX) + "," + str(maxY))
