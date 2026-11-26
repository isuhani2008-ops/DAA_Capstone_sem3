"""Runtime experiments for the main algorithmic components."""
import random
import time
import csv
from pathlib import Path

from sorting import merge_sort_parcels
from knapsack import select_parcels
from graph import build_graph, dijkstra
from tsp import nearest_neighbor_tsp


def measure_time(function, *args):
    start = time.perf_counter()
    function(*args)
    end = time.perf_counter()
    return end - start


def make_parcels(count, seed=42):
    rng = random.Random(seed)
    return [
        {
            "id": f"P{i}",
            "destination": "A",
            "weight": rng.randint(1, 10),
            "deadline": rng.randint(1, 30),
            "priority": rng.randint(1, 100),
        }
        for i in range(count)
    ]


def make_connected_graph(vertex_count, seed=42):
    """Create a connected undirected graph for repeatable experiments."""
    rng = random.Random(seed)
    names = [f"L{i}" for i in range(vertex_count)]
    roads = []

    # A chain guarantees that every vertex is reachable.
    for i in range(vertex_count - 1):
        roads.append({"from": names[i], "to": names[i + 1],
                      "distance": rng.randint(1, 20)})

    # Add extra edges to make the graph more realistic.
    for i in range(vertex_count):
        for j in range(i + 2, vertex_count):
            if rng.random() < 0.12:
                roads.append({"from": names[i], "to": names[j],
                              "distance": rng.randint(1, 30)})

    return names, roads


def run_performance_tests(graph_data):
    print(f"{'Input size':<14}{'Merge Sort (s)':>18}{'Knapsack (s)':>16}{'Dijkstra (s)':>16}")
    print("-" * 64)
    results = []

    for size in (10, 50, 100, 200):
        parcels = make_parcels(size)
        capacity = 100
        sort_time = measure_time(merge_sort_parcels, parcels)
        knapsack_time = measure_time(select_parcels, parcels, capacity)

        locations, roads = make_connected_graph(size)
        graph = build_graph(locations, roads)
        dijkstra_time = measure_time(dijkstra, graph, locations[0])

        print(f"{size:<14}{sort_time:>18.6f}{knapsack_time:>16.6f}{dijkstra_time:>16.6f}")
        results.append({
            "input_size": size,
            "merge_sort_seconds": sort_time,
            "knapsack_seconds": knapsack_time,
            "dijkstra_seconds": dijkstra_time,
        })

    # Save measured values so the report chart can be reproduced.
    output_dir = Path(__file__).resolve().parent / "outputs"
    output_dir.mkdir(exist_ok=True)
    csv_path = output_dir / "runtime_results.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)
    print(f"\nRuntime measurements saved to: {csv_path.relative_to(Path(__file__).resolve().parent)}")

    try:
        import matplotlib.pyplot as plt
        sizes = [row["input_size"] for row in results]
        plt.figure()
        for key, label in [
            ("merge_sort_seconds", "Merge Sort"),
            ("knapsack_seconds", "0/1 Knapsack"),
            ("dijkstra_seconds", "Dijkstra"),
        ]:
            plt.plot(sizes, [row[key] for row in results], marker="o", label=label)
        plt.xlabel("Input size")
        plt.ylabel("Runtime (seconds)")
        plt.title("Mini-Courier Planner: Runtime Comparison")
        plt.legend()
        plt.grid(True)
        chart_path = output_dir / "runtime_comparison.png"
        plt.savefig(chart_path, dpi=150, bbox_inches="tight")
        plt.close()
        print(f"Runtime chart saved to: {chart_path.relative_to(Path(__file__).resolve().parent)}")
    except ImportError:
        print("Matplotlib is not installed; CSV was saved. Install it with: pip install matplotlib")

    # A small route experiment for Nearest Neighbor TSP.
    locations, roads = make_connected_graph(12)
    graph = build_graph(locations, roads)
    all_distances = {name: dijkstra(graph, name)[0] for name in locations}
    matrix = {
        source: {target: all_distances[source][target] for target in locations}
        for source in locations
    }
    destinations = locations[1:]
    tsp_time = measure_time(nearest_neighbor_tsp, locations[0], destinations, matrix)
    print(f"\nNearest Neighbor TSP on {len(destinations)} delivery points: {tsp_time:.6f} seconds")

    print("\nNote: Runtime values depend on your computer and Python environment.")
    print("Run the experiment more than once and report measured results, not invented values.")
