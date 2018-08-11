import random

class RandomizedSet(object):
    """
    We want to be able to getRandom() in O(1)-time. This is easy if we can
    index into our data structure in O(1)-time. However, in order to do that,
    we need to be able to maintain a unique indexing over our data structure
    in O(1)-time.

    The issue is that we can easily insert, and getRandom() in O(1)-time by
    simply incrementally attaching a number to each inserted item,
    but then when we delete items, the deleted indexes are no longer mapped.

    One thing we could do is to push the deleted indexes into a stack,
    and then pull from the stack instead of adding a new number.

    count = 1
    stack = [0]
    table = {
        2:1
    }
    indexes = {
        1:2
    }

    insert(1) -> True
    remove(2) -> False
    insert(2) -> True
    getRandom() -> 2
    remove(1) -> True  

    But now if we do getRandom() then we cannot avoid the deleted index
    in O(1)-time. What if also have a getMax() in constant time, and then
    whenever something is deleted, we replace the max number with the deleted
    number. 

    So, in this case, we would have deleted (1 -> index:0), and then, 
    updated (2 -> index:1) to (2 -> index:0).

    We can maintain a stack of max numbers that keep getting updated whenever
    we delete. 

    To recap,
    when we insert, we update the stack with the new max number,
    and then add an entry to the table and indexes dicts, and increment
    the count counter.

    When we delete, we replace the deleted index with the max number from the 
    stack, and decrement the counter.

    Then, when we get random by simply generating a number between
    0 and count. 

    But we don't really need a stack to maintain maxes because counter
    actually does that for us. 

    self.count = 0
    self.table = {}
    self.indexes = {}

    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = {}
        self.indexes = {}
        self.count = 0

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.table.keys():
            return False

        self.table[val] = self.count
        self.indexes[self.count] = val
        self.count += 1
        return True


    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.table.keys():
            return False

        deleted_index = self.table[val]
        del self.table[val]

        self.count -= 1
        val_with_max_index = self.indexes[self.count] 
        del self.indexes[self.count]
        self.indexes[deleted_index] = val_with_max_index
        self.table[val_with_max_index] = deleted_index

        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        if self.count == 0:
            return -1
        if self.count == 1:
            return self.indexes[0]

        ri = random.randint(0, self.count - 1)
        return self.indexes[ri]

def main():
    """
    self.table = {
        1: 0
    }
    self.indexes = {
        0: 1,
    }
    self.count = 1

    -- remove(0) --
    deleted_index = 0
    val_with_max_index = 1

    """
    rs = RandomizedSet()
    rs.insert(0)
    rs.remove(0)
    rs.insert(-1)
    print(rs.remove(0))

        
if __name__ == "__main__":
    main()

