def min_max(nums):
    if not nums:
        raise ValueError
    
    return (min(nums), max(nums))
#тест кейсы
#print(min_max([3, -1, 5, 5, 0]))
#print(min_max([42]))
#print(min_max([-5, -2, -9]))
#print(min_max([1.5, 2, 2.0, -3.1]))
#print(min_max([]))