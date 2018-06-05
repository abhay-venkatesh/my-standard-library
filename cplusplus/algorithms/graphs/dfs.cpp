/*

The idea of depth-first-search is that you go down a path in a graph
until you cannot go further down.

For instance, consider the following depth-first traversal,

input:
0-->1-->2-->3
|   ^
|   |
 -->4-->5
|
 -->6

output:
0 1 2 3 4 5 6

*/

#include<vector>
#include<iostream>
#include<unordered_map>

using namespace std;

class Node{
public:
  Node(int val) : val(val) {}
  vector<Node*> neighbors;
  int val;
};

void dfs(Node& root, unordered_map<int, bool>& visited) {
  if(visited.find(root.val) == visited.end()) {
    visited[root.val] = true;
    cout << root.val << " ";
  }
  for(const auto neighbor: root.neighbors)
      dfs(*neighbor, visited);
}

void dfs(Node root) {
  unordered_map<int, bool> visited;
  dfs(root, visited);
}

int main() {
  Node node0{0};
  Node node1{1};
  Node node2{2};
  Node node3{3};
  Node node4{4};
  Node node5{5};
  Node node6{6};
  node0.neighbors = vector<Node*>{ &node1, &node4, &node6 };
  node1.neighbors = vector<Node*>{ &node2 };
  node2.neighbors = vector<Node*>{ &node3 };
  node4.neighbors = vector<Node*>{ &node1, &node5 };

  dfs(node0);
}
