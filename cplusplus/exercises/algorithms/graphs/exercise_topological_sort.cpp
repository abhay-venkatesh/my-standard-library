
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

Algorithm 1: Kahn's Algorithm
Let L be the list to be returned
Add every node with no parents into a set/queue/stack S
While S is not empty:
  pull node n out from S
  put n into L
  for each neighbor m of n:
    remove the edge between n and m on the graph
    if m has no other edges then
      place m in S

if graph has edges then it is a cyclic graph
otherwise return L

Algorithm 2: DFS
Let L be the stack to be returned
Visit each node in DFS order
place the node into the stack after all children have been visited

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

void dfs_toposort(Node& root,
                           unordered_map<int, bool>& visited,
                           deque<Node*>& toposort
) {
  if(visited.find(root.val) != visited.end()) {
    return;
  }
  for(const auto neighbor: root.neighbors)
      dfs_toposort(*neighbor, visited, toposort);
  visited[root.val] = true;
  toposort.push_front(&root);
}

deque<Node*> dfs_toposort(Node root) {
  deque<Node*> toposort;
  unordered_map<int, bool> visited;
  dfs_toposort(root, visited, toposort);
  return toposort;
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

  deque<Node*> toposort = dfs_toposort(node0);
  for(const auto node: toposort)
    cout << node->val << " ";
  cout << endl;
}
