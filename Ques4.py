import heapq  # For priority queue (min-heap)

# Function to run Prim's algorithm
def prim_mst(graph, V):
    # Create a priority queue (min-heap)
    pq = [(0, 0)]  # (cost, vertex), starting from vertex 0 with cost 0
    in_mst = [False] * V  # To keep track of vertices included in MST
    mst_cost = 0  # To store the total cost of the MST
    edges_in_mst = 0  # Count of edges in the MST

    while pq and edges_in_mst < V - 1:
        cost, u = heapq.heappop(pq)  # Extract min-cost edge
        if in_mst[u]:
            continue
        # Include vertex u in MST
        in_mst[u] = True
        mst_cost += cost
        edges_in_mst += 1

        # Iterate through adjacent vertices of u
        for v, weight in graph[u]:
            if not in_mst[v]:
                heapq.heappush(pq, (weight, v))

    return mst_cost

# Example usage
if __name__ == "__main__":
    V = 5  # Number of vertices
    graph = {
        0: [(1, 2), (3, 6)],
        1: [(0, 2), (2, 3), (3, 8), (4, 5)],
        2: [(1, 3), (4, 7)],
        3: [(0, 6), (1, 8)],
        4: [(1, 5), (2, 7)]
    }  # Adjacency list (vertex: [(neighbor, weight), ...])

    mst_cost = prim_mst(graph, V)
    print("Cost of the Minimum Spanning Tree (MST) =", mst_cost)
