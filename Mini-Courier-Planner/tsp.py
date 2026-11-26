"""Nearest Neighbor approximation for the Traveling Salesperson Problem."""


def nearest_neighbor_tsp(start, destinations, distance_matrix):
    """
    Start at the depot, repeatedly visit the nearest unvisited destination,
    then return to the depot. This is an approximation, not a guaranteed
    globally optimal TSP solution.
    """
    unvisited = set(destinations)
    route = [start]
    current = start
    total_distance = 0

    while unvisited:
        next_location = min(
            unvisited,
            key=lambda location: distance_matrix[current][location]
        )
        total_distance += distance_matrix[current][next_location]
        route.append(next_location)
        unvisited.remove(next_location)
        current = next_location

    if current != start:
        total_distance += distance_matrix[current][start]
        route.append(start)

    return route, total_distance
