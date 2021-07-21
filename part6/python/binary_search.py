import math

def search(value, array):
  left = 0
  right = len(array) - 1
  while left <= right:
    middle = (int)(math.floor((left+right)/2))
    if array[middle] == value:
      return middle
    elif array[middle] > value:
      right = middle - 1
    else:
      left = middle + 1
  return -2

n, *A = (map(int, input().split()))
k, *B = (map(int, input().split()))

results = []
for i in range(k):
  results.append((str)(search(B[i], A) + 1))

print(" ".join(results))