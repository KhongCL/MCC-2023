
def min_area(n, k, red):
  
  red.sort(key=lambda x: x[0])

  min_area = float('inf')
  
  for split in split_into_k_groups(red, k):

    area = 0
    
    for group in split:
     
      min_x = min(x for x, y in group)
      max_x = max(x for x, y in group)
      min_y = min(y for x, y in group)
      max_y = max(y for x, y in group)
     
      area += (max_x - min_x) * (max_y - min_y)
    
    min_area = min(min_area, area)

  return min_area


def split_into_k_groups(lst, k):
 
  if not lst or k == 0:
    return []

  if k == 1:
    return [[lst]]
 
  result = []
 
  for i in range(1, len(lst) - k + 2):
 
    rest = split_into_k_groups(lst[i:], k - 1)
    
    for r in rest:
      result.append([lst[:i]] + r)

  return result


n, k = map(int, input().split())
red = []
for i in range(n):
  x, y = map(int, input().split())
  red.append((x, y))


print(min_area(n, k, red))
