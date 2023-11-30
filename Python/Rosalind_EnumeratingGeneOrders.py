import math
import itertools

n = 5

solution = math.factorial(n)

numArr = []
numArr += n * [0]
num = 1
x = 1
# While num is less than the amount of values

while num < n + 1:
    # For every value in the num array
    for index in range(0, len(numArr)):
        # The index in numArr is the current n
        numArr[index] = num
        num += 1


items = list(itertools.permutations(numArr))
print(solution)
for val in items:
    perms = []
    for number in val:
        perms.append(number)
    print(*perms, sep=" ")
