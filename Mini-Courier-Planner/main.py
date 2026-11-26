"""Mini-Courier Planner: integrated DAA capstone application."""

from pathlib import Path
import json

from sorting import merge_sort_parcels
from knapsack import select_parcels
from graph import build_graph, dijkstra, build_distance_matrix
from tsp import nearest_neighbor_tsp
from performance import run_performance_tests


ROOT = Path(__file__).resolve().parent


def load_data():
    with open(ROOT / "data" / "parcels.json", "r", encoding="utf-8") as f:
        parcels = json.load(f)
    with open(ROOT / "data" / "delivery_graph.json", "r", encoding="utf-8") as f:
        graph_data = json.load(f)
    return parcels, graph_data


def print_parcels(parcels, heading):
    print(f"\n{heading}")
    print("-" * len(heading))
    print(f"{'ID':<6}{'Destination':<16}{'Weight':>9}{'Deadline':>12}{'Priority':>11}")
    for p in parcels:
        print(
            f"{p['id']:<6}{p['destination']:<16}{p['weight']:>9}"
            f"{p['deadline']:>12}{p['priority']:>11}"
        )


def main():
    parcels, graph_data = load_data()
    capacity = graph_data["vehicle_capacity"]
    depot = graph_data["depot"]
    graph = build_graph(graph_data["locations"], graph_data["roads"])

    print("=" * 60)
    print("              MINI-COURIER PLANNER")
    print("=" * 60)
    print(f"Starting depot: {depot}")
    print(f"Vehicle capacity: {capacity} kg")

    # PHASE 2A: Sort parcels by earliest deadline, then highest priority.
    sorted_parcels = merge_sort_parcels(parcels)
    print_parcels(sorted_parcels, "PHASE 2: PARCELS AFTER PRIORITIZATION")

    # PHASE 2B: 0/1 Knapsack selects the best set within capacity.
    selected, total_weight, total_score = select_parcels(sorted_parcels, capacity)
    print_parcels(selected, "SELECTED PARCELS FOR THIS TRIP")
    print(f"\nTotal selected weight: {total_weight} kg / {capacity} kg")
    print(f"Total priority score: {total_score}")

    if not selected:
        print("\nNo parcels fit within the vehicle capacity.")
        return

    # PHASE 3A: Run Dijkstra from each required location.
    destinations = sorted({p["destination"] for p in selected})
    required_locations = [depot] + destinations
    all_distances = {}
    all_previous = {}

    print("\nPHASE 3: SHORTEST PATHS USING DIJKSTRA")
    for source in required_locations:
        distances, previous = dijkstra(graph, source)
        all_distances[source] = distances
        all_previous[source] = previous

    distance_matrix = build_distance_matrix(required_locations, all_distances)

    print("\nDistance matrix (km):")
    print(" " * 12 + "".join(f"{name:>12}" for name in required_locations))
    for source in required_locations:
        row = "".join(f"{distance_matrix[source][target]:>12.1f}" for target in required_locations)
        print(f"{source:<12}{row}")

    # PHASE 3B: Nearest Neighbor TSP on the shortest-path distance matrix.
    route, route_distance = nearest_neighbor_tsp(depot, destinations, distance_matrix)
    print("\nDELIVERY ROUTE USING NEAREST NEIGHBOR TSP")
    print(" -> ".join(route))
    print(f"Estimated route distance: {route_distance:.1f} km")
    print("(The route returns to the depot after the final delivery.)")

    # Show the actual shortest road path for each consecutive route leg.
    print("\nROAD PATH DETAILS")
    for start, end in zip(route, route[1:]):
        path = []
        current = end
        while current is not None:
            path.append(current)
            current = all_previous[start][current]
        path.reverse()
        print(f"{start} -> {end}: {' -> '.join(path)} ({distance_matrix[start][end]:.1f} km)")

    # PHASE 4: Runtime comparisons.
    print("\nPHASE 4: PERFORMANCE TESTING")
    run_performance_tests(graph_data)


if __name__ == "__main__":
    main()
