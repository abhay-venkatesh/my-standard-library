"""
The idea of insertion sorting is to sort as if you're sorting a deck of cards.
You iteratively choose a card from the deck, and place it in the right position 
in your hands.

For instance, consider the following example array:
A = [1, 7, 4, 5, 2, 9]

Then,
[1, 7, 4, 5, 2, 9]
|
    ^

[1, 7, 4, 5, 2, 9]
    |
       ^

[1, 4, 7, 5, 2, 9]
       |
          ^

[1, 4, 5, 7, 2, 9]
          |
             ^

[1, 2, 4, 5, 7, 9]
             |
                ^
                
[1, 2, 4, 5, 7, 9]
                |
                   ^
"""

def insertion_sort(A):
    for k in range(len(A) - 1):
        i = k
        key = A[i + 1]
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key

"""
--- Loop Invariants and Correctness ---

The loop invariant is something that is true at initialization of the loop,
maintainance of the loop, and termination of the loop. We define the
invariant in such a way that if we can show that the invariant is true 
at all these times, then we can be sure that our algorithm is correct.

"""