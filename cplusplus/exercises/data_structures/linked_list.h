#include <cstddef>
#include <iostream>

#pragma once

using namespace std;

class Node {
public:
  Node(int val, Node* next) : val(val), next(next) {}
  int val;
  Node* next;
};

class LinkedList {
public:
  LinkedList() {
    length_ = 0;
    head_ = NULL;
  }
  void add(int val) {
    head_ = new Node(val, head_);
    length_++;
  }
  void print_list() {
    Node* curr = head_;
    while(curr != NULL) {
      cout << curr->val << " ";
      curr = curr->next;
    }
    cout << endl;
  }
private:
  int length_;
  Node* head_;
};
