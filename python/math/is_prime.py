"""
--- The Sieve of Erastothenes ---

We can check if a number is a prime by checking if every number up until that
number divides it. This is an O(n) problem. We can improve this by only
checking up until sqrt(n).

Theorem: A number n is prime if and only if all numbers up until sqrt(n) do not
divide n.

Proof: By sieve of Erastothenes, we know that a number n is prime if and only
if every number up until n does not divide n (other than 1).

If a number is not a prime, then it is divisible by some m in the range
[1, sqrt(n)].

For instance, all even numbers above 2 are not prime, and are divisble by 2.
The square root of every even number above 2 is greater than or equal to 2.

For every odd number that is not a prime, for instance 35, is divisble by 5,
which is less than sqrt(35). Why is this the case?

Think about factoring a number. The shortest possible factoring for a number
that is not prime is 2 numbers, each of which are not 1 or the number itself.
It is not possible for these 2 numbers to both be greater than the square root
of the number. If there are more than 2 factors that are not 1 or the number
itself, then the numbers will be even smaller. The largest possible factor
of a non-prime number that is not 1 or the number itself, therefore, has to be
the square root of the number.
"""
