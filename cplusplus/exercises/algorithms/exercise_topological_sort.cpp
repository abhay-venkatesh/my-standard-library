
/*

A topological sort is an ordering of a DAG in which each
node is visited only after all its parents (dependencies)
have been visited.

input:
0-->1-->2-->3
|   ^
|   |
 -->4-->5
|
 -->6

output:
0 4 1 2 3 5 6 (one possible)

Algorithm 1:


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
