/*
The Activity Selection Problem

We want to select activities associated with start times
start_times = [], and end times end_times = [].

Our goal is to select the most amount of activities that are
non-overlapping.

--- The optimal substructure of the problem ---
Can we solve subproblems of this problem independently,
and then use the subproblems to construction a solution to the
original problem?

Say we have the solution to some subproblem S[i][j],
that includes all activities beginning at i, and ending before j.

Can we construct a solution to a larger problem S[i][j+1]?
The decision here becomes only one that of whether an activity can
be added or not.

Consider the following example,
start_times = [s1, s2, ...]
end_times = [e1, e2, ...]

*/

int main() {
  return 0;
}
