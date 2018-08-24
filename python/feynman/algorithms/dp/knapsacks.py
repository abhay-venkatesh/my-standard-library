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

"""
--- The 0/1 Knapsack ---
We make a slight change to the unbounded knapsack problem: the items are now
in a finite quantity. Therefore, it is not just important to have solutions
to smaller knapsacks, but we also need to know what items were used 
in that solution. Therefore, we need solutions to subproblems along two
dimensions:
1. Items used
2. Weight

solutions = [[0 for _ in range(K+1)] for _ in range(len(W)+1)]

We illustrate with a toy problem:
W = [1, 2, 3, 4]
V = [1, 3, 7, 15]
K = 4

solutions = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

solutions[i][j] is the solution to a knapsack of weight j using items 
[-1, ..., i-1], where -1 represents no item.

solutions[0][j] for all j are all 0, since knapsacks of weight 0 cannot hold anything,
and solutions[i][0] for all i are all 0, since i = 0 represents -1, no item,
so we cannot have any value if we cannot take any items.

fix j = 1, then
solutions[i][1] = 
if item at i fits in knapsack:
    solutions[i[1] = max(
        solutions[i-1][1], 
        value(i) + solutions[0][1 - weight(i)]
    )
else:
    solutions[i][1] = solutions[i-1][1]

Why does this work? A solution to subproblem[i][j] is constructed using
only one instance of each item. This is true because of the line:

solutions[1][1] = max(
    solutions[i-1][1], 
    value(i) + solutions[0][1 - weight(i)]
)

Why is each version of this optimal? We took each item at most once, 
and, we took the maximum possible version of the combination of items, 
and tried each item, and tried to fit in in the knapsack. 

If this solution is wrong, then the subproblem solution is wrong, which is
false by construction
"""