"""Weighted graph representation and Dijkstra's shortest-path algorithm."""
import heapq


def build_graph(locations, roads):
    """Build an undirected weighted adjacency-list graph."""
    graph = {location: [] for location in locations}

    for road in roads:
        start = road["from"]
        end = road["to"]
        distance = road["distance"]

        graph[start].append((end, distance))
        graph[end].append((start, distance))

    return graph


def dijkstra(graph, source):
    """
    Find shortest distances from source to every reachable vertex.
    Returns distance and previous-vertex dictionaries.
    All edge weights must be non-negative.
    """
    distances = {vertex: float("inf") for vertex in graph}
    previous = {vertex: None for vertex in graph}

    distances[source] = 0
    priority_queue = [(0, source)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Ignore an outdated queue entry.
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, edge_weight in graph[current_vertex]:
            new_distance = current_distance + edge_weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current_vertex
                heapq.heappush(priority_queue, (new_distance, neighbor))

    return distances, previous


def build_distance_matrix(required_locations, all_distances):
    """Create shortest-path distances between all required locations."""
    matrix = {}

    for source in required_locations:
        matrix[source] = {}
        for target in required_locations:
            distance = all_distances[source][target]
            if distance == float("inf"):
                raise ValueError(f"No route exists between {source} and {target}.")
            matrix[source][target] = distance

    return matrix
