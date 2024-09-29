def maximum_units(box_types, truck_size):
    # Sort the box types based on the units per box in descending order
    box_types.sort(key=lambda x: x[1], reverse=True)

    total_units = 0
    total_boxes = 0

    # Iterate over the sorted box types
    for box_type in box_types:
        num_boxes = box_type[0]
        units_per_box = box_type[1]

        if total_boxes + num_boxes <= truck_size:
            total_units += num_boxes * units_per_box
            total_boxes += num_boxes
        else:
            # If the truck can't take all boxes, fill the remaining space
            remaining_space = truck_size - total_boxes
            total_units += remaining_space * units_per_box
            break

    return total_units

# Example usage
box_types = [[1, 3], [2, 2], [3, 1]]  # [number of boxes, units per box]
truck_size = 4
result = maximum_units(box_types, truck_size)
print("Maximum units on the truck:", result)
