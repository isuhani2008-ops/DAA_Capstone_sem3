# 🚚 Mini-Courier Planner

### Design and Analysis of Algorithms (DAA) – Capstone Project

**K.R. Mangalam University, Gurugram**  
**Course:** Design & Analysis of Algorithms (ETCCDA302)  
**Project Type:** Individual Capstone Project  
**Language:** Python

---

## 📌 Project Overview

Mini-Courier Planner is a Python-based courier delivery planning system that demonstrates the application of fundamental **Design and Analysis of Algorithms (DAA)** concepts.

The project helps organize parcel deliveries by considering parcel deadlines, priorities, vehicle capacity, and road distances.

It combines sorting, dynamic programming, graph algorithms, and route optimization techniques to create an efficient delivery-planning workflow.

## 🎯 Project Objectives

- Organize parcels according to their delivery deadlines and priorities.
- Select parcels while respecting the vehicle's weight capacity.
- Calculate shortest paths between delivery locations.
- Generate an approximate delivery route.
- Analyze the execution time of different algorithms.

## 🧠 Algorithms Used

| Algorithm | Application | Time Complexity |
|---|---|---|
| Merge Sort | Sorting parcels by deadline and priority | O(n log n) |
| 0/1 Knapsack | Selecting parcels within vehicle capacity | O(nW) |
| Dijkstra's Algorithm | Finding shortest paths in the road network | O((V + E) log V) |
| Nearest Neighbor TSP | Generating an approximate delivery route | O(k²) |

**Where:**
- `n` = Number of parcels
- `W` = Vehicle capacity
- `V` = Number of graph vertices
- `E` = Number of graph edges
- `k` = Number of delivery locations

## ⚙️ Project Workflow

The project follows these steps:

1. **Input Processing:** Reads parcel details and road-network information from JSON files.
2. **Parcel Sorting:** Uses Merge Sort to arrange parcels by ascending deadline. Higher-priority parcels come first when deadlines are equal.
3. **Parcel Selection:** Applies 0/1 Knapsack dynamic programming to maximize the total priority score within the vehicle's weight capacity.
4. **Shortest Path Calculation:** Uses Dijkstra's algorithm to calculate shortest distances between relevant locations.
5. **Route Generation:** Uses the Nearest Neighbor heuristic to generate an approximate delivery tour.
6. **Performance Analysis:** Measures algorithm execution times and generates a runtime comparison chart.

## 📂 Project Structure

```text
Mini-Courier-Planner/
│
├── main.py
├── sorting.py
├── knapsack.py
├── graph.py
├── tsp.py
├── performance.py
│
├── data/
│   ├── parcels.json
│   └── delivery_graph.json
│
├── outputs/
│   ├── sample_run.txt
│   ├── runtime_results.csv
│   └── runtime_comparison.png
│
├── README.md
├── PHASE_1_DESIGN.md
├── REPORT_TEMPLATE.md
└── requirements.txt
```

## 🛠️ Technologies Used

- **Python:** Core programming language.
- **JSON:** Input data storage.
- **Heapq:** Priority queue implementation for Dijkstra's algorithm.
- **Matplotlib:** Runtime comparison visualization.
- **CSV:** Storage of algorithm performance results.

## 💻 Installation and Setup

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Navigate to the Project Folder

```bash
cd Mini-Courier-Planner
```

### Step 3: Install Dependencies

```bash
py -m pip install -r requirements.txt
```

### Step 4: Run the Main Program

```bash
py main.py
```

### Step 5: Run Performance Analysis

```bash
py performance.py
```

The performance script generates runtime results and a comparison chart in the `outputs` folder.

## 📊 Sample Execution Results

The supplied sample execution uses a vehicle capacity of **15 kg**.

### Selected Parcels

| Parcel ID | Destination | Weight | Priority |
|---|---|---:|---:|
| P02 | B | 6 kg | 100 |
| P06 | B | 2 kg | 50 |
| P01 | A | 4 kg | 90 |
| P08 | C | 3 kg | 75 |
| **Total** | | **15 kg** | **315** |

### Generated Delivery Route

```text
DEPOT → A → B → C → DEPOT
```

**Estimated Total Distance:** 18 km

### Performance Analysis

The project measures the execution time of:

- Merge Sort
- 0/1 Knapsack
- Dijkstra's Algorithm
- Nearest Neighbor TSP

The measured results are saved in:

- `outputs/runtime_results.csv`
- `outputs/runtime_comparison.png`

*Note: Execution times may vary depending on the computer hardware and Python environment.*

## 📈 Performance Visualization

The runtime comparison chart illustrates how the execution time of the selected algorithms changes with increasing input sizes.

Open `outputs/runtime_comparison.png` to view the generated graph.

## 🔍 Assumptions and Limitations

- Each parcel is either selected completely or not selected.
- The vehicle has a fixed weight capacity.
- Parcel deadlines are used for sorting, not for enforcing delivery time windows.
- Road distances are non-negative.
- The road network is treated as an undirected graph.
- Parcels with the same destination can be delivered at the same stop.
- The Nearest Neighbor algorithm provides an approximate route and does not guarantee the optimal TSP solution.

## 🚀 Future Enhancements

- Implement multiple vehicle support.
- Introduce delivery time-window constraints.
- Add real-time traffic information.
- Improve route optimization using advanced heuristics.
- Develop a graphical user interface.
- Support larger datasets and more detailed performance comparisons.

## 🎓 Learning Outcomes

Through this project, the following concepts were implemented and explored:

- Divide-and-conquer approach using Merge Sort.
- Dynamic programming using the 0/1 Knapsack problem.
- Graph representation using adjacency lists.
- Shortest-path computation using Dijkstra's algorithm.
- Approximation techniques for the Travelling Salesperson Problem.
- Time complexity and performance analysis.

## 👩‍💻 Author

**Student Name:** Your Name  
**University:** K.R. Mangalam University  
**Programme:** B.Tech Computer Science and Engineering  
**Course:** Design & Analysis of Algorithms (ETCCDA302)

---

### 📌 Project Information

This project was developed as part of the Design and Analysis of Algorithms capstone assignment to demonstrate the practical implementation and integration of fundamental algorithmic techniques using Python.
