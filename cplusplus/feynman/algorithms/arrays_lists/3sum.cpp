#include <iostream>
#include <cstddef>
#include <vector>
#include <unordered_map>

using namespace std;

/*

Find 2 numbers such that their sum is equal to the the target

V = < 1 -2 4 5 -3 >
target = 1
output = < 4 -3 >

Algorithm:
  put dist(v, target) for each v in V in hash table
  then, go through the list and check if the the sum of

  hash_map.place(dist(v,target), v)

  Then, just go through V and check for each v
  if the key v is present, If it is, then get the matching value
  and you are done.

  Now, here, our target is 1.
  hash_map = < 0 3 -3 -4 4 >

*/
vector<int> two_sum(vector<int> V, int target) {
  unordered_map<int, int> map;
  for(const auto& v : V) {
    map[target - v] = v;
  }

  for(const auto& v : V) {
    if(map.find(v) != map.end()) {
      return vector<int>{map[v], v};
    }
  }

  return vector<int>{};
}

/*

Find 3 numbers such that their sum is equal to the target

v = < 1, -1, 4, 2 >
target = 4
output = < 1, -1, 4 >
sum = 4

Approach 1: For each number in v, perform two_sum
def two_sum(v, target):

*/

vector<int> three_sum(vector<int> V, int target) {
  for(int i = 0; i < V.size(); i++) {
    int diff = target - V[i];
    vector<int> output = two_sum(vector<int>{&V[i],&V[V.size()-1]}, diff);
    if(output.size() != 0) {
      output.push_back(V[i]);
      return output;
    }
  }
  return vector<int>{};
}


int main() {
  vector<int> output = three_sum(vector<int>{1,-1,4,2}, 4);
  for(const auto& c : output) {
    cout << c << " ";
  }
  cout << endl;
  return 0;
}
