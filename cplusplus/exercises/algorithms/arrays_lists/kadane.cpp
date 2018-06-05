#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

/*

To find the maximum subarray, the brute force would
simply be to check every possible subarray. If we search this
by starting with the full array, and then subtracting one piece
from each side, then we have 2^n subarrays. That is too bad.

We can be smarter about this. Do we really care about trying
every single subarray? Is there a way to exploit solutions
to subarrays? Consider the followign input

input = -1,4,3,-4,5,6,-2,6

If we have the solution to the problem for [-1,4,3,-4,5],
can we construct a solution to [-1,4,3,-4,5,6]?

The only determining factor is if we include 6 or not.
Does that improve or worsen our solution? What if 6 itself is
larger than the solution?

There are really 2 cases,
1) Include 6 in the running sum
3) Take only 6

since the array has to be contiguous. Now, it is possible
that since we are taking only contiguous arrays that the running
array becomes smaller than what is necessary. Therefore,
we maintain a global sum as well.

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
