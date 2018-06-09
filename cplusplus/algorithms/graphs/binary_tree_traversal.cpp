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
#include <deque>
#include <iostream>

using namespace std;

class Node {
public:
  Node(int val) : val(val) {
    left = NULL;
    right = NULL;
  }
  int val;
  Node* left;
  Node* right;
};

class BinaryTree {
  deque<Node*> stack_;
  Node* root_;
public:
  BinaryTree(Node* root) : root_(root) {
    setup_stack(root_);
  }
  /*
    T <- get_test_binary_tree()

    In-Order Traversal:
    6 2 5 1 7 4 3

    Test Run:
    stack_ = []

    output order:
    6 2 5 1 7 4 3
  */
  Node* get_next_in_order() {
    if(stack_.size() == 0) {
      return NULL;
    }
    Node* curr = stack_.front();
    stack_.pop_front();
    setup_stack(curr->right);
    return curr;
  }
  void setup_stack(Node* node) {
    if(node == NULL) return;
    stack_.push_front(node);
    setup_stack(node->left);
  }
};

/*
  3 - 4
 /     \
1       7
 \
  2 - 5
    \
      6
*/
BinaryTree* get_test_binary_tree() {
  Node* node1 = new Node(1);
  Node* node2 = new Node(2);
  Node* node3 = new Node(3);
  Node* node4 = new Node(4);
  Node* node5 = new Node(5);
  Node* node6 = new Node(6);
  Node* node7 = new Node(7);
  node1->left = node2;
  node1->right = node3;
  node2->right = node5;
  node2->left = node6;
  node3->left = node4;
  node4->left = node7;
  BinaryTree* tree = new BinaryTree(node1);
  return tree;
}

int main() {
  BinaryTree* tree = get_test_binary_tree();
  Node* curr;
  while((curr = tree->get_next_in_order()) != NULL) {
    cout << curr->val << " ";
  }
  cout << endl;

  return 0;
}
