
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

*/

#include<vector>
#include<deque>
#include<iostream>
#include<unordered_map>

using namespace std;

class Node{
public:
  Node(int val) : val(val) {}
  vector<Node*> neighbors;
  int val;
};

void dfs(Node& root, unordered_map<int, bool>& visited, deque<Node*>& toposort) {
  if(visited.find(root.val) != visited.end()) {
    return;
  }
  for(const auto neighbor: root.neighbors)
      dfs(*neighbor, visited, toposort);
  visited[root.val] = true;
  toposort.push_front(&root);
}

deque<Node*> dfs(Node root) {
  unordered_map<int, bool> visited;
  deque<Node*> toposort;
  dfs(root, visited, toposort);
  return toposort;
}

/*
--- Kahn's Algorithm for Topological Sorting ---

G <- Input Graph

algorithm kahn(G):
  Q = queue()
  T = list()
  Q <- all nodes n in G such that n has 0 in-degree
  while Q is not empty:
    curr = Q.pop()
    T.insert(curr)
    for each neighbor n of curr:
      remove edge between n and curr
      if n has 0 in-degree:
        Q.push(n)

  if Q is not empty:
    throw exception("Graph is not a DAG")
  else return T

Test:
G <- Input Graph:
0   1-->2-->3
|   ^
|   |
 -->4-->5
|
 -->6

Q = [1]
T = [0]
curr = 0


*/
void kahn() {


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

  deque<Node*> output = dfs(node0);
  for(const auto node: output)
    cout << node->val << " ";
  cout << endl;
  return 0;
}
