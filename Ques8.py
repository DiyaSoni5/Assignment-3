def merge(intervals):
    if not intervals:
        return []

    # Sort intervals based on the starting value
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for i in range(1, len(intervals)):
        last_merged = merged[-1]
        current_interval = intervals[i]

        # If the current interval overlaps with the last merged interval, merge them
        if current_interval[0] <= last_merged[1]:
            last_merged[1] = max(last_merged[1], current_interval[1])
        else:
            merged.append(current_interval)

    return merged

# Example usage
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge(intervals))
