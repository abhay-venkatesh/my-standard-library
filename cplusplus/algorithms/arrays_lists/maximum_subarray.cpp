/*

--- The Maximum Subarray Problem ---

Given an array of negative and positive numbers (and 0),
return the largest subarray possible.

input = < 1 -2 4 -5 8 >
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

int[] kadane(int[] input) {
  if((sizeof(input)/sizeof(int)) == 0) return 0;
  int max_till_now = input[0];
}

int main() {
  int[] input = { 1, -2, 5, -4, 8};
  int[] output = kadane(input);
  return 0;
}
