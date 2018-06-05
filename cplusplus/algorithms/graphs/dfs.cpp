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

/*

-------Correctness-------
The goal of DFS is to produce a traversal depth-first,
that is, to go in a direction until it is not possible to go any
further, and then try another path.

Here, we begin with a root node, and then perform DFS from there.
First, we visit the root node, but checking if it has been previously
visited. In this way, we never visit any node twice.

I admit that this might be slighly less efficient since there are
more than necessary function calls being made, but the asymptotic
complexity should stay the same.

After visiting each node, we call dfs on each of its neighbors.
This recurses in the direction of first neighbor on each neighbor,
and stops when no neighbors are left. This is DFS.

-------Time Complexity-------
We count the total number of function calls to DFS. First,
we will call DFS once at least on each node. Then, for each node,
we will call DFS on each of its neighbors. This leads to a
worst case complexity of O(V + E).

Now, if n is our problem size, then in the worst case, we can have
a fully connected graph. In a fully connected graph, each node is
connected to every other node.

So, if there are n nodes, then there are n + (n-1) + (n-2) + ... + 1
or equivalently, 1 + 2 + ... n = n(n+1)/2 edges.

Therefore, we have O(n^2) complexity.

*/
