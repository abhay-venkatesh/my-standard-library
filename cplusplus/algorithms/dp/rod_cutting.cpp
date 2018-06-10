/*

--- The Rod Cutting Problem ---
We have a rod of length L and we want to cut it up into some number of pieces.
For each piece of length l, we have an associated value V[l].

We want to maximize the total value that we can get from cutting up
the rod.

--- The Optimal Substructure of the Rod Cutting Problem ---

Let R[L] denote the solution to problem size L. If we had the solutions to
problem sizes 0-(L-1), can we find the solution to a problem of size L?

We can find the solution by splitting up the problem of size L into
smaller sizes, and by trying out

R[L] = max(V[L],R[1]+R[L-1], R[2]+R[L-2], ..., R[L-1]+R[1])

Alternatively, we can try
R[L] = max[V[1]+R[L-1], ..., V[L]+R[0]]

Since the solutions in the first formulation would be included in this one.

For instance,
L = 4
V = [2,4,8,12]

R[0] = 0
R[1] = max(2) = 2
R[2] = max(4,2+2) = 4
R[3] = max(8,2+4) = 8
R[4] = max(12,2+8,4+4) = 12

--- Reconstructing a Solution from the Optimal Value ---
Now that we have filled out our table R, we want to use it to reconstruct a
solution. We want to find basically where all the cuts were made.

We start off with R[4], we know that the cut was made at 12 because that is V[L]
So we basically check the max condition again, and see what cut was chosen
recursively.
*/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

/*
L = 4
V = [0,3,4,10,12]

R[0] = 0
R[1] = 3
R[2] = 6
R[3] = 10
R[4] = 13

*/
void construct_solution(
  vector<int>& solution,
  vector<int> table,
  vector<int> values
) {

  if(*table.end() == *values.end()) {
    solution.push_back(table.size()-1);
    return;
  }

  for(int l = table.size()-1; l >= 0; l--) {
    for(int j = 1; j <= l; j++) {
      if(table.at(l) == (values[j]+table[l-j])) {
        if(l-j != 0) {
          solution.push_back(l-j);
          break;
        }
      }
    }
  }
}

vector<int> rod_cutting(vector<int> values) {
  int length = values.size()-1;
  vector<int> table = { 0 };
  int max_value = 0;
  for(int l = 1; l <= length; l++) {
    max_value = values[l];
    for(int j = 1; j <= l; j++) {
      if((values[j]+table[l-j]) > max_value)
        max_value = values[j]+table[l-j];
    }
    table.push_back(max_value);
  }
  cout << max_value << endl;

  vector<int> solution;
  construct_solution(solution, table, values);
  return solution;
}

int main() {
  vector<int> output = rod_cutting(vector<int>{0,1,4,10,12});
  for(const int &n: output) {
    cout << n << " ";
  }
  cout << endl;
  return 0;
}
