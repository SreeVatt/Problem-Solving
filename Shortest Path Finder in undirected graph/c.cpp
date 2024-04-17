#include <iostream>
#include <vector>
#include <queue>

using namespace std;

// Function to represent the graph as an adjacency list
vector<vector<int>> graph;

// Function to add an edge to the graph
void addEdge(int u, int v) {
  graph[u].push_back(v);
  graph[v].push_back(u); // For undirected graphs
}

// Function to perform BFS and find the shortest path
vector<int> BFS(int source, int destination) {
  int n = graph.size();
  vector<bool> visited(n, false);
  vector<int> parent(n, -1); // Stores parent node in the path

  queue<int> q;
  q.push(source);
  visited[source] = true;

  while (!q.empty()) {
    int u = q.front();
    q.pop();

    // If destination is found, reconstruct the path
    if (u == destination) {
      vector<int> path;
      int current = u;
      while (current != -1) {
        path.push_back(current);
        current = parent[current];
      }
      reverse(path.begin(), path.end()); // Reverse to get the path from source to destination
      return path;
    }

    // Explore adjacent nodes
    for (int v : graph[u]) {
      if (!visited[v]) {
        visited[v] = true;
        parent[v] = u;
        q.push(v);
      }
    }
  }

  // Destination not reachable
  return vector<int>();
}

int main() {
  // Graph creation (replace with actual data for your delivery network)
  int numVertices = 6; // Example with 6 locations
  graph.resize(numVertices);
  addEdge(0, 1); // Warehouse connected to location 1
  addEdge(1, 2);
  addEdge(1, 3);
  addEdge(2, 4);
  addEdge(3, 4);
  addEdge(4, 5);  // Location 5 is the last customer

  // Example delivery route: Warehouse (0) -> Customer 2 (via 1) -> Customer 4 (via 2) -> Customer 5
  int source = 0;
  int destination = 5;

  vector<int> shortestPath = BFS(source, destination);

  if (shortestPath.empty()) {
    cout << "Destination unreachable from source." << endl;
  } else {
    cout << "Shortest path from source to destination: ";
    for (int node : shortestPath) {
      cout << node << " -> ";
    }
    cout << "END" << endl;
  }

  return 0;
}