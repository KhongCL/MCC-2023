# A function to find the minimum area of blue rectangles
# to cover all the red rectangles
def min_area(n, k, red):
  # Sort the red rectangles by their leftmost x-coordinate
  red.sort(key=lambda x: x[0])
  # Initialize the minimum area to infinity
  min_area = float('inf')
  # Loop through all possible ways to split the red rectangles into k groups
  for split in split_into_k_groups(red, k):
    # Initialize the area of the current split to zero
    area = 0
    # Loop through each group in the split
    for group in split:
      # Find the minimum and maximum x and y coordinates of the group
      min_x = min(x for x, y in group)
      max_x = max(x for x, y in group)
      min_y = min(y for x, y in group)
      max_y = max(y for x, y in group)
      # Add the area of the blue rectangle that covers the group to the area of the current split
      area += (max_x - min_x) * (max_y - min_y)
    # Update the minimum area if the area of the current split is smaller
    min_area = min(min_area, area)
  # Return the minimum area
  return min_area

# A helper function to generate all possible ways to split a list into k groups
def split_into_k_groups(lst, k):
  # If the list is empty or k is zero, return an empty list
  if not lst or k == 0:
    return []
  # If k is one, return the list as a single group
  if k == 1:
    return [[lst]]
  # Initialize the result list
  result = []
  # Loop through all possible lengths of the first group
  for i in range(1, len(lst) - k + 2):
    # Split the rest of the list into k - 1 groups recursively
    rest = split_into_k_groups(lst[i:], k - 1)
    # Add the first group and the rest of the groups to the result list
    for r in rest:
      result.append([lst[:i]] + r)
  # Return the result list
  return result

# Read the input
n, k = map(int, input().split())
red = []
for i in range(n):
  x, y = map(int, input().split())
  red.append((x, y))

# Print the output
print(min_area(n, k, red))
