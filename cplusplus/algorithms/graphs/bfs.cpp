#include <iostream>
#include <vector>

using namespace std;

void bfs_recursive(int curr, vector<vector<int>> graph,
         vector<vector<bool>> visited) {

  for(const auto& neighbor: graph[curr]) {
    if(visited[curr][neighbor] == false) {
      cout << neighbor << " ";
    }
  }

  for(const auto& neighbor: graph[curr]) {
    if(visited[curr][neighbor] == false) {
      visited[curr][neighbor] = true;
      bfs_recursive(neighbor, graph, visited);
    }
  }
}

void bfs_recursive(vector<vector<int>> graph) {
  vector<vector<bool>> visited(graph.size(),
                               vector<bool>(graph.size(), 0));

  bfs_recursive(0, graph, visited);
}

void run_bfs_recursive() {
  vector<vector<int>> graph = {
    {1,2,3},
    {},
    {},
    {4,5},
    {},
    {}
  };
  bfs_recursive(graph);
}

class Node {
public:
  Node(int val) : val(val) {}
  int val;
  vector<Node*> neighbors;
}

// TODO:

/*

Algorithm:
  Q = queue()
  Q.push(root)
  while Q is not empty:
    curr = Q.pop()
    mark curr as visited
    for each neighbor n of curr:
      if n is not yet visited:
        Q.push(n)

*/
void bfs_iterative(Node& root) {

}

/*

Input:
0-->1-->2
|
\-->3-->5
|       ^
|       |
\-->4--/

Output:
0 1 3 4 2 5

*/
void run_bfs_iterative() {
  Node node0{0};
  Node node1{1};
  Node node2{2};
  Node node3{3};
  Node node4{4};
  Node node5{5};
  node0.neighbors = vector<Node*> { &node1, &node3, &node4 };
  node1.neighbors = vector<Node*> { &node2 };
}

int main() {
  return 0;
}
