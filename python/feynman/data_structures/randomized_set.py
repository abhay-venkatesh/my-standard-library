import random

class RandomizedSet:
    """
    count = 1
    vals = {
        0: 2
    }
    indices = {
        2: 0
    }
    
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.count = 0
        self.vals = {}
        self.indices = {}
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.indices.keys():
            return False
        
        self.vals[self.count] = val
        self.indices[val] = self.count
        self.count += 1
        return True
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.indices.keys():
            return False
        
        self.count -= 1
        
        index = self.indices.pop(val, None)
        self.vals.pop(index, None)
                
        max_indexed_val = self.vals.pop(self.count, None)
        self.indices[max_indexed_val] = index
        self.vals[index] = max_indexed_val
        return True
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        index = random.randint(0, self.count - 1)
        return self.vals[index]

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
    randomSet  = RandomizedSet()
    randomSet.insert(1)
    randomSet.remove(2)
    randomSet.insert(2)
    randomSet.getRandom()
    randomSet.remove(1)
    randomSet.insert(2)
    print(randomSet.getRandom())
        
if __name__ == "__main__":
    main()

