"""

--- All O(1) Data Structure ---

We will implement a data structure that supports
1. inc(key): inserts a new key with value 1, or increments an existing key by
             1. Key is guaranteed to be a non-empty string.
2. dec(key): If a key's value is 1, remove it. Otherwise, decrement by 1.
             If the key does not exist, do nothing. Key is guaranteed to be a
             non-empty string.
3. getMaxKey(): returns a key with maximal value. Returns "" if no keys.
4. getMinKey(): returns a key with minimal value. Returns "" if no keys.

The idea is to implement a 2D doubly-linked list, where the rows correspond to
values, and each column is a key for that value.

For instance,

$ ao = AllOne()
$ ao.inc("first")
$ ao.inc("second")
$ ao.inc("third")
$ ao.inc("second")
$ ao.display()

1: ["first"]--["third"]
        |
        |
2: ["second"]


"""
