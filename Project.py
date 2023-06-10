import heapq

import numpy as np


# Design Part - Carpet Design Similarity
def find_similar_carpet(input_map, carpet_maps, num_similar):
    similarity_scores = []
    for i, carpet in enumerate(carpet_maps):
        similarity = np.sum(input_map == carpet) / (
            input_map.shape[0] * input_map.shape[1]
        )
        similarity_scores.append((i, similarity))

    similarity_scores.sort(key=lambda x: x[1], reverse=True)
    similar_carpet_indices = [x[0] for x in similarity_scores[:num_similar]]
    return similar_carpet_indices


def find_affordable_carpets(carpet_prices, max_budget):
    n = len(carpet_prices)
    dp = [[0] * (max_budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, max_budget + 1):
            if carpet_prices[i - 1] <= j:
                dp[i][j] = max(
                    dp[i - 1][j],
                    dp[i - 1][j - carpet_prices[i - 1]] + carpet_prices[i - 1],                )
            else:
                dp[i][j] = dp[i - 1][j]

    selected_items = []
    i, j = n, max_budget
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            selected_items.append(carpet_prices[i - 1])
            j -= carpet_prices[i - 1]
        i -= 1

    return selected_items


# Routing Part - Find Nearest Factory Outlet
def find_shortest_path(graph, start, destination):
    distances = {vertex: float("inf") for vertex in graph}
    distances[start] = 0
    previous_vertices = {vertex: None for vertex in graph}

    queue = [(0, start)]

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)

        if current_distance > distances[current_vertex]:
            continue

        if current_vertex == destination:
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_vertices[neighbor] = current_vertex
                heapq.heappush(queue, (distance, neighbor))

    path = []
    current_vertex = destination

    while current_vertex is not None:
        path.append(current_vertex)
        current_vertex = previous_vertices[current_vertex]

    return list(reversed(path))


# Example usage
input_map = np.array([[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]])

carpet_maps = [
    np.array([[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]]),
    np.array([[1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0]]),
    np.array([[1, 1, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0]]),
    np.array([[0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0]]),
    np.array([[1, 0, 0, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 0, 0, 1]]),
]

carpet_prices = [200, 150, 300]
budget = 500

map_graph = {
    "Intersection1": {"Intersection2": 10, "Intersection3": 5},
    "Intersection2": {"Intersection1": 10, "Intersection4": 1},
    "Intersection3": {"Intersection1": 5, "Intersection4": 5},
    "Intersection4": {"Intersection2": 1, "Intersection3": 5, "Intersection5": 3},
    "Intersection5": {"Intersection4": 3},
}

branches = {
    "Branch1": "Intersection2",
    "Branch2": "Intersection4",
    "Branch3": "Intersection5",
}
user_location = "Intersection5"
destination_branch = "Branch2"


# Carpet Design Similarity
similar_indices = find_similar_carpet(input_map, carpet_maps, num_similar=3)
print(f"Similar Carpets: {similar_indices}")

# Maximum Carpets within Budget
affordable_carpets = find_affordable_carpets(carpet_prices, max_budget=budget)
print(f"Affordable Carpets: {affordable_carpets}")

# Find Nearest Factory Outlet
path_to_branch = find_shortest_path(
    map_graph, user_location, branches[destination_branch]
)

# Print Path to the Destination Branch
print("Path to the Branch:", " -> ".join(path_to_branch))
