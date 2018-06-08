/*
The Activity Selection Problem

We want to select activities associated with start times
start_times = [], and end times end_times = [].

Our goal is to select the most amount of activities that are
non-overlapping.

--- Optimal Substructure of the Activity Selection Problem ---
Let S[i][j] denote the set of all activities with starting time i and
ending time before j.

Can we construct a solution for problem S[i][j] from subproblems?

Basically, can we write

S[i][j] = {
case 1: ...,
case 2: ...,
case 3: ...,
.
.
}

?

Consider the following example,
start_times = [1, 3, 5, 9]
end_times = [3, 4, 7, 10]

S[][] = [
  [0,0,0,0,0],
  [0,0,0,0,0],
  [0,0,0,0,0],
  [0,0,0,0,0],
  [0,0,0,0,0],
]

S[1][1] = ? =

--- The Greedy Solution ---

algorithm:
  sort items by end_times
  greedily pick item with earliest end_time

proof:
  maximal subset must contain the activity with earliest end time
  if it did not,
  TODO:
*/

int main() {
  return 0;
}
