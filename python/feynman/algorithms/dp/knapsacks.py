"""
--- The Unbounded Knapsack Problem ---
Given W = [w_0, ..., w_{n-1}] weights, and V = [v_0, ..., v_{n-1}] values,
and a knapsack that can hold total weight K, what set I of indexes 
i \in {0, ..., n-1} maximizes R = \sum_{i \in I} v_i such that 
K >= \sum_{i \in I} w_i? It is important to note that each of the items
are in infinite quantity. 

This is an optimization problem. The brute force requires us to take 
all possible combinations, of which there are:

For each item, we can choose to take 0, ..., K of it, assuming that each item
weighs at least 1. So, in the worst case, we have K^n total choices. This is
exponential in the problem size, and therefore, we want to find a better way.

The idea is that for the choices that we make for our items, there are 
overlaps in the choices. For choices made for subproblems, we can reuse
those choices to create solutions to larger problems. By remembering the choices
made, we can perform a time-space tradeoff, and solve the problem using
dynamic programming.

We just performed the first step in dynamic programming, which is to
characterize the optimal substructure of the problem: which means to identify
that the problem has overlapping subproblems, and solutions to subproblems can
be independently computed and then the original problem can be solved
using the solutions to subproblems.

Then, we recursively define a solution. Let us have a table that stores
the solution, that is, the maximum value of a knapsack of weight 
j \i {0, ..., K}.

solutions = [0 for _ in range(K+1)]
solutions[0] = 0 # cannot put anything in a knapsack that can hold weight 0
solutions[j] = max_{0 <= i <= 1}(solutions[0], solutions[1 - w_i] + v_i)

And we are done! We have a recursive formulation. 

Let us argue about why this produces an optimal solution. For each
subproblem of size j \i {0, ..., K}, we either take the best solution we have
so far, or, we try adding all possible values that might improve the solution.

If this process does not produce an optimal solution, then that would mean that
one of the subproblems did not have an optimal solution. But by construction,
each of the subproblems does have an optimal solution, because we have tried it.
"""