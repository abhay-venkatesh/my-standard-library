def twoSum(self, nums, target):
        """
        [-1, 0, 1, 2, -1, -4]
        
        target = 2
        num = 1
        
        table = {-1}
        
        num - table.get(target - num) == 0:
            return [num, table.get(target - num)]
    
        """
        bag = set()
        for num in nums:
            bag.add(num)
            
            if target - num in bag:
                return [num, target - num]
                
def main():
    print(twoSum([-1, 0, 1, 2, -1, -4]))

if __name__ == '__main__':
    main()