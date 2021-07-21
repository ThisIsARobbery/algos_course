import math

def search_point(array):
  left = 0
  right = len(array) - 1
  while left <= right:
    middle = math.floor((left + right) / 2)
    if array[middle] == middle:
      return True
    elif array[middle] > middle:
      right = middle - 1
    else:
      left = middle + 1
  return False

n, *A = (map(int, input().split()))
print(search_point(A))