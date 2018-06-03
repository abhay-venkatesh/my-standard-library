#include <iostream>
#include <vector>

// TODO: Complete this

using namespace std;

void bfs(int curr, vector<vector<int>> graph,
         vector<vector<bool>> visited) {

  for(const auto& neighbor: graph[curr]) {
    if(visited[curr][neighbor] == false) {
      cout << neighbor << " ";
    }
  }

  for(const auto& neighbor: graph[curr]) {
    if(visited[curr][neighbor] == false) {
      visited[curr][neighbor] = true;
      bfs(neighbor, graph, visited);
    }
  }
}

void bfs(vector<vector<int>> graph) {
  vector<vector<bool>> visited(graph.size(),
                               vector<bool>(graph.size(), 0));

  bfs(0, graph, visited);
}

int main() {
  vector<vector<int>> graph = {
    {1,2,3},
    {},
    {},
    {4,5},
    {},
    {}
  };
  bfs(graph);
}
