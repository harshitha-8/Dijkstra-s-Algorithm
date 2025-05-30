# Dijkstra's Algorithm Implementation

## Overview
This project contains a Python implementation of **Dijkstra's Algorithm**, which is a famous algorithm used to find the shortest path between nodes in a weighted graph.

## Features
- Calculates the shortest distance from a source node to all other nodes.
- Handles graphs represented as adjacency lists or matrices.
- Efficiently finds shortest paths in graphs with non-negative edge weights.

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/harshitha-8/Dijkstra-s-Algorithm.git


2. Navigate into the project directory:
   ```bash
   cd Dijkstra-s-Algorithm

3. Run the Python script:
   ```bash
   python3 Dijkstra_Algorithm.py

### Example usage
```bash
graph = {
    'A': {'B': 5, 'C': 1},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 1, 'B': 2, 'D': 4, 'E': 8},
    'D': {'B': 1, 'C': 4, 'E': 3, 'F': 6},
    'E': {'C': 8, 'D': 3},
    'F': {'D': 6}
}

source = 'A'
distances = dijkstra(graph, source)
print(distances)

##Requirements
Python 3.x

##Author
Harshitha Manjunatha
