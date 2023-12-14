# Breadth First Search (BFS) Algorithm

Breadth First Search (BFS) is a searching algorithm used to explore nodes and edges in a graph or to navigate a grid map in order to find the shortest path from a start point to an end point.

## Graph Representation
![Graph](graph.gif)

## Grid Map Representation
![Grid Map](grid.gif)

To apply BFS on a grid, the first step is to convert the empty grid into a matrix where 0 represents an obstacle, and 1 represents a free cell.
![Grid to Matrix](matrix_pic.png)

To convert an empty grid to a matrix of 0s and 1s, it's necessary to specify the priority for the direction vector. For example, one might start by walking up -> down -> left -> right, or follow a different priority, including diagonal directions.
![Direction Priority](direction_pic.png)

Once the conversion is complete, the path from the start point to the end point can be obtained by traversing in reverse from the end point to the start point. The algorithm identifies the next point for each cell to achieve the end point.
For example:
- Start: 1
- End: 10
- Path: 1 -> 3 -> 6 -> 10
![Path Example](path.gif)

## Output from Python Script
![Output](output_pic.png)

To execute the Python script, use the following command:
```bash
rosrun bfs_path_planning_pkg bfs_algorithm.py
