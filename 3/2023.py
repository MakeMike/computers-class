# Ask the number of days
days = int(input())
# Set the initial variables
availableNum = [0,0,0,0,0]
available = []
maxDays = []
finalStatement = ''
# Ask the availablity
for i in range(days):
  temp = input()
  available.append([*temp])
# Count the total availability per day, putting it in a list
for i in range(len(available)):
  for j in range(len(available[i])):
    if available[i][j] == 'Y':
      availableNum[j] += 1
# Find the most available days
max = max(availableNum)
# Append the index of the most available days to a list(maxDays)
for i in range(len(availableNum)):
  if availableNum[i] == max:
    maxDays.append(i+1)
# Concatenate the max days into a string
for i in maxDays:
  finalStatement += str(i) + ','
# Output the final statement to the stdout
print(finalStatement[:-1])
