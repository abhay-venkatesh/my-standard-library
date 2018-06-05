#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

/*

input = -1,4,3,-4,5,6,-2,6
max_ending_here = 12
max_so_far = 14

*/

int kadane(vector<int> input) {
  int max_ending_here = input.at(0), max_so_far = input.at(0);
  for(const auto& n: vector<int>{&input[1],&input[input.size()-1]}) {
    max_ending_here = max(n, max_ending_here + n);
    max_so_far = max(max_ending_here, max_so_far);
  }

  return max_so_far;
}

int main() {
  int max_sum = kadane(vector<int>{-1,4,3,-4,5,6,-2,6});
  cout << max_sum << endl;

  return 0;
}
