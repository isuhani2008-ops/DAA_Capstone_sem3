# Mini-Courier Planner

A beginner-friendly Python capstone prototype for the Design & Analysis of Algorithms (ETCCDA302) assignment.

## Assignment algorithms implemented

1. **Merge Sort** — sorts parcels by earliest deadline, then highest priority.
2. **0/1 Knapsack (Dynamic Programming)** — selects the maximum total priority score without exceeding vehicle capacity.
3. **Dijkstra's Algorithm** — finds shortest road distances between locations.
4. **Nearest Neighbor TSP approximation** — chooses a delivery order using the shortest-path distance matrix.
5. **Performance testing** — measures runtime for multiple input sizes.

## Project structure

```text
Mini-Courier-Planner/
├── main.py
├── sorting.py
├── knapsack.py
├── graph.py
├── tsp.py
├── performance.py
├── data/
│   ├── parcels.json
│   └── delivery_graph.json
└── outputs/
```

## Requirements

- Python 3.9 or later
- Python standard library for the core application.\n- Matplotlib for automatic runtime chart generation.

## Run the project

1. Extract the ZIP file.
2. Open the `Mini-Courier-Planner` folder in VS Code.
3. Open the terminal in that folder.
4. Run:

```bash
python main.py
```

On some Windows installations, use:

```powershell
py main.py
```

## Input data

### parcels.json

Each parcel contains:

- `id`: unique parcel identifier
- `destination`: delivery location
- `weight`: parcel weight in kg
- `deadline`: deadline priority value (smaller number means earlier deadline)
- `priority`: numerical score used by the Knapsack objective

### delivery_graph.json

- `depot`: starting and ending location
- `vehicle_capacity`: maximum carrying capacity in kg
- `locations`: graph vertices
- `roads`: undirected edges with non-negative distances in km

## Design assumptions

- Road distances are undirected and non-negative.
- The vehicle starts at the depot and returns to the depot after deliveries.
- If multiple selected parcels have the same destination, that destination is visited once.
- Parcel selection maximizes the sum of priority scores subject to the weight capacity. Deadline is used for sorting, not as a hard delivery-time constraint.
- Nearest Neighbor is a heuristic. It produces an approximate route and does not guarantee the globally shortest TSP route.
- The sample data is illustrative and can be replaced with other valid datasets.

## Complexity analysis

Let:
- `n` = number of parcels
- `W` = vehicle capacity (integer weight units)
- `V` = number of graph vertices
- `E` = number of graph edges
- `k` = number of unique selected delivery destinations

| Component | Time complexity | Auxiliary space |
|---|---:|---:|
| Merge Sort | O(n log n) | O(n) |
| 0/1 Knapsack DP | O(nW) | O(nW) |
| Dijkstra with adjacency list and binary heap | O((V + E) log V) | O(V + E) |
| Nearest Neighbor TSP | O(k²) | O(k) |

The DP table uses `O(nW)` space. The graph adjacency list uses `O(V + E)` space. Actual runtime depends on the computer and input data.

## Performance testing

The application prints measured runtimes for Merge Sort, Knapsack, and Dijkstra at several input sizes, plus a small Nearest Neighbor experiment. It saves the measured values to `outputs/runtime_results.csv` and, when Matplotlib is installed, creates `outputs/runtime_comparison.png`.

For a formal report:
1. Run the program at least three times.
2. Record the measured values.
3. Compare how runtime changes as input size grows.
4. Create a chart from your actual measurements.
5. Mention that very small runtimes can fluctuate due to system load and timer precision.

## Viva preparation

Be ready to explain:
- Why Merge Sort is `O(n log n)`.
- What each cell in the Knapsack DP table represents.
- Why Dijkstra requires non-negative edge weights.
- Why a priority queue is used in Dijkstra.
- Why Nearest Neighbor is an approximation rather than an exact TSP solver.
- The difference between theoretical complexity and measured runtime.

## Important academic note

This is a prototype implementation and a starting point for your individual capstone. Understand it, test it, personalize the dataset, and follow your faculty's submission and originality requirements.
