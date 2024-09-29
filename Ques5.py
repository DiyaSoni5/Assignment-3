def find_content_children(g, s):
    # Sort the greed factors of children and sizes of cookies
    g.sort()
    s.sort()

    # Initialize pointers for children and cookies
    child = 0
    cookie = 0

    # Loop through both arrays
    while child < len(g) and cookie < len(s):
        # If the current cookie can satisfy the current child
        if s[cookie] >= g[child]:
            child += 1  # Move to the next child
        cookie += 1  # Always move to the next cookie

    return child  # The number of content children

# Example usage
g = [1, 2, 3]  # Greed factors of children
s = [1, 1]     # Sizes of cookies
result = find_content_children(g, s)
print("Number of content children:", result)
