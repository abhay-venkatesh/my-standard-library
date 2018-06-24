"""

--- Problem Statement ---

We are given a sequence of n matrices to be multiplied, and we wish to
compute the product A1*A2*A3...*An.

In order to compute this product, we must parenthesize the matrices to resolve
all ambiguities. Matrix multiplication is associative, so all parenthesizations
will yield the same solution.

A product of matrices is _fully parenthesized_ if it is either a single matrix,
or the product of two fully parenthesized matrix products.

"""
