
# Quicksort function to rank scores
def quicksort(arr):     # Average: O(n log n), Worst: O(n^2)
    # Base case: A single element array is already sorted
    if len(arr) <= 1:
        return arr

    # Choosing a pivot and partitioning the array into three sub-arrays
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]  # Elements less than pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to pivot
    right = [x for x in arr if x > pivot]  # Elements greater than pivot

    # Recursively applying quicksort to sub-arrays and combining the results
    return quicksort(left) + middle + quicksort(right)



# Calculate the number of mines within 1 tile of a given position
def minesNextTo(x, y, mines, size):     # Average: O(1), Worst: O(1)
    n = 0  # Counter for adjacent mines

    # Checking all adjacent tiles (8 directions)
    for dx in range(-1, 2):  # Horizontal offset: -1 (left), 0 (center), 1 (right)
        for dy in range(-1, 2):  # Vertical offset: -1 (up), 0 (center), 1 (down)
            if dx == 0 and dy == 0:
                continue  # Skip the current tile

            nx, ny = x + dx, y + dy  # New coordinates after applying offset
            # Check if the adjacent tile is within the board and has a mine
            if 0 <= nx < size and 0 <= ny < size and (nx, ny) in mines:
                n += 1

    return n

