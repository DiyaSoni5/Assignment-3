class Solution:
    def maximumUnits(self, boxTypes, truckSize):
        # Sort boxTypes based on units per box in descending order
        boxTypes.sort(key=lambda x: x[1], reverse=True)

        total_units = 0
        total_boxes = 0

        # Loop through each box type
        for num_boxes, units_per_box in boxTypes:
            if total_boxes + num_boxes <= truckSize:
                total_units += num_boxes * units_per_box
                total_boxes += num_boxes
            else:
                remaining_space = truckSize - total_boxes
                total_units += remaining_space * units_per_box
                break

        return total_units

# Example usage
solution = Solution()
boxTypes = [[1, 3], [2, 2], [3, 1]]  # Number of boxes and units per box
truckSize = 4
result = solution.maximumUnits(boxTypes, truckSize)
print("Maximum units that can be loaded onto the truck:", result)  # Output: 8

