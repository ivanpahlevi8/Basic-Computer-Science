import heapq

# Graph representation
data = {
    'A': {'B': 3, 'C': 3},
    'B': {'A': 3, 'D': 3.5, 'E': 2.8},
    'C': {'A': 3, 'F': 3.5, 'E': 2.8},
    'D': {'B': 3.5, 'E': 3.1, 'G': 10},
    'E': {'B': 2.8, 'C': 2.8, 'D': 3.1, 'G': 7},
    'F': {'C': 3.5, 'G': 2.5},
    'G': {'D': 10, 'E': 7, 'F': 2.5},
}

def solution(graph, start, end):
    # Priority queue to keep track of the node with the smallest distance
    queue = [(0, start)]

    # Distance from start to each node, initialized to infinity
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # To reconstruct the shortest path
    previous_nodes = {node: None for node in graph}

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        # Skip processing if we have already found a shorter path
        if current_distance > distances[current_node]:
            continue

        # Stop when we reach the destination node
        if current_node == end:
            break

        # Explore neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # If a shorter path to the neighbor is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    # Reconstruct the path from end to start
    path = []
    while end is not None:
        path.append(end)
        end = previous_nodes[end]
    path.reverse()

    return distances[path[-1]], path  # Return the distance and the path

# Find and display the shortest path from F to D
shortest_distance, shortest_path = solution(data, 'F', 'D')
print(f"Shortest Num From F to D : {shortest_distance}")
print(f"Shortest Path From F to D : {shortest_path}")
