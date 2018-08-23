def twoSum(nums, target):
        bag = set()
        for num in nums:
            if target - num in bag:
                return [num, target - num]
                
            bag.add(num)
                
def main():
    print(twoSum([0, 1, -1], 0))

if __name__ == '__main__':
    main()