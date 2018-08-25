from functools import wraps

def pre_condition(condition):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            assert condition(*args, **kwargs)
            return func(*args, **kwargs) 
        return wrapper
    return decorator

def three_sum(nums):
    nums.sort()

@pre_condition(lambda nums, target: sorted(nums) == nums)
def two_sum(nums, target):
    print("YOLO")
                
def main():
    two_sum([0, 2, 1], 2)

if __name__ == '__main__':
    main()