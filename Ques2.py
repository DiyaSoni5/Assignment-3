def find_max_min(arr, low, high):
    # If there is only one element
    if low == high:
        return arr[low], arr[low]
    
    # If there are two elements
    elif high == low + 1:
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]
    
    # If there are more than two elements
    else:
        mid = (low + high) // 2

        # Recursively get the minimum and maximum of the left half
        min_left, max_left = find_max_min(arr, low, mid)

        # Recursively get the minimum and maximum of the right half
        min_right, max_right = find_max_min(arr, mid + 1, high)

        # Overall min is the minimum of the two halves
        overall_min = min(min_left, min_right)

        # Overall max is the maximum of the two halves
        overall_max = max(max_left, max_right)

        return overall_min, overall_max

# Example usage
arr = [100, 11, 445, 1, 330, 3000]
n = len(arr)
min_val, max_val = find_max_min(arr, 0, n - 1)
print("Minimum:", min_val)
print("Maximum:", max_val)
