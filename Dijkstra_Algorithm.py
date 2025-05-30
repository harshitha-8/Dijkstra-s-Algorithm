import heapq

def dijkstra(graph, start):
    distances = {node: float("infinity") for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbour, weight in graph[current_node].items():
            new_distance = current_distance + weight
            if new_distance < distances[neighbour]:
                distances[neighbour] = new_distance
                heapq.heappush(priority_queue, (new_distance, neighbour))

    return distances

if __name__ == "__main__":
        graph = {
            'A': {'B': 1, 'C': 4},
            'B': {'A': 1, 'C': 2, 'D': 5},
            'C': {'A': 4, 'B': 2, 'D': 1},
            'D': {'B': 5, 'C': 1}
        }
        start_node = 'A'
        distances = dijkstra(graph, start_node)
        print(f"distances from {start_node}: {distances}")