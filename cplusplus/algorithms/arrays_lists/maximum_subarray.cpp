/*

--- The Maximum Subarray Problem ---

Given an array of negative and positive numbers (and 0),
return the largest subarray possible.

input = < 1 -2 5 -4 8 >
output = < 4 -5 8 >
sum = 7

--- The Brute Force Solution ---

Try every possible subarray.

input = < 1 -2 4 -5 8 >
try 1 = < 1 -2 4 -5 >
try 2 = < -2 4 -5 8 >
try 3 = < 1 -2 4 >
try 4 = < -2 4 -5 >

There might be some space for dynamic programming here, since the subproblems
overlap. Without dynamic programming, the complexity is O(2^n) since for every
subarray we have 2 choices to decrease the size.

With dynamic programming, we have 3 instead of 4 tries for every 2 subproblems.
This will still be exponential.

--- Kadane's Algorithm ---

Overview: Kadane's algorithm is a dynamic programming algorithm that leverages the fact
that for every problem size of i, the maximum subarray for problem of size i+1
will either include the item at i+1 exclusively, or append the item at i+1 to
the solution to the problem of size i. This is because the array has to be
contiguous - we have to start a new subarray or continue the previous one we had.

Correctness: This will always cover the solution because we try all the options possible.
Given a solution of problem size i, the only possibilities for a problem of size
i+1 is that the solution either contains the solution to problem size i as a
prefix or it does not.

*/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> kadane(vector<int> input) {
  if(input.size() == 0) return vector<int>{};

  int max_so_far = input.at(0);
  int max_so_far_i = 0;
  int max_so_far_j = 0;
  int max_ending_here = input.at(0);
  int max_ending_here_i = 0;
  int max_ending_here_j = 0;
  for(int i = 0; i < input.size(); i++) {
    if(input.at(i) > max_ending_here + input.at(i)) {
      max_ending_here = input.at(i);
      max_ending_here_i = i;
      max_ending_here_j = i;
    } else {
      max_ending_here = max_ending_here + input.at(i);
      max_ending_here_j = i;
    }

    if(max_ending_here > max_so_far) {
      max_so_far = max_ending_here;
      max_so_far_i = max_ending_here_i;
      max_so_far_j = max_ending_here_j;
    }
  }
  cout << max_so_far_i << " " << endl;
  cout << max_so_far_j << " " << endl;

  return vector<int>{&input[max_so_far_i], &input[max_so_far_j+1]};
}

int main() {
  vector<int> input = { 1, -2, 5, -4, 8};
  vector<int> output = kadane(input);
  for(const auto& n:output) {
    cout << n << " ";
  }
  cout << endl;
  return 0;
}
