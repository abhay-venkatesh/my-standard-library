#include <iostream>
#include <vector>
#include <limits>

using namespace std;

void swap(vector<int> &v, int i, int j) {
  int temp = v.at(i);
  v.at(i) = v.at(j);
  v.at(j) = temp;
}

void reverse(vector<int> &v, int i, int j) {
  while(j > i) {
    swap(v, i, j);
    i++;
    j--;
  }
}

/*
Given a list
L = [1, 2, 3]

produce the next lexicographical permutation,
output = [1, 3, 2]

If there is no next lexicographical permutation, that is,
the items are in descending order, then produce the ascending order of it.

For instance,
input = [3, 2, 1]
output = [1, 2, 3]

Approach 1: Brute force
Try all permutations, but this is O(n!). Cannot try.

Approach 2:
Find first number from right that is decreasing
Swap that number with the first larger number on its right
Reverse the remaining array
*/

vector<int> next_permutation(vector<int> v) {

  // TODO:

  swap(v, i, next_largest_i);
  reverse(v, next_largest_i, v.size()-1);

  return v;
}

int main() {
  vector<int> output = next_permutation(vector<int>{4,3,2,1});
  for(const auto& c : output) {
    cout << c << " ";
  }
  cout << endl;
  return 0;
}
