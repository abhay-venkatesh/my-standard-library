from functools import wraps

def pre_condition(condition):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            assert condition(*args, **kwargs)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@pre_condition(lambda nums, target: sorted(nums) == nums)
def two_sum(nums, target):
    """
    nums = [-1, 0, 1, 2, 4, 6]
    target = 2
    
    If we want to find the two numbers that sum upto 2,
    we can simply walk inwards starting from both ends until
    we hit a combination that matches 2. This works because:
    assume that we did not find two numbers that sum to 2, but they 
    actually were in the list. 

    That would mean that we either incremented, or decremented i or j,
    when we should not have had. 

    When do we increment i or decrement j? 
    We increment i when nums[i] + nums[j] < target. If we did not find
    two numbers, but they did exist, that would mean that we should have
    not incremented i when nums[i] + nums[j] < target, but that would not
    happen because ...

    The smallest possible sum is nums[0] + nums[1],
    and the largest possible sum is nums[-1] + nums[-2]. 

    Therefore, to get smaller, we decrement j, 
    and to get bigger, we increment i. 

    Consider our example, 
    nums = [-1, 0, 1, 2, 4, 6]
    target = 2

    nums[0] + nums[5] == 5
    nums[0] + nums[4] == 3

    By incrementing i, we necessarily increase the sum, because every
    value on the left of i is >= the value at i. 
    """
    i = 0
    j = len(nums) - 1
    while i < j: 
        if nums[i] + nums[j] == target:
            return [nums[i], nums[j]]
        elif nums[i] + nums[j] > target:
            j -= 1
        else: 
            i += 1

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        
        nums = [-2,0,1,1,2]
        threeSums = [
            [-2,0,2]
        ]
        """
        threeSums = []
        nums.sort()
        i = 0
        while i < (len(nums)-2):
            if i == 0 or (i > 0 and nums[i] != nums[i-1]):
                twoSums = self.twoSums(nums[i+1:], -nums[i])
                for twoSum in twoSums:
                    threeSum = [nums[i]]
                    threeSum.extend(twoSum)
                    threeSums.append(threeSum)
            i += 1
            
        return threeSums
        
        
    def twoSums(self, nums, target):
        i = 0
        j = len(nums) - 1
        twoSums = []
        while i < j: 
            if nums[i] + nums[j] == target:
                twoSums.append([nums[i], nums[j]])
                i += 1
                j -= 1
                while i < j and nums[i] == nums[i-1]:
                    i += 1
                while i < j and nums[j] == nums[j+1]:
                    j -= 1
            elif nums[i] + nums[j] > target:
                j -= 1
            else: 
                i += 1
        return twoSums
                
def main():
    sol = two_sum([-1, 0, 1, 2, 4, 6], -1)
    print(sol)

if __name__ == '__main__':
    main()