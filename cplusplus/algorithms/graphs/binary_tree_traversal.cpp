/*

--- Traversing Binary Trees ---

We present three different ways in which we could traverse a binary tree:
1. In-Order Traversal (LVR): We visit the left subtree, then the node, and then
the right subtree.
2. Pre-Order Traversal (VLR): Visit the current node, then the left and right
subtrees.
3. Post-Order Traversal (LVR): Visit the left and right subtrees, and then the
current node.

*/

#include <vector>
#include <iostream>

using namespace std;

class Node {
public:

  int val;
  Node* left;
  Node* right;
}

/*
  3 - 4
 /     \
1       7
 \
  2 - 5
    \
      6
*/
Node* get_test_binary_tree() {
  Node node1{1};
  Node node2{2};
  Node node3{3};
  Node node4{4};
  Node node5{5};
  Node node6{6};
  node1.left = &node2;
  node1.right = &node3;
  node2.right = &node5;
  node2.left = &node6;
  node3.right = &node4;
  node4.left = &node7;
  return &node1;
}
