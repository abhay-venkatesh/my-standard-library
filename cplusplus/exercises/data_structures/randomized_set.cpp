/*

--- RandomizedSet Analysis ---

Solution Credits: https://leetcode.com/renw/

RandomizedSet rs = new RandomizedSet();
rs.insert(1);
rs.insert(2);
rs.delete(1);
rs.insert(4);
rs.insert(1);

--- rs ---
nums = [2,1]
m = {
  2: 0,
  1: 1
}

--- delete(4) ---
last = 1

Basically, the idea is that you insert each item into an unordered_map,
mapped to its current index in nums.

Then, when deleting, simply delete the number and swap with the last item.

Why do we need to do this? Why not just place into a boolean map and lookup?
For instance,

insert(1)

map[1] -> true

then, check if the map contains 1 and then if it does, remove it.

This is fine, but then we cannot produce a number at random in constant time.
*/
class RandomizedSet {
public:
    /** Initialize your data structure here. */
    RandomizedSet() {

    }

    /* Inserts a value to the set.
    Returns true if the set did not already contain the specified element. */
    bool insert(int val) {
        if (m.find(val) != m.end()) return false;
        nums.emplace_back(val);
        m[val] = nums.size() - 1;
        return true;
    }

    /** Removes a value from the set.
    Returns true if the set contained the specified element. */
    bool remove(int val) {
        if (m.find(val) == m.end()) return false;
        int last = nums.back();
        m[last] = m[val];
        nums[m[val]] = last;
        nums.pop_back();
        m.erase(val);
        return true;
    }

    /** Get a random element from the set. */
    int getRandom() {
        return nums[rand() % nums.size()];
    }
private:
    vector<int> nums;
    unordered_map<int, int> m;
};
