def min_max(nums):
    if not nums:
        raise ValueError
    
    return (min(nums), max(nums))